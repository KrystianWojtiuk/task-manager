from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Position, TaskType, Team, Worker, Project, Task


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ["name", ]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "description", ]
    search_fields = ["name", "description", ]


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", "team", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("position", "team",)}),)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "deadline",
                    "is_complete", "display_teams", ]
    list_filter = ["is_complete", "teams", ]
    search_fields = ["name", "description", ]

    def display_teams(self, obj):
        return ", ".join([team.name for team in obj.teams.all()])
    display_teams.short_description = 'teams'


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    search_fields = ["name", ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "deadline", "is_complete",
                    "priority", "task_type", "display_assignees", "project", ]
    list_filter = ["is_complete", "priority", "task_type", "project", ]
    search_fields = ["name", "description", ]

    def display_assignees(self, obj):
        return ", ".join([str(worker) for worker in obj.assignees.all()])
    display_assignees.short_description = 'assignees'
