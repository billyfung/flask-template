import os


INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')


class BaseConfig:

    PROJECT = 'ohm'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = False

    ADMINS = ['email']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'secret key'

    LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')

    # Fild upload, should override in production.
    # Limited the maximum allowed payload to 16 megabytes.
    # http://flask.pocoo.org/docs/patterns/fileuploads/#improving-uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'uploads')


class DefaultConfig(BaseConfig):

    DEBUG = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://user@localhost/appdb'


class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
