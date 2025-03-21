from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, ''
    'todo/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        Task.objects.create(title=title)
        return redirect("/")

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/")
