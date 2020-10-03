from .base import *
from dj_database_url import parse as db_url



DEBUG = False

ALLOWED_HOSTS=['backend-challenge5.herokuapp.com',]

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'orders',
    'USER': 'lucy',
    'PASSWORD': 'lucy',
}}