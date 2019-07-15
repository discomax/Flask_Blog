from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

from flaskblog.users.routes import users  # user instance with the user blueprint
from flaskblog.posts.routes import posts  # posts instance with the posts blueprint
from flaskblog.main.routes import main  # main instance with the main blueprint

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)