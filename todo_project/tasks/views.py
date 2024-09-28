# tasks/views.py
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer# tasks/views.py
from django.shortcuts import render





class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
def index(request):
    return render(request, 'tasks/index.html')
