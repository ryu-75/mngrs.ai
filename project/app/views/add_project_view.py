from typing import Any
from django.http import HttpResponse
from django.views.generic import CreateView
from app.forms import ProjectForm
from django.contrib import messages
from app.models import Project, Tag
from django.urls import reverse_lazy
from app.tasks import send_email_task

class AddProjectView(CreateView):
    template_name = 'create.html'
    form_class = ProjectForm
    model = Project
    success_url = reverse_lazy('home')
    
    def form_valid(self, form: ProjectForm) -> HttpResponse:
        project = form.save()
        tags = form.cleaned_data.get('tags')
        if tags:
            for tag_title in tags.split(','):
                tag = Tag.objects.create(title=tag_title.strip())
                tag.save()
                project.tags.add(tag)
        send_email_task()
        messages.info(self.request, "Project create correctly !")
        return super().form_valid(form)
    
    def form_invalid(self, form: ProjectForm) -> HttpResponse:
        messages.warning(self.request, "Your project cannot be create...")
        return super().form_invalid(form)