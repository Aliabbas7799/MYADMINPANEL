from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm






def home(request):
    return render(request, 'admin_panel.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # 👈 This must match your URL name
        else:
            return render(request, 'admin_panel.html', {'error': 'Invalid credentials'})
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'admin_panel.html')



def custom_logout(request):
    logout(request)
    return redirect('custom_login')  # OR redirect('login')


@login_required
def dashboard(request):
    print("Current user:", request.user)
    return render(request, 'dashboard.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})



def add_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User added successfully.")
            return redirect('user_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserForm()
    return render(request, 'add_user.html', {'form': form, 'is_edit': False})

def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully.")
            return redirect('user_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'add_user.html', {'form': form, 'is_edit': True})




def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('user_list')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to a task list page
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.filter(is_deleted=False).order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # 👈 make sure this name matches your URL name
    else:
        form = TaskForm(instance=task)

    return render(request, 'add_task.html', {'form': form, 'title': 'Edit Task', 'task': task})
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_deleted = True
    task.save()
    return redirect('task_list')
@login_required
def report_list(request):
    return render(request, 'report_list.html')

