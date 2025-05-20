from django.http import HttpResponse
from django.shortcuts import render

from tasks.models import Worker, Task, Project


def index(request):
    num_workers = Worker.objects.count()
    num_projects = Project.objects.count()
    num_tasks = Task.objects.count()
    context = {
        "num_workers": num_workers,
        "num_projects": num_projects,
        "num_tasks": num_tasks,
    }
    return render(request, "tasks/index.html", context=context)