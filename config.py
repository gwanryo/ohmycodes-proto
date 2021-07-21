import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'sharecode.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
