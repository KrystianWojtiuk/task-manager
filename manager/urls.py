from django.urls import path

from manager.views import index, WorkerListView

app_name = "manager"

urlpatterns = [
    path("", index, name="index"),
    path("worker-list/", WorkerListView.as_view(), name="worker-list"),
]