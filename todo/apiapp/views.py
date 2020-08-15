from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    api_list = {
        'List' : '/task-list/',
        'DetailView': '/detail-task/<str:id>',
        'Create': '/create-task/',
        'Update': '/update-task/<str:id>',
        'Delete': '/delete-task/<str:id>'
    }
    return Response(api_list)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    #print(tasks)
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detailView(request,id):
    task = Task.objects.get(id = id)
    serializer = TaskSerializer(task,many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    success = False
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        success = True
    return Response({'success':success})

@api_view(['POST'])
def updateTask(request,id):
    success = False
    task = Task.objects.get(id = id)
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
        success = True
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request,id):
    success = False
    task = Task.objects.get(id = id)
    if task is not None:
        task.delete()
        success = True
    return Response({'Success': success })