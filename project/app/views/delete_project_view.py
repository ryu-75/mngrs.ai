from typing import Dict, Any
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from app.models import Project
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.contrib import messages

class DeleteProjectView(DeleteView):
    model = Project
    success_url = reverse_lazy('home')
    
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponseRedirect(self.success_url)
    
    def delete(self, request: HttpRequest, *args: tuple, **kwargs: Dict[str, Any]) -> HttpResponse:
        project = self.get_object()
        
        for tag in project.tags.all():
            tag.delete()
        messages.info(self.request, "Your project has been deleted correctly.")
        return super().delete(request, *args, **kwargs)