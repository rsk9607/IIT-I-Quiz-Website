from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('aboutus', views.aboutus, name='about'),
    path('help', views.help, name='help'),
    path('samplequiz', views.samquiz, name='samquiz'),
    path('Answers', views.quizanswers, name='quizanswers'),
    path('logout', views.loggingout, name='logout'),
    path('quiz', views.quiz, name='quizzes'),
    path('create', views.create, name='create'),
    path('c++quiz', views.cppquiz, name='cppquiz'),
    path('pythonquiz', views.pythonquiz, name='pythonquiz'),
    path('htmlquiz', views.htmlquiz, name='htmlquiz'),
    path('javascriptquiz', views.javascriptquiz, name='javascriptquiz'),
    path('cssquiz', views.cssquiz, name='cssquiz'),
    path('aiquiz', views.aiquiz, name='aiquiz'),
    path('mlquiz', views.mlquiz, name='mlquiz'),
    path('djangoquiz', views.djangoquiz, name='djangoquiz'),
    path('adminquiz/<name>', views.adminquiz, name='adminquiz'),
    path('adminquiz/answers/<name>', views.quizans, name='quizans'),
    path('existquiz',views.quizexisting,name='quizzes_existing'),
    path('delete/<name>',views.delete,name='delete'),
]