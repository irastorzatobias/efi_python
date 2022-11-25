from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db/todo_app'

db = SQLAlchemy(app)