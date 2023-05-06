from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('services.html', views.services, name="services"),
    path('pricing.html', views.pricing, name="pricing"),
    path ('appointment', appointment.as_view(), name= 'appointment'),
]
