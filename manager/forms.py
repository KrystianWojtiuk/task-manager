from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import Project, Task


class DeadlineValidationForm(forms.ModelForm):
    """Base form to validate that deadline is at least 1 day from now if incomplete,
    and render a HTML5 datetime picker."""

    class Meta:
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M"
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.deadline:
            self.initial['deadline'] = self.instance.deadline.strftime("%Y-%m-%dT%H:%M")

    def clean(self):
        cleaned_data = super().clean()
        deadline = cleaned_data.get("deadline")
        is_complete = cleaned_data.get("is_complete", False)

        if deadline and not is_complete:
            if deadline < timezone.now() + timedelta(days=1):
                self.add_error(
                    "deadline",
                    "Deadline must be at least 1 day from now for incomplete tasks/projects."
                )

        return cleaned_data


class ProjectForm(DeadlineValidationForm):
    class Meta:
        model = Project
        fields = "__all__"


class TaskForm(DeadlineValidationForm):
    class Meta:
        model = Task
        fields = "__all__"
