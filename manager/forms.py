from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import Project, Task


class DeadlineValidationForm(forms.ModelForm):
    """Base form for deadline validation logic."""

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        is_complete = self.cleaned_data.get("is_complete", False)

        if not is_complete and deadline < timezone.now() + timedelta(days=1):
            raise forms.ValidationError("Deadline must be at least 1 day from now.")

        return deadline


class ProjectForm(DeadlineValidationForm):
    class Meta:
        model = Project
        fields = "__all__"


class TaskForm(DeadlineValidationForm):
    class Meta:
        model = Task
        fields = "__all__"
