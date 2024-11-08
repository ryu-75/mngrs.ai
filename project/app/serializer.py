from rest_framework import serializers
from app.models import Project, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']  

class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True) 

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'completed', 'due_date', 'tags'] 
