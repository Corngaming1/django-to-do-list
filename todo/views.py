from django.shortcuts import render, redirect
from .models import Task

def homepage(request):
    return render(request, 'todo/homepage.html')  # Uses homepage.html

def index(request):
    return render(request, 'todo/index.html')  # Your task list page


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

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.due_date = request.POST.get('due_date')
        task.category = request.POST.get('category')
        task.save()
        return redirect('home')  # or your homepage route name

    return render(request, 'todo/edit_task.html', {'task': task})
