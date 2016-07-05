from django.contrib import admin
from .models import Art


class ArtAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'art_type')
    list_filter = ('art_type',)
    fields = ( 'image_tag', )
    readonly_fields = ('image_tag', )

    class Media:
        js = ('js/tiny_mce/tiny_mce.js', 'js/tiny_mce/textareas.js',)

admin.site.register(Art, ArtAdmin)


