
from cmath import log
from turtle import color, title
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from .models import Board, Task, Token
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes


def testHtml(request): 
    return render(request, "test.html")


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_board(request):
    user = request.user
    boards = Board.objects.filter(users=user)
    boards_json = serializers.serialize("json", boards)
    
    return HttpResponse(boards_json, content_type='application/json')

# reqiures params board_id
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_task(request):
    board_pk = request.GET["board_id"]
    print(board_pk)
    
    board = Board.objects.get(pk=board_pk)
    tasks = Task.objects.filter(board=board)
    tasks_json = serializers.serialize("json", tasks)

    return HttpResponse(tasks_json, content_type='application/json')

# requires name of Board and the user via TokenAuth
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def post_board(request):
    
    if request.method == "POST":
        name = request.POST.get("name")
        
        board = Board.objects.create(name=name)
        board.users.add(request.user)

        board_json = serializers.serialize("json", [board])
        return HttpResponse(board_json, content_type='application/json')
        

    return

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def post_task(request):
    if request.method == "POST":
        
        title = request.POST.get("title")
        urgency = request.POST.get("urgency")
        category = request.POST.get("category")
        color = request.POST.get("color")
        user_id = request.POST.get("user_id")
        board_id = request.POST.get("board_id")
        description = request.POST.get("description")
        
        user = User.objects.get(pk=user_id)
        board = Board.objects.get(pk=board_id)
        
        task = Task.objects.create(title=title, urgency=urgency, category=category, color=color, user=user, board=board, description=description)
       
        # task = Task.objects.create(**request.POST) # Wenn es nicht klappt, google "Python resolve dictionary in function"

        task_json = serializers.serialize("json", [task])
        return HttpResponse(task_json, content_type='application/json')
        
        
    return

@csrf_exempt
def register(request): 
    if request.method == "POST":  
        first_name=request.POST.get("first_name")
        username=request.POST.get("username")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        password_repeat=request.POST.get("password_repeat")
        email=request.POST.get("email")
            
        
        if password == password_repeat:
            print("create user")
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                token = Token.objects.get(user=user).key
                
                
                return JsonResponse({"token": token}, safe=False)
            except IntegrityError:
                return JsonResponse({"errorMessage": "Username already exists" }, safe=False) 
        else:
            return JsonResponse({"errorMessage": "Passwords don't match" }, safe=False)
         
        
    return 

def logout_view(request):
    
    request.user.auth_token.delete() 
    logout(request)
    return Response({"success": _("Successfully logged out.")},
                    status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_users_board(request):
    board_id = request.GET.get("board_id") 
    
    board = Board.objects.get(pk=board_id)
    usernames_added = board.users.all().values("username")
    not_added_users = User.objects.filter(~Q(username__in=usernames_added))
    not_added_users_json = serializers.serialize("json", not_added_users)

    return HttpResponse(not_added_users_json,  content_type='application/json')

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_users_task(request):
    board_id = request.GET.get("board_id") 
    board = Board.objects.get(pk=board_id)
    users = board.users.all()
    users_json = serializers.serialize("json", users)
    return HttpResponse(users_json,  content_type='application/json')


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def add_user_board(request):
    if request.method == "POST":
        user_ids = request.POST.get("user_ids")
        board_id = request.POST.get("board_id")
        print("user Ids", user_ids)
        print("board_id", board_id)
        
        user_ids = list(user_ids.split(","))        
        board = Board.objects.get(pk=board_id)
        
        for user_id in user_ids: 
            board.users.add(User.objects.get(pk=user_id))
        board_json = serializers.serialize("json", [board])
        return HttpResponse(board_json, content_type='application/json')
    

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def remove_user_board(request):
    if request.method == "POST":
        user_ids = request.POST.get("user_ids")
        board_id = request.POST.get("board_id")
        user_ids = list(user_ids.split(","))
        board = Board.objects.get(pk= board_id)
        
        print(user_ids)
        for user_id in user_ids: 
            board.users.remove(User.objects.get(pk=user_id))
        board_json = serializers.serialize("json", [board])
        return HttpResponse(board_json, content_type='application/json')        

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_user(request): 
    user_id = request.GET.get("user_id")
    
    user = User.objects.get(pk=user_id)
    user = [user]
    user_json = serializers.serialize("json", user)
    
    return HttpResponse(user_json,  content_type='application/json')

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def changeCategory(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        newCategory = request.POST.get("newCategory")
        task = Task.objects.get(pk=task_id)
        task.category = newCategory
        task.save()
        task_json = serializers.serialize("json", [task])
        return HttpResponse(task_json, content_type='application/json')

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def changeUrgency(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        newUrgency = request.POST.get("newUrgency")
        task = Task.objects.get(pk=task_id)
        task.urgency = newUrgency
        task.save()
        task_json = serializers.serialize("json", [task])
        return HttpResponse(task_json, content_type='application/json')

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def changeUser(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        newUserId = request.POST.get("newUser")
        newUser = User.objects.get(pk=newUserId)
        task = Task.objects.get(pk=task_id)
        task.user = newUser
        task.save()
        
        task_json = serializers.serialize("json", [task])
        return HttpResponse(task_json, content_type='application/json')


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def deleteUser(request): 
    if request.method == "POST":
        task_id = request.POST.get("task_id") 
        task = Task.objects.filter(pk=task_id)
        task.delete()
        task_json = serializers.serialize("json", [task])
        return HttpResponse(task_json, content_type='application/json') 

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def add_guest_boards(request):
    
    if request.method == "POST":
        user =request.user
       
        user1 = User.objects.get(pk=54)
        user2 = User.objects.get(pk=55)
        user3 = User.objects.get(pk=56)
        # == Musk, Seehofer, Hamilton, Will Smith
        
        board1 = Board.objects.create(name="Chat App")
        board1.users.add(request.user)
        board1.users.add(user1)
        board1.users.add(user2)
        board1.users.add(user3)
        task = Task.objects.create(title="coding the Backend", urgency="Dringend", category="In progress", color="white", user=user, board=board1, description="Designing the ERM Model for the Database. Realising with Django framework")
        task = Task.objects.create(title="designing the App", urgency="Dringend", category="Testing", color="white", user=user, board=board1, description="Creating the UX Design of the whole App ")
        task = Task.objects.create(title="testing", urgency="Dringend", category="To do", color="white", user=user, board=board1, description="Testing the App with jest")

        board2 = Board.objects.create(name="CRM App")
        board2.users.add(request.user)
        board2.users.add(user1)
        board2.users.add(user2)
        board2.users.add(user3)
        task = Task.objects.create(title="Erstellen der Website", urgency="Dringend", category="Done", color="white", user=user, board=board2, description="Coden des gesamten CRM Projekt anhand des Designs")
        task = Task.objects.create(title="Hosting der Website", urgency="Dringend", category="In progress", color="white", user=user, board=board2, description="Hosting des CRMs ")

        board3 = Board.objects.create(name="Notizen App")
        board3.users.add(request.user)
        board3.users.add(user1)
        board3.users.add(user2)
        board3.users.add(user3)
        task = Task.objects.create(title="Zielgruppe?", urgency="Dringend", category="To do", color="white", user=user, board=board3, description="Für wen esrtellen wir das Produkt?")


        board_json = serializers.serialize("json", [board1])
        return HttpResponse(board_json, content_type='application/json')
        

    return