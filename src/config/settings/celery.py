import os
from celery.schedules import crontab
from dotenv import load_dotenv


load_dotenv()

CELERY_TIMEZONE = os.getenv('CELERY_TIMEZONE')
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
CELERY_TASK_SERIALIZER = os.getenv('CELERY_TASK_SERIALIZER')
CELERY_RESULT_SERIALIZER = os.getenv('CELERY_RESULT_SERIALIZER')
CELERY_TASK_TRACK_STARTED = os.getenv('CELERY_TASK_TRACK_STARTED')
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = os.getenv('CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP')



CELERY_BEAT_SCHEDULE = {
    'dumpdata-task': {
        'task': 'apps.base.tasks.dumpdata.dumpdata',
        'schedule': crontab(day_of_month='1,15', hour='3', minute='0'),  # Run on 1st and 15th of each month at 3:00 AM
    },
}
