from django.urls import path
from django.contrib.auth import views as auth_views

from manager.views import index, WorkerListView, TaskListView, ProjectListView, WorkerDetailView, TaskDetailView, \
    ProjectDetailView, ProjectCreateView, TaskCreateView

app_name = "manager"

urlpatterns = [
    path("", index, name="index"),
    path("login/", auth_views.LoginView.as_view(template_name="manager/login.html"), name="login"),
    path("workers/", WorkerListView.as_view(), name="workers"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("projects/create/", ProjectCreateView.as_view(), name="project-create"),
    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create")
]
