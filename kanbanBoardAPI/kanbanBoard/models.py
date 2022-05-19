

from django.db import models
from datetime import date
from django.conf import settings

# Create your models here.


class Board (models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=500)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)


