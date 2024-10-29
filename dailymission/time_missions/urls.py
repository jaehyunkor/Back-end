# time_missions/urls.py

from django.urls import path
from .views import home  # home 뷰 임포트

urlpatterns = [
    path('', home, name='home'),  # 홈 뷰로 변경
]
