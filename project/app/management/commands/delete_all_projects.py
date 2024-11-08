from django.core.management.base import BaseCommand
from app.models import Project
from typing import Dict, Any
class Command(BaseCommand):
    help = "Delete all project in the Project table"
    
    def handle(self, *args: str, **kwargs: Dict[str, Any]):
        confirmation = input("Are you sure you want to delete all projects? Type 'yes' to confirm: ")
        
        if confirmation.lower() == 'yes':
            deleted_count, _ = Project.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"Successfully deleted {deleted_count} projects."))
        else:
            self.stdout.write(self.style.WARNING("Deletion canceled."))