import os
import hashlib
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
     hashlib.sha1(os.urandom(128)).hexdigest(), 
)

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
FORCE_SQLITE = os.environ.get('FORCE_SQLITE', 'no') == 'yes' # Used to debug

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
INTERNAL_IPS = os.environ.get('INTERNAL_IPS', 'localhost,127.0.0.1').split(',') 

DB_TABLE_NAME = os.environ.get('DB_TABLE_NAME', 'custom_db_table_name')

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'customers',
]
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
ROOT_URLCONF = 'my_project.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'customers.context_processors.external_urls',
            ],
        },
    },
]
WSGI_APPLICATION = 'my_project.wsgi.application'

from . import database
if DEBUG or FORCE_SQLITE:
    DATABASES = {
        'default': database.debug()
    }
else:
    DATABASES = {
        'default': database.config()
    }

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
DOCKERFILE_URL = os.environ.get('DOCKERFILE_URL', '#')
GIT_PROJECT_URL = os.environ.get('GIT_PROJECT_URL', '#')
