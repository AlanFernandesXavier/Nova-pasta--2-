# todo_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Rota da API
    path('', include('tasks.urls')),      # Rota para o front-end
]
