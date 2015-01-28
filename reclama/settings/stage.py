from os import getenv
from base import *


# Security
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'changeme')
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*')

# Debug
DEBUG = True
TEMPLATE_DEBUG = True

# Database
import dj_database_url
DATABASE_URL = getenv('DJANGO_DATABASE_URL', 'sqlite:///db.sqlite3')
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}
