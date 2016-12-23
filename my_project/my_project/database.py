import os

from django.conf import settings

engines = {
    'sqlite': 'django.db.backends.sqlite3',
    'oracle': 'django.db.backends.oracle',
}

def config():
    engine = engines['oracle']

    return {
        'ENGINE': engine,
        'NAME': os.getenv('DATABASE_NAME', ''),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
}

def debug():
    engine = engines['sqlite']

    return {
        'ENGINE': engine,
        'NAME': os.getenv('DATABASE_NAME', 'db.sqlite3'),
}
