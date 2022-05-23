"""kanbanBoardAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from kanbanBoard.views import get_board, get_task, post_board, post_task

from kanbanBoard.views import testHtml

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", obtain_auth_token), 
    path("test/", testHtml), 
    path("board/", get_board), 
    path("task/", get_task), 
    path("board/add/", post_board), 
    path("task/add/", post_task), 

]
