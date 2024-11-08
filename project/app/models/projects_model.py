from django.db import models
from django.conf import settings

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    completed = models.BooleanField(default=False) # True if a project is marked finish
    due_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'project'
        
    def __str__(self):
        return self.title
        
class Tag(models.Model):
    projects = models.ManyToManyField(Project, related_name='tags')
    title = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'tag'
        
    def __str__(self):
        return self.title
    