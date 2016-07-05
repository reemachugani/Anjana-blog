from django.contrib import admin
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
    list_display = ('title', 'pub_date', 'status')
    list_filter = ('status',)

    class Media:
        js = ('js/tiny_mce/tiny_mce.js', 'js/tiny_mce/textareas.js',)

admin.site.register(Entry, EntryAdmin)
