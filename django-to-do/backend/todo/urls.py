from django.urls import path
from . import views
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

urlpatterns = [
    

    path('', views.homepage, name='homepage'),  # Show homepage first
    path('tasks/', views.home, name='task-list'),    # Show task list at /tasks/
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
     path('guest-login/', views.guest_login, name='guest-login'),
]

