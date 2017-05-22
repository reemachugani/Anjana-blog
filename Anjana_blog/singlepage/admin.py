from django.contrib import admin
from .models import Singlepage


class SinglepageAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }

    class Media:
        js = ('js/tiny_mce/tiny_mce.js', 'js/tiny_mce/textareas.js',)

admin.site.register(Singlepage, SinglepageAdmin)
