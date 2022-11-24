from flask import jsonify

def find_user(model, public_id):
    return model.query.filter_by(public_id=public_id).first()

def build_user(user):
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['admin'] = user.admin
    return user_data

def build_todo(todo):
    todo_data = {}
    todo_data['id'] = todo.id
    todo_data['text'] = todo.text
    todo_data['complete'] = todo.complete
    return todo_data

def no_user_found():
    return jsonify({"message": 'No user found'})
