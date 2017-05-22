from django.db import models
from markdown import markdown

class Singlepage(models.Model):
    title = models.CharField(max_length=250, help_text=u'Max 250 characters')
    slug = models.SlugField(help_text=u'Suggested value automatically generated from title. Must be unique.')
    display_word = models.CharField(max_length=50, help_text=u'Max 50 characters. Displayed in the header.')
    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        super(Singlepage, self).save(force_insert, force_update)

    @models.permalink
    def get_absolute_url(self):
        return ('single_page', (), { 'slug': self.slug })