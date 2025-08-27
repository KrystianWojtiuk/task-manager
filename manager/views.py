from multiprocessing.pool import worker

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

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
    queryset = Worker.objects.all().select_related("position")


class WorkerDetailView(DetailView):
    model = Worker
    queryset = Worker.objects.select_related("position").prefetch_related("tasks")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        worker = self.object

        context["completed_tasks"] = worker.tasks.filter(is_complete=True)
        context["unfinished_tasks"] = worker.tasks.filter(is_complete=False)

        return context


class ProjectListView(ListView):
    model = Project
    template_name = "manager/project_list.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    queryset = Project.objects.prefetch_related(
        "tasks__assignees",
        "tasks__task_type"
    )


class TaskListView(ListView):
    model = Task
    template_name = "manager/task_list.html"
    context_object_name = "tasks"
    queryset = Task.objects.all().select_related("task_type").select_related("project")

    def get_queryset(self):
        qs = super().get_queryset()
        project_id = self.request.GET.get("project")
        if project_id:
            qs = qs.filter(project_id=project_id)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context


class TaskDetailView(DetailView):
    model = Task
    queryset = Task.objects.select_related("task_type").select_related("project").prefetch_related("assignees")
