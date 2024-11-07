from django.urls import path
import app.views

urlpatterns = [
    path('', app.views.HomeView.as_view(), name='home'),
    path('<int:pk>/', app.views.HomeView.as_view(), name='project'),
    path('create/', app.views.AddProjectView.as_view(), name='create_project'),
    path('tags/', app.views.AddProjectView.as_view(), name='tags'),
    path('update/<int:pk>/', app.views.UpdateProjectView.as_view(), name='update_project'),
    path('delete/<int:pk>/', app.views.DeleteProjectView.as_view(), name='delete_project'),
]
