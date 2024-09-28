# tasks/urls.py
from django.urls import path
from .views import TaskListCreate, index

urlpatterns = [
    path('', index, name='task-index'),  # Adiciona a rota para o front-end
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
]
