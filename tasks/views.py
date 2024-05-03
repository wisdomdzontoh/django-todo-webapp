from django.shortcuts import redirect, render
from .models import Task
# Create your views here.

def home(request):
    tasks = Task.objects.all().order_by('-due_date')
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
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        due_time = request.POST.get("due_time")
        completed = False
        
        if title != "" and due_date != "" and due_time !="":
            task = Task(
                title=title, 
                description=description,  
                due_date=due_date,
                due_time=due_time,
                completed=completed,
            )
            task.save()
            return redirect('home')
    else:
        return render(request, 'tasks/add_task.html')
    return render(request, 'tasks/add_task.html')
    

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {
        'task': task,
    }
    return render(request, 'tasks/delete.html', context)

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {
        'task': task,
    }
    return render(request, 'tasks/task_detail.html', context)

def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect('home')
    
def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.delete()
        return redirect('home')