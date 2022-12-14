from flask import request, jsonify, make_response
from flask_migrate import Migrate
from extensions import db, app

import models
import helpers

import uuid # Para generar id random
from werkzeug.security import generate_password_hash, check_password_hash  # Para el hash de las password, generacion de token
import jwt # Creacion de token de login
import datetime
from functools import wraps

migrate = Migrate(app, db)
# Decorador para trabajar con el token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = models.User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that action'})

    users = models.User.query.all()
    res = []

    if(users):
        for user in users:
            formatted_user = helpers.build_user(user)
            res.append(formatted_user)

        return jsonify({'users': res});

    helpers.no_user_found()


@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that action'})

    user = helpers.find_user(models.User, public_id)

    if not user:
        return helpers.no_user_found()

    formatted_user = helpers.build_user(user)

    return jsonify({"user": formatted_user})

@app.route('/user', methods=['POST'])
def create_user():

    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = models.User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created'})


@app.route('/user/<public_id>', methods=['PUT'])
def promote_user(public_id):
    user = helpers.find_user(models.User, public_id)

    if not user:
        return helpers.no_user_found()

    user.admin = True

    db.session.commit()
    return jsonify({'message': 'The user now is admin'})

@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that action'})

    user = helpers.find_user(models.User, public_id)

    if not user:
        return helpers.no_user_found()

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"})

@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = models.User.query.filter_by(name=auth.username).first()

    if not user:
        return helpers.no_user_found()

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)}, app.config['SECRET_KEY'] ) # Login de 5 minutos, la key va a ser usada para el encode del token

        return jsonify({"token": token})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'}) # Errores no contemplados

@app.route('/todo', methods=['GET'])
@token_required
def get_all_todos(current_user):
    todos = models.Todo.query.filter_by(user_id=current_user.id).all()

    output = []

    for todo in todos:
        output.append(helpers.build_todo(todo))

    return jsonify({'todos' : output})

@app.route('/todo/<todo_id>', methods=['GET'])
@token_required
def get_one_todo(current_user, todo_id):
    todo = models.Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message' : 'No todo found!'})

    return jsonify({'todo': helpers.build_todo(todo)})

@app.route('/todo', methods=['POST'])
@token_required
def create_todo(current_user):
    data = request.get_json()

    new_todo = models.Todo(text=data['text'], complete=False, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({'message' : "Todo created!"})

@app.route('/todo/<todo_id>', methods=['PUT'])
@token_required
def complete_todo(current_user, todo_id):
    todo = models.Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message' : 'No todo found!'})

    todo.complete = True
    db.session.commit()

    return jsonify({'message' : 'Todo item has been completed!'})

@app.route('/todo/<todo_id>', methods=['DELETE'])
@token_required
def delete_todo(current_user, todo_id):
    todo = models.Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message' : 'No todo found!'})

    db.session.delete(todo)
    db.session.commit()

    return jsonify({'message' : 'Todo item deleted!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)