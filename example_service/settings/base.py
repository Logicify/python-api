import socket

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VERSION = "1.0.0"
API_VERSION = 1

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lkjt534ofdpsafls356u45ijtkifjs;alfskloxchok6jfhs'
DEBUG = False
ALLOWED_HOSTS = []

try:
    HOSTNAME = socket.gethostname()
except:
    HOSTNAME = 'localhost'

from .app_structure import *