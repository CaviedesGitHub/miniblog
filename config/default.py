# config/default.py

from os.path import abspath, dirname

# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))
print("BASE_DIR: ", BASE_DIR)
SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
print("SECRET_KEY: ", SECRET_KEY)
# Database configuration
SQLALCHEMY_TRACK_MODIFICATIONS = False
print("SQLALCHEMY_TRACK_MODIFICATIONS: ", SQLALCHEMY_TRACK_MODIFICATIONS)

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''

# Configuración del email
MAIL_SERVER = 'smtp.live.com' #'smtp-relay.gmail.com' #'aspmx.l.google.com' #'smtp.gmail.com' #'smtp.live.com'
MAIL_PORT = 587
MAIL_USERNAME = 'caviedes72@hotmail.com'
MAIL_PASSWORD = ''
DONT_REPLY_FROM_EMAIL = 'dontreply@infoerror.com'
ADMINS = ('LuisPadilla1250@gmail.com', )
MAIL_USE_TLS = True
MAIL_DEBUG = False

ITEMS_PER_PAGE = 3
ITEMSADMIN_PER_PAGE = 5