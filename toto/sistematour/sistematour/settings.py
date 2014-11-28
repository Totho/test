

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pss$2@y6_@&6*z4@mw%p9f4t9sg9ubupjpeqft087jw(2g&7oq'

# SECURITY WARNING: don't run with debug turned on in production!
try:
    from .local_settings import DEBUG , TEMPLATE_DEBUG
except Exception:
    DEBUG = True
    TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

APPS = ["main",
        ]
try:
    import django_extensions
    APPS += ["django_extensions"]
except:
    pass


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)+ tuple(APPS)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sistematour.urls'

WSGI_APPLICATION = 'sistematour.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATICFILES_DIRS = ( os.path.join (BASE_DIR,'public/static'), )
MEDIA_ROOT = ( os.path.join (BASE_DIR,'public/media') )

STATIC_URL= '/static/'
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.sep.join([os.path.dirname(os.path.dirname(__file__)), 'templates']),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)