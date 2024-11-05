from django.utils.deprecation import MiddlewareMixin
from app.forms import CreateProjectForm
from django.http import HttpRequest, HttpResponse

class ManagedFormMiddleware(MiddlewareMixin):
    def process_template_response(self, request: HttpRequest, response: HttpResponse):
        if hasattr(response, 'context_data'):
            response.context_data['action'] = 'create_project'
            response.context_data['create_form'] = CreateProjectForm()
        return response