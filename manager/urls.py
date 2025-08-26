from django.urls import path

from manager.views import index, WorkerListView, TaskListView, ProjectListView

app_name = "manager"

urlpatterns = [
    path("", index, name="index"),
    path("worker-list/", WorkerListView.as_view(), name="worker-list"),
    path("project-list/", ProjectListView.as_view(), name="project-list"),
    path("task-list/", TaskListView.as_view(), name="task-list"),
]