# Generated by Django 4.2.2 on 2023-07-23 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizocrats', '0006_result_delete_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizzes',
            name='user',
            field=models.ForeignKey(default='Admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
