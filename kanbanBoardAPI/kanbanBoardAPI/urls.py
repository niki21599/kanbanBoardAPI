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

from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from kanbanBoard.views import get_board, get_task, post_board, post_task, register, logout_view, get_users_board, get_users_task, add_user_board, remove_user_board,deleteUser, get_user, changeCategory, changeUrgency, changeUser, add_guest_boards
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from kanbanBoard.views import testHtml




urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", obtain_auth_token), 
    path("test/", testHtml), 
    path("board/", get_board), 
    path("task/", get_task), 
    path("board/add/", post_board), 
    path("task/add/", post_task), 
    path("register/", register), 
    path("logout/", logout_view), 
    path("board/add/user/", add_user_board),
    path("task/user/", get_users_task),
    path("board/user/", get_users_board), 
    path("board/remove/user/", remove_user_board),
    path("get/user/", get_user), 
    path("change/category/", changeCategory), 
    path("change/urgency/", changeUrgency), 
    path("change/user/", changeUser),
    path("delete/user/", deleteUser), 
    path("guestBoards/add/", add_guest_boards), 
] + staticfiles_urlpatterns()
