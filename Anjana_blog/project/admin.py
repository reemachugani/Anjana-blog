from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }

    class Media:
        js = ('js/tiny_mce/tiny_mce.js', 'js/tiny_mce/textareas.js',)

admin.site.register(Project, ProjectAdmin)