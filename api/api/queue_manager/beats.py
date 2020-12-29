from celery.schedules import crontab

from .tasks import app
from ..settings import envs

app.conf.beat_schedule = {
    'get_site_info-every_hour': {
        'task': 'get_price',
        'schedule': envs.TASK_GET_PRICE_SECONDS,  # seconds
    },
}
