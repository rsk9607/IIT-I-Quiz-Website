from django.urls import path
from . import views

urlpatterns = [
    path('quizocrats/', views.quizocrats, name='quizocrats'),
]