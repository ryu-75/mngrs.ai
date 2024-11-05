from django.urls import path
import app.views

urlpatterns = [
    path('', app.views.HomeView.as_view(), name='home'),
    path('create/', app.views.AddProjectView.as_view(), name='create_project'),
]
