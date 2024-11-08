from django import forms
from app.models import Project
from django.core.exceptions import ValidationError

class UpdateProjectForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tags (separated by commas)',
        })
    )
    class Meta:
        model = Project
        fields = ["title", "description", "image", "due_date", "completed", "tags"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={
            'required': True,
            'class': 'form-control',
            'placeholder': 'Project title'
        })
        self.fields['description'].widget = forms.TextInput(attrs={
            'required': False,
            'class': 'form-control',
            'placeholder': 'Project description'
        })
        self.fields['image'].required = False
        self.fields['due_date'].widget = forms.DateInput(attrs={
            'required': False,
            'class': 'form-control',
            'placeholder': 'Due date',
            'type': 'date',
            'id': 'startDate'
        })    
        self.fields['completed'].widget = forms.Select(choices=[(True, 'Yes'), (False, 'No')], attrs={
            'default': False,
            'class': 'form-control'
        })