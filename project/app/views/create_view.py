from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)