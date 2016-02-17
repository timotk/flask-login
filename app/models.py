from datetime import datetime
from app import db
from werkzeug import generate_password_hash, check_password_hash
from sqlalchemy import Sequence, Column, Integer, String, Boolean, DateTime


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('userid'), primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(256))
    created_on = Column(DateTime, default=datetime.now, nullable=True)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)
