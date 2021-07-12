from __future__ import absolute_import

import logging
import os

from celery import Celery
from django.conf import settings
from .settings import ASYNC_TASK_TIME_INTERVAL, VIDEO_TAG

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube.settings')
app = Celery('youtube')
app.conf["accept_content"] = ['json']
app.conf["result_serializer"] = 'json'
app.conf["task_serializer"] = 'json'

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'print-message-every-ten-seconds': {
        'task': 'tasks.fetch_youtube_videos',
        'schedule': ASYNC_TASK_TIME_INTERVAL,
        'args': (VIDEO_TAG,)
    },
}


