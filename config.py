import os

SECRET_KEY = "secret"
FLASK_DEBUG = 1
SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = os.path.join(os.getcwd(),'app','user', 'static', 'images', 'profiles')
UPLOAD_FOLDER2 = os.path.join(os.getcwd(),'app','films', 'static', 'images', 'films')