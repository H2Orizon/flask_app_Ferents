from app import db
from datetime import datetime as dt
from sqlalchemy.orm import backref
from app.user.models import User

film_tags_conect = db.Table(
    'film_tegs_many_to_many',
    db.Column('film_id', db.ForeignKey('films.id', ondelete='CASCADE'), primary_key=True),
    db.Column('tag_id', db.ForeignKey('film_tegs.id', ondelete='CASCADE'), primary_key=True)
)

class Films(db.Model):
    __tablename__ = "films"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=backref("films", lazy="dynamic"), lazy="joined")
    add_to_db = db.Column(db.DateTime, default=dt.now())
    duration = db.Column(db.Time, nullable=False)
    img_file = db.Column(db.String(20), nullable=True , default="Default.png")
    film_tags = db.relationship('FilmTags', secondary=film_tags_conect, back_populates='films')

    def __repr__(self):
        return f"<Add({self.name})>"
    
class FilmTags(db.Model):
    __tablename__ = "film_tegs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    films = db.relationship('Films', secondary=film_tags_conect, back_populates='film_tags')