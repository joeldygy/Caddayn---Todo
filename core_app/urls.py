from django.urls import path
from core_app import views

urlpatterns = [
    path('todo/list/', views.todo_list),
    path('todo/create/', views.todo_create),
    path('todo/<int:id>/', views.todo_detail),
    path('todo/update/<int:id>/', views.todo_update),
    path('todo/delete/<int:id>/', views.todo_delete),
]
