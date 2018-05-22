import os
basedir = os.path.abspath(os.path.dirname(__file__))


class ProductionConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    PORT = int(os.getenv('PORT', 5000))
    FIXER_ACCESS_KEY = os.getenv('FIXER_ACCESS_KEY')
    HISTORICAL_INTERVAL_DAYS = 7 * 2


class DevelopmentConfig(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database_dev.db')
    SQLALCHEMY_ECHO = True
    PORT = 5000
    FIXER_ACCESS_KEY = '871649a063434b259b496d15b9568fb0'
    HISTORICAL_INTERVAL_DAYS = 7


class TestingConfig(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_ECHO = True
    PORT = 5000
    FIXER_ACCESS_KEY = os.getenv('FIXER_ACCESS_KEY')
    HISTORICAL_INTERVAL_DAYS = 7