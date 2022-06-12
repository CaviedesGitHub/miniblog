# config/dev.py

from .default import *

APP_ENV = APP_ENV_DEVELOPMENT
print("APP_ENV: ", APP_ENV)
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/miniblog'
print("SQLALCHEMY_DATABASE_URI: ", SQLALCHEMY_DATABASE_URI)