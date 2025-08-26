from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import Position, TaskType, Worker, Project, Task


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ["name", ]


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("position",)}),)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "deadline",
                    "is_complete"]
    list_filter = ["is_complete"]
    search_fields = ["name", "description", ]


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    search_fields = ["name", ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "deadline", "is_complete",
                    "priority", "task_type", "display_project", "display_assignees", ]
    list_filter = ["is_complete", "priority", "task_type", "project", ]
    search_fields = ["name", "description", ]

    def display_assignees(self, obj):
        return ", ".join([str(worker) for worker in obj.assignees.all()])

    def display_project(self, obj):
        return str(obj.project)
    display_project.short_description = 'project'
