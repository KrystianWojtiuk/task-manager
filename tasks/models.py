from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100)


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Worker(AbstractUser):
    position = models.ForeignKey(Team, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    teams = models.ManyToManyField(Team, related_name='projects')


class TaskType(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Urgent', 'High'),
        ('Normal', 'Low'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Normal'
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.PROTECT)
    assignees = models.ManyToManyField(Worker, related_name='tasks', blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

