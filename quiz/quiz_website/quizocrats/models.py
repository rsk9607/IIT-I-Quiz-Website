from django.db import models

# Create your models here.
class quizzes(models.Model):

    quiz_name=models.CharField(max_length=50)
    topics=models.TextField()
    questions=models.IntegerField()
    time=models.IntegerField()
    ques1=models.CharField()
    ans1=models.CharField()
    op1_1=models.CharField()
    op1_2=models.CharField()
    op1_3=models.CharField()
    op1_4=models.CharField()
    ques2=models.CharField()
    ans2=models.CharField()
    op2_1=models.CharField()
    op2_2=models.CharField()
    op2_3=models.CharField()
    op2_4=models.CharField()
    ques3=models.CharField()
    ans3=models.CharField()
    op3_1=models.CharField()
    op3_2=models.CharField()
    op3_3=models.CharField()
    op3_4=models.CharField()
    ques4=models.CharField()
    ans4=models.CharField()
    op4_1=models.CharField()
    op4_2=models.CharField()
    op4_3=models.CharField()
    op4_4=models.CharField()
    ques5=models.CharField()
    ans5=models.CharField()
    op5_1=models.CharField()
    op5_2=models.CharField()
    op5_3=models.CharField()
    op5_4=models.CharField()
    