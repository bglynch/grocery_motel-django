import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')$wd=*_swxaq62ffokxp*%_ssx4xlh2795y*&s9r(+oxwipblx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['grocery-motel-django-bglynch.c9users.io', 'bglynch-grocerymotel-django.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'checkout',
    'cart',
    'products',
    'crispy_forms',
    'accounts',
    'home',
    'storages',
    'social_django',
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

ROOT_URLCONF = 'grocerymotel.urls'

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
                'django.template.context_processors.media',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'grocerymotel.wsgi.application'


# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Message storage for flash messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Bootstrap version for crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Login redirect location
LOGIN_REDIRECT_URL = 'get_products'
LOGIN_URL = 'login'

# Keys to connect to Stripe
STRIPE_PUBLISHABLE = os.environ.get('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET = os.environ.get('STRIPE_SECRET_KEY')


AUTHENTICATION_BACKENDS = (
'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
'social_core.backends.google.GoogleOpenId',  # for Google authentication
'social_core.backends.google.GoogleOAuth2',  # for Google authentication
'django.contrib.auth.backends.ModelBackend',
)

# Keys to connect to GoogleOAuth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
