# mathapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lamp_power, name='lamp_power'),
]
