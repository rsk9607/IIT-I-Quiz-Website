from django.db import models

# Create your models here.
class quizzes(models.Model):
    Difficulties=[
        ('H','Hard'),
        ('M','Medium'),
        ('E','Easy'),
        ('N','Not mentioned'),
    ]
    quiz_name=models.CharField(max_length=50)
    topics=models.TextField()
    difficulty=models.CharField(max_length=1,choices=Difficulties)
    questions=models.IntegerField()
    time=models.IntegerField()