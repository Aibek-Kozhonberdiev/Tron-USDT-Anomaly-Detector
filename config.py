import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = eval(os.environ.get('FLASK_DEBUG', "True"))
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('FLASK_KEY', 'my-secret-key')
    STATIC_FOLDER = 'static'
    TEMPLATE_FOLDER = 'templates'
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
    MIXER = os.environ.get('MIXER')
