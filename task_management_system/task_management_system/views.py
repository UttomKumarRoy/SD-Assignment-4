
from django.shortcuts import render
from task.models import TaskModel

def index(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task/show_tasks.html', {'tasks': tasks})
