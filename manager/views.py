from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from manager.models import Worker, Task, Project


@login_required
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


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    template_name = "manager/worker_list.html"
    context_object_name = "workers"
    queryset = Worker.objects.all().select_related("position")


class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker
    queryset = (
        Worker.objects
        .select_related("position")
        .prefetch_related("tasks__task_type")
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        worker = self.object
        all_tasks = list(worker.tasks.all())
        context["completed_tasks"] = [t for t in all_tasks if t.is_complete]
        context["unfinished_tasks"] = [t for t in all_tasks if not t.is_complete]

        return context


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "manager/project_list.html"
    context_object_name = "projects"


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    queryset = Project.objects.prefetch_related(
        "tasks__assignees",
        "tasks__task_type"
    )


class ProjectFormView(LoginRequiredMixin, CreateView, UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("manager:projects")
    template_name = "manager/project_form.html"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        if pk:
            return Project.objects.get(pk=pk)
        return None


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("manager:projects")
    template_name = "manager/project_delete.html"


class TaskListView(LoginRequiredMixin, ListView):
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


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    queryset = Task.objects.select_related("task_type").select_related("project").prefetch_related("assignees")


class TaskFormView(LoginRequiredMixin, CreateView, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("manager:tasks")
    template_name = "manager/task_form.html"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        if pk:
            return Task.objects.get(pk=pk)
        return None


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("manager:tasks")
    template_name = "manager/task_delete.html"
