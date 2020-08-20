import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_sample.settings')

app = Celery('django_celery_sample', broker='amqp://rabbit:123456@localhost:5672//celery_sample', backend='amqp://')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.update(
#     BROKER_URL='amqp://',
#     CELERY_RESULT_BACKEND='amqp://',
#     CELERY_TASK_SERIALIZER='json',
#     CELERY_ACCEPT_CONTENT=['json'],
#     CELERY_RESULT_SERIALIZER='json',
#     CELERY_TIMEZONE='Asia/Shanghai',
#     CELERY_ENABLE_UTC=True,
#     CELERY_QUEUES=(
#         Queue('receivedata', routing_key='receivedata',
#               consumer_arguments={'x-priority': 100}),
#         Queue('parsedata', routing_key='parsedata',
#               consumer_arguments={'x-priority': 10}),
#         Queue('forwarddata', routing_key='forwarddata',
#               consumer_arguments={'x-priority': 5}),
#     )
# )

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()
