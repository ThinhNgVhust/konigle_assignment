import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "konigle.settings")
app = Celery("konigle")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule  = {
    'every-5-seconds':{
        'task':'unity.tasks.show',
        'schedule':5

    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print("Request ",self.request)