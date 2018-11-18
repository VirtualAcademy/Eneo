from django.urls import path
from .views import *


urlpatterns = [
    path('fuel/management/<int:pk>', FuelDetailsView.as_view(), name='fuel'),
    path('dashboard/', profile, name='dashboard'),
    path('dashboard/<username>', userdashboard, name='userdashboard'),
    path('', home, name='index'),
]