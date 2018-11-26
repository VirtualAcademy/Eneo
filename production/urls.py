from django.urls import path
from .views import *


urlpatterns = [
    path('chart', chart, name='chart'),
    # path('fuel/management/storage', storage, name='store'),
    # path('dashboard/', profile, name='dashboard'),
    # path('dashboard/<username>', userdashboard, name='userdashboard'),
    # path('', home, name='index'),
]