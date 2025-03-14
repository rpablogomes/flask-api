from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random

db = SQLAlchemy()

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), unique=True)
    email=db.Column(db.String(120), unique=True)
    password=db.Column(db.Text(), nullable=False)
    created_at=db.Column(db.DataTime, default=datetime.now())
    updated_at=db.Column(db.DataTime, onupdate=datetime.now())
    bookmarks=db.relationship('Bookmark', backref="user")

    def __repr__(self) -> str:
        return f"User >> {self.username}"

class Bookmark(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    body=db.Column(db.Text, unique=True)
    url=db.Column(db.Text, unique=True)
    short_url=db.Column(db.String(3), unique=True)
    visits=db.Column(db.String(3), unique=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at=db.Column(db.DataTime, default=datetime.now())
    updated_at=db.Column(db.DataTime, onupdate=datetime.now())

    def generate_short_characters(self):
        characters = string.digits+string.ascii_letters
        picked_chars = ''.join(random.choices(characters, k=3))

        link=self.query.filter_by(short_url=picked_chars).first

        if link:
            self.short_url=self.generate_short_characters()
        else:
            return picked_chars
    def __init__(self, **kwargs):
        super.__init__(**kwargs)

        

    def __repr__(self) -> str:
        return f"Bookmark >> {self.url}"