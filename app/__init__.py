from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("../config.py")

from . import views

from .posts import post_bp
app.register_blueprint(post_bp)

from .user import user_bp
app.register_blueprint(user_bp)