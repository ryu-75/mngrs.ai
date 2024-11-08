from django.contrib import admin
from .models import Project, Tag
from django.utils.translation import gettext_lazy as _

# Personnalize filter: Sort by 'completed' and 'due_date'
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'due_date')   # Column to display
    search_fields = ('title', 'description')            # Field to search in
    list_filter = ('completed', 'due_date')             # Add filter by 'completed' and 'due_date'
    ordering = ('due_date',)                            # Sort projects by 'due_date' (most recent)
    date_hierarchy = 'due_date'                         # Add a date hierarchy filter based on 'due_date' 
    
    actions = ['mark_completed', 'mark_uncompleted']                        
    
    def mark_completed(self, request, queryset):
        """Mark projects as completed"""
        updated = queryset.update(completed=True)
        self.message_user(request, f"{updated} projects marked as completed.")
    mark_completed.short_description = _("Mark selected projects as completed")

    def mark_uncompleted(self, request, queryset):
        """Mark projects as uncompleted"""
        updated = queryset.update(completed=False)
        self.message_user(request, f"{updated} projects marked as uncompleted.")
    mark_uncompleted.short_description = _("Mark selected projects as uncompleted")

    def formatted_due_date(self, obj):
        """Formatted due date"""
        return obj.due_date.strftime('%d/%m/%Y')
    formatted_due_date.admin_order_field = 'due_date'    # Sort by 'due_date' in admin interface
    formatted_due_date.short_description = _("Due date")
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)                           # Display tag name
    search_fields = ('title',)                          # Field to search by tag title

# Saved admin
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)