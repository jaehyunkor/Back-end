# dailymission/celery.py

import os
from celery import Celery

# Django의 기본 설정 모듈을 설정합니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailymission.settings')

app = Celery('dailymission')

# Django 설정에서 Celery 설정을 로드합니다.
app.config_from_object('django.conf:settings', namespace='CELERY')

# 모든 task 모듈을 자동으로 발견합니다.
app.autodiscover_tasks()
