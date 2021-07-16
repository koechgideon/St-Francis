from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('event/', views.event, name="event"),
    path('about/', views.about, name="about"),
]
