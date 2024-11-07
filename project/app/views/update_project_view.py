from django.views.generic import UpdateView
from app.models import Project, Tag
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from app.forms import UpdateProjectForm

class UpdateProjectView(UpdateView):
    model = Project
    form_class = UpdateProjectForm
    template_name = 'update.html'
    success_url = reverse_lazy('home')
    
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponseRedirect(self.success_url)
    
    def form_valid(self, form: UpdateProjectForm) -> HttpResponse:
        project = form.save()
        tags = form.cleaned_data.get('tags')
        if tags:
            for tag_title in tags.split(','):
                tag = Tag.objects.create(title=tag_title.strip())
                tag.save()
                project.tags.add(tag)
        messages.info(self.request, "Project create correctly !")
        messages.info(self.request, "Your project has been modified correctly.")
        return super().form_valid(form)
    
    def form_invalid(self, form: UpdateProjectForm) -> HttpResponse:
        messages.warning(self.request, "Your project cannot be modified.")
        return super().form_invalid(form)
    
    