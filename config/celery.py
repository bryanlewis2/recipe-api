# celery.py (your Celery app configuration)

from celery import Celery
from celery.schedules import crontab

app = Celery('config', broker='redis://redis:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks() 

app.conf.task_routes = {
    'recipe.tasks.*': {'queue': 'default'},
}
app.conf.beat_schedule = {
    'send-daily-like-notifications': {
        'task': 'recipe.tasks.send_daily_like_notifications',
        'schedule': 10.0,  # Change this to your preferred time
    },
}
