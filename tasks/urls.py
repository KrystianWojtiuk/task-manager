from django.urls import path

from tasks.views import index, WorkerListView

app_name = "tasks"

urlpatterns = [
    path("", index, name="index"),
    path("worker-list/", WorkerListView.as_view(), name="worker-list"),
]