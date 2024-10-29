# time_missions/serializers.py

from rest_framework import serializers
from .models import DailyMission

class DailyMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMission
        fields = ['title', 'description', 'is_active']  # 모델의 필드 이름을 맞추어 사용하세요.
