from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User  # Import User model
from django.http import HttpResponseRedirect  # Import HttpResponseRedirect
from django.urls import reverse

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    




@login_required(login_url='/accounts/login/')

def homepage(request):
    if request.user.is_authenticated:
        # This logic is for authenticated users
        return render(request, 'todo/homepage.html')  # Display homepage for authenticated users
    else:
        # This logic is for guest users
        return render(request, 'todo/homepage.html')  # Display homepage for guest users

def guest_login(request):
    # If the user is already logged in, redirect to the task list
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('task-list'))

    # If guest user doesn't exist, create one
    guest_user, created = User.objects.get_or_create(username="guest")
    
    # Log the guest user in
    login(request, guest_user)
    
    # Redirect to task list or homepage
    return HttpResponseRedirect(reverse('homepage'))  # Make sure this points to your task list or homepage

def index(request):
    return render(request, 'todo/index.html')  # Your task list page

def home(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

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

