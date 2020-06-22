
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9b+g7%um-e+b4z+p6%qa25zr#8$saw+fi9u9+ys_2)4(ol*s8m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [os.environ['WEBSITE_SITE_NAME'] + '.azurewebsites.net','localhost', '127.0.0.1'] if 'WEBSITE_SITE_NAME' in os.environ else ['127.0.0.1']

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_rabbitmq.core.RabbitmqChannelLayer",
        "CONFIG": {
            "host": "amqp://admin:2plus2isFOUR@40.113.203.73/dct",
            # "ssl_context": ... (optional)
        },
    },
}

# ASGI_APPLICATION should be set to your outermost router
ASGI_APPLICATION = 'crystalp.routing.application'
WSGI_APPLICATION = 'crystalp.wsgi.application'


LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

USE_THOUSAND_SEPARATOR = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'frontend.apps.FrontendConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_datatables',
    'import_export',
    'channels',
    'mathfilters',
    'storages',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# CRISPY_FAIL_SILENTLY = not DEBUG

REST_FRAMEWORK = {
    # "DATE_INPUT_FORMATS": ["%Y-%m-%d"],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_datatables.filters.DatatablesFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
    'PAGE_SIZE': 30,
}

AUTH_USER_MODEL = 'frontend.User'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

IMPORT_EXPORT_USE_TRANSACTIONS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crystalp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'eveshelcare@gmail.com'
EMAIL_HOST_PASSWORD = 'Seansean24'
EMAIL_USE_TLS = True  # STARTTLS

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'eveshelcare@gmail.com'
EMAIL_HOST_PASSWORD = 'Seansean24'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
#----- Azure Serve static
DEFAULT_FILE_STORAGE = 'dct.custom_azure.AzureMediaStorage'
# STATICFILES_STORAGE = 'dct.custom_azure.AzureStaticStorage'
# STATIC_LOCATION = "static"
MEDIA_LOCATION = "dctpython"
AZURE_ACCOUNT_NAME = "payplusfileshare"
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
# STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
#-----Azure storage

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    ("images", "./images"),
    ("js", "./js"),
    ("assets", "./assets"),
]
