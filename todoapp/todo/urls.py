from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('todo/create/', views.todo_create, name='todo_create'),
    path('todo/update/<int:pk>/', views.todo_update, name='todo_update'),
    path('todo/delete/<int:pk>/', views.todo_delete, name='todo_delete'),
]

