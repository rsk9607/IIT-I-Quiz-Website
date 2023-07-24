from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('aboutus', views.aboutus, name='about'),
    path('help', views.help, name='help'),
    path('logout', views.loggingout, name='logout'),
    path('quiz', views.quiz, name='quizzes'),
    path('create', views.create, name='create'),
    path('adminquiz/<name>', views.adminquiz, name='adminquiz'),
    path('answers/<name>', views.quizans, name='quizans'),
    path('existquiz',views.quizexisting,name='quizzes_existing'),
    path('delete/<name>',views.delete,name='delete'),
    path('instr/<name>',views.instr,name='instr'),
    path('progress',views.progress,name='progress'),
]