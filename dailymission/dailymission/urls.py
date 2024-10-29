"""
URL configuration for dailymission project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# dailymission/urls.py

from django.contrib import admin
from django.urls import path, include  # include 추가
from time_missions.views import home  # home 뷰 가져오기
from time_missions.views import ProductListAPI

urlpatterns = [
    path('', home, name='home'),  # 홈 페이지 URL 설정
    path('time_missions/', include('time_missions.urls')),  # time_missions 앱의 URL 포함
    path('admin/', admin.site.urls),  # admin 페이지 URL 설정
    path('api/mission/', ProductListAPI.as_view(), name='ProductListAPI'),  # as_view() 추가
]

