from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_name = "config"):
    app = Flask(__name__)
    app.config.from_object(config_name)

    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():

        from . import views

        from .posts import post_bp
        app.register_blueprint(post_bp)

        from .user import user_bp
        app.register_blueprint(user_bp)
        from .films import films_bp
        app.register_blueprint(films_bp)
        from app.posts.models import Post

        # db.create_all()
        

    return app