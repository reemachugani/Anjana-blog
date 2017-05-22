from django.db import models
from markdown import markdown

class Project(models.Model):
    """
    Class defining model for Projects
    """
    title = models.CharField(max_length=250, help_text = u'Maximum 250 characters')
    slug = models.SlugField(help_text=u'Suggested value automatically generated from title. Must be unique.')
    about = models.TextField()
    about_html = models.TextField(editable=False, blank=True)
    excerpt = models.TextField(help_text = u'A short summary of the project.')
    excerpt_html = models.TextField(editable=False, blank=True)
    
    url = models.URLField('URL', unique=True)

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        self.about_html = markdown(self.about)
        self.excerpt_html = markdown(self.excerpt)
        super(Project, self).save(force_insert, force_update)

    @models.permalink
    def get_absolute_url(self):
        return ('project_detail_page', (), { 'slug': self.slug })