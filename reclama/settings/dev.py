from base import *


# Security
SECRET_KEY = 'changeme'
ALLOWED_HOSTS = []

# Debug
DEBUG = True
TEMPLATE_DEBUG = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../', 'db.sqlite3'),
    }
}