from django.db import models
from category.models import TaskCategory

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.taskTitle
