import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_task_project.settings')

app = Celery('celery_task_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
