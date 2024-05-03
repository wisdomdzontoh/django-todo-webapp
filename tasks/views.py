from django.shortcuts import render
from .models import Task
# Create your views here.

def home(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'tasks/index.html', context)

def completed(request):
    completed_tasks = Task.objects.filter(completed=True)
    context = {
        'completed_tasks': completed_tasks,
    }
    return render(request, 'tasks/completed.html', context)

def remaining(request):
    remaining_tasks = Task.objects.filter(completed=False)
    context = {
        'remaining_tasks': remaining_tasks,
    }
    return render(request, 'tasks/remaining.html', context)

def add_task(request):
    return render(request, 'tasks/add_task.html')

def delete_task(request):
    return render(request, 'tasks/delete.html')

def task_detail(request):
    return render(request, 'tasks/task_detail.html')