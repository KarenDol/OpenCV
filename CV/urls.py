from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faceapi/', views.faceapi, name='faceapi'),
    path('save_video/', views.save_video, name='save_video'),
]