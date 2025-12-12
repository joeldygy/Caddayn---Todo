from django.urls import path
from core_app.controller import TodoController

urlpatterns = [
    path('', TodoController.list, name='todo_list'),
    path('create/', TodoController.create, name='todo_create'),
    path('<int:id>/', TodoController.detail, name='todo_detail'),
    path('<int:id>/update/', TodoController.update, name='todo_update'),
    path('<int:id>/delete/', TodoController.delete, name='todo_delete'),
]
