from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Position(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ('deadline',)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.deadline < timezone.now() + timedelta(days=1):
            raise ValidationError({"deadline": "Deadline must be at least 1 day from now."})


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Urgent', 'Urgent'), ('High', 'High'),
        ('Normal', 'Normal'), ('Low', 'Low')
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
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        ordering = ('deadline',)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.deadline < timezone.now() + timedelta(days=1):
            raise ValidationError({"deadline": "Deadline must be at least 1 day from now."})
