from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
    app.config["WTF_CSRF_SECRET_KEY"] = os.getenv('WTF_CSRF_SECRET_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from application.database.users import User, init_db
    db.init_app(app)
    
    login_manager = LoginManager(app)
    login_manager.login_view = "login"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from application.routes.prediction import prediction
    from application.routes.auth import auth
    app.register_blueprint(prediction)
    app.register_blueprint(auth)
    
    if not os.path.isfile("application/database/database.db"):
        app.app_context().push()
        init_db()
    
    return app

app = create_app()