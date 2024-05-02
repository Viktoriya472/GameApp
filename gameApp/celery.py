import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','gameApp.settings.dev')
app = Celery('gameApp')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_newsletter': {
        'task': 'main.tasks.send_newsletter',
        'schedule': crontab(day_of_week='1', hour='10', minute='0')
    }
}
