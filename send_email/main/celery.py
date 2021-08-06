import os
from celery import Celery
from celery.schedules import crontab

# Указываем, где находится наш Django-вский модуль
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_email.settings')

# Создаем объект селери, первый аргумент - это имя текущего модуля
# https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#first-steps
app = Celery('send_email')
# Загружаем настройки из файла Django так, чтобы CELERY читал только те переменные, которые начинаются с CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')
# Автоматически подцепляем наши таски
app.autodiscover_tasks()