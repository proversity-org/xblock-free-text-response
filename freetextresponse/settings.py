# -*- coding: utf-8 -*-
"""
Settings for freetextresponse xblock
"""
import os
from path import Path as path

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': 'intentionally-omitted',
    },
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

INSTALLED_APPS = (
    'django_nose',
    'freetextresponse',
)
BASE_DIR = path(__file__).abspath().dirname()
TEMPLATE_DIRS = (
     os.path.join(BASE_DIR, 'templates/'),
)

SECRET_KEY = 'freetextresponse_SECRET_KEY'

USE_I18N = True

# Sourced from http://www.localeplanet.com/icu/ and wikipedia
LANGUAGES = [
    ('en', u'English'),
    ('ar', u'العربية'),  # Arabic
]
LANGUAGE_CODE = 'en'
LANGUAGE_DICT = dict(LANGUAGES)