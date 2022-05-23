from kanbanBoard.models import Task
from django.contrib import admin
from kanbanBoard.models import Board

# Register your models here.


admin.site.register(Board)
admin.site.register(Task)