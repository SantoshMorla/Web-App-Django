from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo

# Create your views here.

def index(request):
    return render(request, 'index.html')

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_app/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo_app/todo_detail.html', {'todo': todo})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        todo = Todo.objects.create(title=title)
        return redirect('todo_detail', pk=todo.pk)
    return render(request, 'todo_app/todo_create.html')

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        completed = request.POST.get('completed') == 'on'
        todo.title = title
        todo.completed = completed
        todo.save()
        return redirect('todo_detail', pk=todo.pk)
    return render(request, 'todo_app/todo_update.html', {'todo': todo})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_app/todo_delete.html', {'todo': todo})