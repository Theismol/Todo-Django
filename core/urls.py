from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('new', views.new_todo, name='new_todo'),
    path('logout',views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('completed_todos/', views.completed_todos, name='completed_todos'),
    path('signup/',views.sign_up, name='sign_up'),
    path('<int:pk>/', views.edit_todo, name='edit_todo'),
    path('<int:pk>/delete', views.delete_todo, name='delete_todo'),
    path('', views.index, name='index'),
]