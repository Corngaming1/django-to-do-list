
from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        Task.objects.create(title=request.POST['title'])
    return redirect('todo_list')

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('todo_list')
python manage.py migrate

@login_required
def your_view(request):
    ...

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'