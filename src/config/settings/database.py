import  os
from  django.conf  import  settings

POSTGRES=True

if POSTGRES:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT"),
            # "TIME_ZONE": os.getenv("TIME_ZONE"),
            # "USE_TZ": os.getenv("USE_TZ"),
        }
    }
else:
    DATABASES = {
        "default":{
            "ENGINE": "django.db.backends.sqlite3" ,
            "NAME": settings.BASE_DIR /"db.sqlite3" ,
        }
    }