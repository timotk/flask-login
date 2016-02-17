import os

IP = '127.0.0.1'
PORT = 5000
DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SECRET_KEY = ''
WTF_CSRF_SECRET_KEY = ''
