from dataclasses import field
from re import template
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Task

# Create your views here.
class CreateTask(CreateView):
    model = Task
    fields = ['task_name','task_description']
    template_name = 'Task/create_task.html'
    success_url = '/task/view/'