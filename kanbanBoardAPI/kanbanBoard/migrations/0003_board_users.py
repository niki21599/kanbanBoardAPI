# Generated by Django 4.0.4 on 2022-05-20 12:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kanbanBoard', '0002_alter_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
