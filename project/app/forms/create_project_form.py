from django import forms
from app.models import Project
from django.core.exceptions import ValidationError

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "image", "due_date"]

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
        self.fields['due_date'].required = False
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        
        if Project.objects.filter(title=title).exists():
            raise ValidationError("This title is already used")
        if title is None:
            raise ValidationError('You should to add a title as minimum')
        return cleaned_data
    
    # def create(self):
    #     cleaned_data = self.cleaned_data
    #     try:
    #         project = Project.objects.create(
    #             title = cleaned_data.get('title'),
    #             description = cleaned_data.get('description'),
    #             image = cleaned_data.get('image'),
    #             completed = cleaned_data.get('completed'),
    #             due_date = cleaned_data.get('due_date')
    #         )
    #         return project
    #     except:
    #         return None