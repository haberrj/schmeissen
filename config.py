import os

from dotenv import load_dotenv


base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '.env'))


class Config:
    SECRET_KEY = 'development'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LANGUAGES = ['en'] # no german speaking allowed


class TestConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')

    ADMINS = ['admin@schmeissen.io']


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    ADMINS = ['admin@schmeissen.io']