from django.urls import path
from main import views

urlpatterns = [
    path('class/', views.HomeView.as_view()),
    path('function/', views.home),
    path('about/', views.AboutView.as_view(template_name='about.html')),
    path('contact/', views.ContactView.as_view(template_name='about.html')),
]
