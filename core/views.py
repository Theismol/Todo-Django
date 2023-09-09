from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import NewTodoForm, SignupForm, LoginForm, EditTodoForm
# Create your views here.


@login_required
def index(request):
    todos = Todo.objects.filter(complete=False).filter(created_by=request.user)
    return render(request, 'core/index.html', {
        'todos': todos,
    })


def new_todo(request):
    if request.method == 'POST':
        form = NewTodoForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('core:index')
    form = NewTodoForm()

    return render(request, 'core/edit.html', {
        'form': form,
        'title': 'Add todo'
    })


def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        form = EditTodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()

            return redirect('core:index')
    form = EditTodoForm(instance=todo)

    return render(request, 'core/edit.html', {
        'form': form,
        'title': 'Edit todo'
    })


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form,
    })

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()

    return redirect('core:index')


def completed_todos(request):
    todos = Todo.objects.filter(complete=True)
    return render(request, 'core/completed_todos.html', {
        'todos': todos,
    })


def logout_view(request):
    logout(request)
    return render(request, 'core/login.html')
