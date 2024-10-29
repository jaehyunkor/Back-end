import os
import django
import random
from celery import Celery
from .models import DailyMission

# Django 환경 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailymission.settings')
django.setup()

# Celery 애플리케이션 초기화
app = Celery('dailymission',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')


@app.task
def change_mission():
    print("Updating mission...")
    try:
        mission_count = DailyMission.objects.count()
        if mission_count > 0:
            # 랜덤으로 하나의 미션 선택
            random_index = random.randint(0, mission_count - 1)
            mission = DailyMission.objects.all()[random_index]

            # 선택된 미션의 is_active를 True로 설정
            mission.is_active = True
            mission.save()

            # 나머지 미션의 is_active를 False로 설정
            DailyMission.objects.exclude(id=mission.id).update(is_active=False)

            print("Mission updated successfully.")
        else:
            print("No mission found to update.")
    except Exception as e:
        print(f"An error occurred: {e}")