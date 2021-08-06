import os
from celery import Celery
from celery.schedules import crontab

# Указываем, где находится наш Django-вский модуль
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_email.settings')

# Создаем объект селери, первый аргумент - это имя текущего модуля
# https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#first-steps
app = Celery('send_email')
# Загружаем настройки из файла Django так, чтобы CELERY читал только те переменные,
# которые начинаются с CELERY (указывается в namespace)
app.config_from_object('django.conf:settings', namespace='CELERY')
# Автоматически подцепляем наши таски из файла tasks.py
app.autodiscover_tasks()



# 2. Шедулер Celery - настройки интервалов
# https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html
app.conf.beat_schedule = {
    'send-spam-every-1-minutes': {
        'task': 'main.tasks.send_beat_email',
        'schedule': crontab(minute='*/1'),
    },
}