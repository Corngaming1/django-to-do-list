from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('todo_project.urls')), 
    path('signup/', SignUpView.as_view(), name='signup'),
    ]
