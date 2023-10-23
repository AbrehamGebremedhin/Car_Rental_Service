import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Car_rental_service.settings')

app = Celery('rental')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
