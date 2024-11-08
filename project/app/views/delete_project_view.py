from typing import Dict, Any
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from app.models import Project
from app.forms import ProjectForm
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.contrib import messages

class DeleteProjectView(DeleteView):
    model = Project
    success_url = reverse_lazy('home')
    
    def form_valid(self, form: ProjectForm) -> HttpResponse:
        project = self.get_object()
        
        for tag in project.tags.all():
            tag.delete()
        messages.info(self.request, "Your project has been deleted correctly.")
        return super().form_valid(form)
    
    def form_invalid(self, form: ProjectForm) -> HttpResponse:
        messages.warning(self.request, "Your project cannot be delete...")
        return super().form_invalid(form)
        