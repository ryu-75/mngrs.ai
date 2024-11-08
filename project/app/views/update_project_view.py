from django.views.generic import UpdateView
from app.models import Project, Tag
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from app.forms import UpdateProjectForm
from django.shortcuts import get_object_or_404

class UpdateProjectView(UpdateView):
    model = Project
    form_class = UpdateProjectForm
    template_name = 'update.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form: UpdateProjectForm) -> HttpResponse:
        project = form.save(commit=False)
        project_id = Project.objects.get(id=self.kwargs['pk'])
        
        description = form.cleaned_data.get('description') or project_id.description
        image = form.cleaned_data.get('image') or project_id.image
        due_date = form.cleaned_data.get('due_date') or project_id.due_date
            
        project.description = description
        project.image = image
        project.due_date = due_date
        
        # Update project data
        project.save()
        
        # Processing tags
        tags = form.cleaned_data.get('tags')
        if tags:
            for tag_title in tags.split(','):
                tag = Tag.objects.create(title=tag_title.strip())
                tag.save()
                project.tags.add(tag)
        messages.info(self.request, "Project update correctly!")
        messages.info(self.request, "Your project has been modified correctly.")
        return super().form_valid(form)
    
    def form_invalid(self, form: UpdateProjectForm) -> HttpResponse:
        messages.warning(self.request, "Your project cannot be update...")
        return super().form_invalid(form)
    
    