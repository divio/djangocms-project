'''
Contains all the settings for developing on a local workstation:
    * enable debug toolbar
    * don't send notification mails to the customer
    * ...
This is the default settings file if no specific settings are provided.
'''

from cmsproject.settings.development import *

CACHE_BACKEND = 'dummy://'

#DATABASE_ENGINE = 'mysql'
#DATABASE_NAME = ''
#DATABASE_USER = ''
#DATABASE_PASSWORD = ''
#DATABASE_HOST = ''
#DATABASE_PORT = ''