from django.urls import path
from . import views

urlpatterns = [
    path('show_tasks/', views.show_tasks, name='show_tasks'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('add_task/', views.add_task, name='add_task'),

]