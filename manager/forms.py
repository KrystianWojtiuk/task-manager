from django import forms
from django.utils import timezone
from datetime import timedelta, datetime
from .models import Project, Task


class DeadlineValidationForm(forms.ModelForm):
    """Base form for shared deadline validation and Flatpickr integration."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deadline'].widget.attrs.update({
            "class": "flatpickr form-control",
            "placeholder": "YYYY-MM-DD HH:MM",
            "readonly": True
        })

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if not isinstance(deadline, datetime):
            raise forms.ValidationError("Enter a valid date and time.")
        return deadline

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

    class Meta:
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={
                    "type": "text",
                    "class": "flatpickr form-control",
                    "placeholder": "YYYY-MM-DD HH:MM",
                    "readonly": True
                },
                format="%Y-%m-%d %H:%M"
            ),
        }


class ProjectForm(DeadlineValidationForm):
    class Meta:
        model = Project
        fields = "__all__"


class TaskForm(DeadlineValidationForm):
    class Meta:
        model = Task
        fields = "__all__"
