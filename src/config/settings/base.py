import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY=os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split()

INTERNAL_IPS = os.getenv("INTERNAL_IPS").split(",")
CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL_ORIGINS") == "True"


# Application definition
INSTALLED_APPS = [
    "jazzmin" ,  # which is used to add the admin panel # pip install jazzmin
    # "debug_toolbar" ,  # which is used to debug the application # pip install django-debug-toolbar
    "modeltranslation" ,  # which is used to translate the models # pip install django-modeltranslation

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "corsheaders" , # which is used to allow given host to access the resources # pip install django-cors-headers
    "rest_framework" , # which is used to create the restful api # pip install djangorestframework
    "drf_yasg" , # which is used to create the api documentation # pip install drf-yasg

    'apps.amocrm.apps.AmocrmConfig',
    'apps.chatbot.apps.ChatbotConfig',
    'apps.products.apps.ProductsConfig',
    'apps.vacancy.apps.VacancyConfig',
    'apps.web.apps.WebConfig',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    'corsheaders.middleware.CorsMiddleware', # added

    'django.middleware.locale.LocaleMiddleware' , # added
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'debug_toolbar.middleware.DebugToolbarMiddleware', # added
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_HR_USER = os.getenv("EMAIL_HR_USER")
WSGI_APPLICATION = "config.wsgi.application"

TIME_ZONE=os.getenv("TIME_ZONE")
USE_I18N=os.getenv("USE_I18N") # which is used to enable the internationalization
USE_TZ=os.getenv("USE_TZ") # which is used to enable the timezone

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', '').split(',')

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]