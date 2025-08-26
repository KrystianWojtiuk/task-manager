from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from manager.models import Worker, Task, Project


def index(request):
    num_workers = Worker.objects.count()
    num_projects = Project.objects.count()
    num_tasks = Task.objects.count()
    context = {
        "num_workers": num_workers,
        "num_projects": num_projects,
        "num_tasks": num_tasks,
    }
    return render(request, "manager/index.html", context=context)


class WorkerListView(ListView):
    model = Worker
    template_name = "manager/worker_list.html"
    context_object_name = "workers"


class ProjectsListView(ListView):
    model = Project
    template_name = "manager/project_list.html"
    context_object_name = "projects"


class TaskListView(ListView):
    model = Task
    template_name = "manager/task_list.html"
    context_object_name = "manager"
