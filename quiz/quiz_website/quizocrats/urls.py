from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('aboutus', views.aboutus, name='about'),
    path('help', views.help, name='help'),

]