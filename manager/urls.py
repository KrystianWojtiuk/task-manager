from django.urls import path

from manager.views import index, WorkerListView, TaskListView, ProjectListView, WorkerDetailView, TaskDetailView, \
    ProjectDetailView

app_name = "manager"

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="workers"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
]
