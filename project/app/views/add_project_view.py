from typing import Any
from django.http import HttpResponse
from django.views.generic import CreateView
from app.forms import CreateProjectForm
from django.contrib import messages
from app.models import Project

class AddProjectView(CreateView):
    template_name = 'create.html'
    form_class = CreateProjectForm
    model = Project
    success_url = '/'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['action'] = 'create_project'
        return context
    
    def form_valid(self, form: CreateProjectForm) -> HttpResponse:
        form.save()
        messages.info(self.request, "Project create correctly !")
        return super().form_valid(form)
    
    def form_invalid(self, form: CreateProjectForm) -> HttpResponse:
        messages.warning(self.request, "Your project cannot be create...")
        return super().form_invalid(form)