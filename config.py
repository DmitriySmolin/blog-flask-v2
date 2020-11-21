class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test1.db'
    SECRET_KEY = 'something very secret'


    ###  Flask-security  ###
    SECURITY_PASSWORD_SALT = "salt"
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
