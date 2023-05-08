from os import path
from flask import Flask
import mysql.connector
from flask_login import LoginManager


DB_NAME = "database"
DB_PATH = path.join(path.abspath('website'), DB_NAME)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)
cursor = db.cursor()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'zakaria'

    create_database()

    

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #if not login come here
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User().load_user(id)

    return app


def create_database():
    print("Creating the database....")
    try:
        global db, cursor
        cursor.execute("CREATE DATABASE IF NOT EXISTS mydatebase")
        db.commit()
        print("database created successfully..")

    except Exception as e:
        print(f"error: {e}")

