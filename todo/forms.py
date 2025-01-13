from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        # required=False,
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder": "2006-10-25 14:30:59"
            }
        ),
        required=False,
    )

    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "tags",
        )


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
