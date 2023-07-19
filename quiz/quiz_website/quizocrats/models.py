from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class quizzes(models.Model):
    quiz_name=models.CharField(max_length=50)
    topics=models.TextField()
    questions=models.IntegerField()
    time=models.IntegerField()

class questionare(models.Model):
    quiz=models.ForeignKey(quizzes,on_delete=models.CASCADE)
    question=models.TextField()
    correct_opt=models.TextField()
    opt1=models.TextField()  
    opt2=models.TextField()  
    opt3=models.TextField()  
    opt4=models.TextField()  

class result(models.Model):
    quiz=models.ForeignKey(quizzes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    score=models.IntegerField()
    date=models.DateTimeField()
    
