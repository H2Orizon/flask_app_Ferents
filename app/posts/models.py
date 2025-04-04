from app import db
from datetime import datetime as dt
from sqlalchemy.orm import backref

post_tags = db.Table(
    'post_tags',
    db.Column('post_id', db.ForeignKey('posts.id'),primary_key=True),
    db.Column('tag_id', db.ForeignKey('tags.id'),primary_key=True)
)

class Post(db.Model):
    __tablename__='posts'

    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    content=db.Column(db.Text, nullable=False)
    category=db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    author=db.relationship('User',backref=backref("posts",lazy="dynamic"),lazy="joined")
    is_active = db.Column(db.Boolean, default=True)
    date=db.Column(db.DateTime, default=dt.now())

    tags = db.relationship('Tag', secondary=post_tags, back_populates='posts')
    def __repr__(self):
        return f"<Post({self.title})>"
class Tag(db.Model):
    __tablename__='tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    posts = db.relationship('Post', secondary=post_tags, back_populates='tags')
    