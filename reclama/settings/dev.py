from os import getenv
from base import *  # noqa


# Security
SECRET_KEY = os.getenv('SECRET_KEY', 'changeme')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*')

# Debug
DEBUG = True
TEMPLATE_DEBUG = True

# Database
import dj_database_url
DATABASE_URL = getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}
