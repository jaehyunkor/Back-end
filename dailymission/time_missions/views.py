# time_missions/views.py

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DailyMission
from .serializers import DailyMissionSerializer

def home(request):
    # 현재 활성화된 미션 조회
    mission = DailyMission.objects.filter(is_active=True).first()
    print(f"{mission}")
    return render(request, 'time_missions/home.html', {'mission': mission})


class ProductListAPI(APIView):
    def get(self, request):
        missions = DailyMission.objects.all()
        serializer = DailyMissionSerializer(missions, many=True)
        return Response(serializer.data)
