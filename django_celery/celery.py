import os

from celery import Celery
from django.conf import settings
from django.utils import timezone
# set the default Django settings module for the 'celery' program.
from kombu import Queue, Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_sample.settings')

app = Celery('django_celery_sample', broker='amqp://rabbit:123456@localhost:5672//celery_sample', backend='amqp://')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.config_from_object("celeryconfig")  # 指定配置文件

default_exchange = Exchange('default', type='direct')

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=settings.CELERY_TASK_RESULT_EXPIRES,
    CELERY_IGNORE_RESULT=settings.CELERY_IGNORE_RESULT,
    CELERYD_MAX_TASKS_PER_CHILD=settings.CELERYD_MAX_TASKS_PER_CHILD,
    CELERY_TASK_SERIALIZER=settings.CELERY_TASK_SERIALIZER,
    # CELERY_DEFAULT_QUEUE='receivedata_queue',

    CELERY_QUEUES=(
        Queue('receivedata_queue', routing_key='receivedata_key',
              consumer_arguments={'x-priority': 100}),
        Queue('parsedata_queue', default_exchange, routing_key='parsedata_key',
              consumer_arguments={'x-priority': 10}),
        Queue('forwarddata_queue', default_exchange, routing_key='forwarddata_key',
              consumer_arguments={'x-priority': 5}),
    ),

    CELERY_ROUTES={
        'django_celery.tasks.receivedata': {'queue': 'receivedata_queue', 'routing_key': 'receivedata_key'},
        'django_celery.tasks.parsedata': {'queue': 'parsedata_queue', 'routing_key': 'parsedata_key'},
        'django_celery.tasks.forwarddata': {'queue': 'forwarddata_queue', 'routing_key': 'forwarddata_key'},
    },

)

app.now = timezone.now
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()
