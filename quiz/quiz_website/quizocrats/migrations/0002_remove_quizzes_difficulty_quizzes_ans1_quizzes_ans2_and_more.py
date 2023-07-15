# Generated by Django 4.2.2 on 2023-07-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizocrats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizzes',
            name='difficulty',
        ),
        migrations.AddField(
            model_name='quizzes',
            name='ans1',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='ans2',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='ans3',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='ans4',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='ans5',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op1_1',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op1_2',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op1_3',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op1_4',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op2_1',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op2_2',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op2_3',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op2_4',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op3_1',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op3_2',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op3_3',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op3_4',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op4_1',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op4_2',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op4_3',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op4_4',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op5_1',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op5_2',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op5_3',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='op5_4',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='ques1',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='ques2',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='ques3',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='ques4',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='ques5',
            field=models.CharField(max_length=50, null=type),
            preserve_default=type,
        ),
    ]