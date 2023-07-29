from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.
@login_required
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {'tasks': tasks})

@login_required
def create_task(request):
    task = Task(
        title=request.POST['title'],
        description=request.POST['description'],
        )
    task.save()
    return redirect('tasks')

@login_required
def delete_task(request, id):
    deleted_task = Task.objects.get(id=id)
    deleted_task.delete()
    return redirect('tasks')

@login_required
def edit_task(request, id):
    task = Task.objects.get(id=id)
    forms = TaskForm(request.POST or None, instance=task)
    if forms.is_valid() and request.POST:
        forms.save()
        return  redirect('tasks')
    return render(request, 'edit_task.html', {'forms': forms})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            return redirect('tasks')
        else:
            messages.error(request, 'Credenciales inválidas.')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')