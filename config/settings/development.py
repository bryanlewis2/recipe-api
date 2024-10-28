from .base import *


DEBUG = True
ALLOWED_HOSTS = ['http://recipe-api-v1-b9ab5586572a.herokuapp.com/', 'localhost', '127.0.0.1', '0.0.0.0']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
