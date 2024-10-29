from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab  # crontab을 import 합니다.

# Django 설정 모듈 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailymission.settings')

# Celery 애플리케이션 초기화
app = Celery('dailymission',
             broker='redis://localhost:6379/0',  # Redis 브로커
             backend='redis://localhost:6379/0')  # Redis 백엔드

# Django의 설정 파일에서 Celery 설정 로드
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# 주기적 작업 설정
app.conf.beat_schedule = {
    'change-mission-every-1-minute': {
        'task': 'time_missions.tasks.change_mission',  # 실행할 작업 경로
        'schedule': crontab(minute='*/1'),  # 매 1분마다 실행
    },
}

# Celery 애플리케이션을 초기화합니다.
if __name__ == '__main__':
    app.start()

if os.name == 'nt':  # 윈도우에서만 적용
    app.conf.worker_pool = 'solo'