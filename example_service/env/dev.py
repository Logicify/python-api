from example_service.settings.base import *
import os

DEBUG = os.environ.get('DEBUG', '0') in ['1', 'true', 'True', 'yes', 'Yes']

DEFAULT_LOG_LEVEL = 'DEBUG'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': DEFAULT_LOG_LEVEL,
            'filters': [],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        # 'django.db.backends': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        # },
        'root': {
            'handlers': ['console', ],
            'level': DEFAULT_LOG_LEVEL,
        },
        'django.request': {
            'handlers': ['console', ],
            'level': 'ERROR',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', ],
            'propagate': True,
            'level': DEFAULT_LOG_LEVEL,
        },
    }
}

ALLOWED_HOSTS = ['*']