'''
Contains all the settings for developing on a local workstation:
    * enable debug toolbar
    * don't send notification mails to the customer
    * ...
This is the default settings file if no specific settings are provided.
'''

from cmsproject.settings.development import *

IS_DEV_SERVER = False
IS_HTTP_SERVER = True

#CACHE_BACKEND = 'memcached://127.0.0.1:11211/?timeout=300&max_entries=300'

#DATABASE_ENGINE = 'mysql'
#DATABASE_NAME = 'cmsproject'
#DATABASE_USER = 'root'
#DATABASE_PASSWORD = ''
#DATABASE_HOST = ''
#DATABASE_PORT = ''