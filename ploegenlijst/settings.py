from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)r2waboda$o)g39!ap!l7dx$numws6k7zi9=m*3e1hbudc!2&r'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*', '127.0.0.1',
'https://kluisjeslijst.up.railway.app/*',]
ALLOWED_ORIGINS = ['http://*', 'https://*',
'https://kluisjeslijst.up.railway.app/*'],
CSRF_TRUSTED_ORIGINS = ['http://*', 'https://*',
'https://kluisjeslijst.up.railway.app/*/',
]
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'viking',
    # 'debug_toolbar',
    'rest_framework',
    'corsheaders',
]
# INTERNAL_IPS = ["127.0.0.1",] #debug toolbar
MIDDLEWARE = [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware', ## tijdens debug 
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",  #29-10-2022
    "whitenoise.middleware.WhiteNoiseMiddleware",  #29-10-22
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ploegenlijst.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[ BASE_DIR / 'mykluisjes/build','templates'
        ],
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

WSGI_APPLICATION = 'ploegenlijst.wsgi.application'
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'viking.sqlite3',
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL='/images/'
STATICFILES_DIRS = [
    BASE_DIR / 'mykluisjes/build/static']

# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/' # new
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
MEDIA_ROOT= BASE_DIR / 'static/images'
# FIXTURE_DIRS = [BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS=True
