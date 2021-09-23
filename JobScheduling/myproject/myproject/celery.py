
from __future__ import absolute_import, unicode_literals
from datetime import timezone

import os

from celery import Celery

from django.conf import settings  # noqa
# from celery.schedules import crontab
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')



app = Celery('myproject')
app.conf.enable_utc = False
app.conf.update(timezone="Asia/Kolkata")


# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object(settings,namespace="CELERY")
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()

# celery beat settings
app.conf.beat_schedule={
    'send-mail-every-day-at-7':{
        'task':'myapp.tasks.send_mail_func',
        'schedule': crontab(minute=10, day_of_month=23, month_of_year = 9),
        # 'args': # can user this agrs in fun 
    }

}

# # Celery Beat Settings
# app.conf.beat_schedule = {
#     'send-mail-every-day-at-8': {
#         'task': 'send_mail_app.tasks.send_mail_func',
#         'schedule': crontab(hour=0, minute=46, day_of_month=19, month_of_year = 6),
#         #'args': (2,)
#     }
#   
# }

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))