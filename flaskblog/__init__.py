import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'e3d415735ac112a2262ff99a9b3680c0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mpatterson73@gmail.com'
app.config['MAIL_PASSWORD'] = 'reagan7705'
mail = Mail(app)

from flaskblog.users.routes import users  # user instance with the user blueprint
from flaskblog.posts.routes import posts  # posts instance with the posts blueprint
from flaskblog.main.routes import main  # main instance with the main blueprint

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)