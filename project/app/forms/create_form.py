from django import forms
from app.models import Project

class CreateForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255, widget=forms.CharField(attrs={
        'required': True,
        'class': 'form-control',
        'placeholder': 'Project title'
    }))
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
        'required': False,
        'class': 'form-control',
        'placeholder': 'Project description'
    }))
    image = forms.ImageField(label='Picture', required=False)
    due_date = forms.DateTimeField(required=False)
    
    class Meta:
        model = Project
        fields = ["title", "description", "image", "due_date"]
    