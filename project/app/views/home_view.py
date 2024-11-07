from typing import Dict, Any
from django.http.response import HttpResponse as HttpResponse
from django.http.response import HttpResponseNotFound
from django.views.generic import ListView
from app.models import Project, Tag
from django.db.models.query import QuerySet
from app.serializer import TagSerializer

class HomeView(ListView):
    template_name = 'index.html'
    model = Project
    context_object_name = 'projects'
    
    def get_queryset(self) -> QuerySet[Project]:
        sort_by = self.request.GET.get('sort_by')
        project_id = self.kwargs.get('pk')
            
        if project_id:
            try:
                return Project.objects.filter(id=project_id)
            except Project.DoesNotExist:
                return HttpResponseNotFound("Project not found", status=404)
        else:
            if sort_by == 'due_date':
                return Project.objects.filter(due_date__isnull=False).order_by('due_date')
            elif sort_by == 'completed':
                return Project.objects.filter(completed=True).order_by('-completed')
            else:
                return Project.objects.all().order_by('due_date')
        
    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        projects = context['projects']

        # Sérialiser les tags de chaque projet
        for project in projects:
            project.tags_list = TagSerializer(project.tags.all(), many=True).data
        return context