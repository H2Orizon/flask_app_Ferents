from flask import Blueprint

films_bp = Blueprint("films",
                     __name__,
                     static_folder="static",
                     template_folder="templates",
                     url_prefix="/films",
)
from . import views