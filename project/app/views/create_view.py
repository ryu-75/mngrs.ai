from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import FormView
from app.forms import CreateProjectForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

class CreateView(FormView):
    template_name = 'create.html'
    form_class = CreateProjectForm
    success_url = 'home'
    
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