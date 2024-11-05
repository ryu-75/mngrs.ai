from typing import Any
from django.http import HttpRequest, HttpResponseRedirect
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from app.forms import CreateProjectForm
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateProjectForm()
        return context
    
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)