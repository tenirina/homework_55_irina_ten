from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class ToDoForm(forms.Form):
    text = forms.CharField(max_length=500, required=True, label="Text")
    description = forms.CharField(max_length=1500, required=True, label="Description", widget=widgets.Textarea)
    status = forms.CharField(max_length=500, required=True, label="Status")
    completion_data = forms.CharField(max_length=500, required=False, label="Completion data")

    def clean_text(self):
        text = self.cleaned_data.get("text")
        if text:
            return text
        raise ValidationError('The field is required')
