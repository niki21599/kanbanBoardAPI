
from cmath import log
from turtle import color, title
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from .models import Board, Task, Token
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def user_login(request): 
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user: 
        login(request, user)
        token = Token.objects.get(User=user)
        print(token)
        return HttpResponse("You are authenticated")
    else:
        return HttpResponse("Invalid Data")



def testHtml(request): 
    return render(request, "test.html")


#requires TokenAuth header mit Token
def get_board(request):
    

    # Somehow get the User via TokenAuthentication
    user = User.objects.get(pk=1)
    print(user)
    boards = Board.objects.filter(users=user)
    boards_json = serializers.serialize("json", boards)
    # print(boards)


    return HttpResponse(boards_json, content_type='application/json')

# reqiures params board_id
def get_task(request):
    board_pk = request.GET["board_id"]
    print(board_pk)
    # Get the Board via primaryKey
    board = Board.objects.get(pk=board_pk)
    tasks = Task.objects.filter(board=board)
    tasks_json = serializers.serialize("json", tasks)

    return HttpResponse(tasks_json, content_type='application/json')

# requires name of Board and the user via TokenAuth
@csrf_exempt
def post_board(request):
    user = User.objects.get(pk=1)
    
    if request.method == "POST":
        name = request.POST.get("name")
        print("hallo")
        print(request.POST.get("title"))

        # Schwierigkeiten mit users wg. ManyToManyRelationship
        # Man kann nicht einfach user übergeben

        #board = Board.objects.create(name=name, users=)
        #board_json = serializers.serialize("json", board)
        #return HttpResponse(board_json, content_type='application/json')

    return

@csrf_exempt
def post_task(request):
    if request.method == "POST":
        pass
        #request.POS

        #title = request.POST.get("title")
        title = request.POST.get("title")
        print(title)
        #urgency = request.POST.get("urgency", "dringend")
        #category = request.POST.get("category", "testing")
        #color = request.POST.get("color", "yellow")
        #user_id = request.POST.get("user_id", 1)
        #board_id = request.POST.get("board_id", 1)
        
        #user = User.objects.get(pk=user_id)
        #board = Board.objects.get(pk=board_id)
       
        #task = Task.objects.create(title=title, urgency=urgency, category=category, color=color, user=user, board=board)
        #task_json = serializers.serialize("json", [task])
        return JsonResponse({}, safe=False)
        
    return

def register(request): 
    return
def logout(request): 
    return
def logout(request): 
    return

