"""
Django settings for naccsweb project.

Generated by 'django-admin startproject' using Django 1.11.23.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET', '4cEyK87ncSGPHPGdYCD8EPX%d$@5U^Yh6P0sw8qvkQuoL3&L@TWhgM%cs5')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

print("DEBUG MODE:", DEBUG)

ALLOWED_HOSTS = ['192.168.254.25', 'localhost', '192.168.254.34']

# Application definition

INSTALLED_APPS = [
    'watson',
    'league.apps.LeagueConfig',
    'settings.apps.SettingsConfig',
    'core.apps.CoreConfig',
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'naccsweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'naccsweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_DB'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/login'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

DJANGO_USE_S3 = os.environ.get('DJANGO_USE_S3', False)

if DJANGO_USE_S3:
    print("Using S3")
    # AWS Settings
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_DEFAULT_ACL = 'public-read'

    # Static Location
    AWS_STATIC_LOCATION = 'static'
    STATICFILES_STORAGE = 'naccsweb.storage_backends.StaticStorage'
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)

    # Public Media
    AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
    MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN,
                                    AWS_PUBLIC_MEDIA_LOCATION)
    DEFAULT_FILE_STORAGE = 'naccsweb.storage_backends.PublicMediaStorage'

    # Private Media
    AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
    PRIVATE_FILE_STORAGE = 'naccsweb.storage_backends.PrivateMediaStorage'
else:
    STATIC_ROOT = os.path.join(BASE_DIR, '../staticfiles/')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    MEDIA_URL = '/files/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'files')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'noreply@collegiatecounterstrike.com'
SERVER_EMAIL = 'noreply@collegiatecounterstrike.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@collegiatecounterstrike.com'

if os.environ.get('DJANGO_SECURE'):
    X_FRAME_OPTIONS = 'DENY'
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

if(os.environ.get('PAYPAL_MODE') == "live"):
    PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
elif(os.environ.get('PAYPAL_MODE') == "sandbox"):
    PAYPAL_CLIENT_ID = os.environ.get('SANDBOX_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('SANDBOX_SECRET_ID')
