

from django.db import models
from datetime import date
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class Board (models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=500)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    #User can have more than one Board
    #users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    # Siehe hier many-to-many relationship https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_many/
    

class Task (models.Model): 
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    color = models.CharField(max_length=500)
    urgency = models.CharField(max_length=500)
    color = models.CharField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created: 
        Token.objects.create(user=instance)