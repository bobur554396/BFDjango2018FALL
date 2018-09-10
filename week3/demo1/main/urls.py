from django.urls import path, re_path
from main import views

urlpatterns = [
    path('', views.index),
    path('hello/', views.hello),
    path('time/', views.current_time),
    re_path(r'^time/plus/(\d{1,2})/$', views.hour_ahead),
    path('time/plus/1/', views.current_time),
]