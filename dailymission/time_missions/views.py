# time_missions/views.py

from django.shortcuts import render
from .models import DailyMission

def home(request):
    # 현재 활성화된 미션 조회
    mission = DailyMission.objects.filter(is_active=True).first()
    print(f"{mission}")
    return render(request, 'time_missions/home.html', {'mission': mission})
