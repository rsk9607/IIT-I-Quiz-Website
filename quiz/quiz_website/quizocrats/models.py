from django.db import models

# Create your models here.
class quizzes(models.Model):

    quiz_name=models.CharField(max_length=50)
    topics=models.TextField()

    questions=models.IntegerField()
    time=models.IntegerField()