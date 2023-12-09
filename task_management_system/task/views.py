from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task/show_tasks.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('show_tasks')

    return render(request, 'task/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('show_tasks')

    return render(request, 'task/delete_task.html', {'task': task})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()

    return render(request, 'task/add_task.html', {'form': form})