# time_missions/apps.py
from django.apps import AppConfig

class TimeMissionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'time_missions'

    def ready(self):
        # 데이터베이스가 초기화된 후에 쿼리를 실행하도록 설정
        pass

