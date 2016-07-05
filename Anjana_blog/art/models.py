from django.db import models
from markdown import markdown
from tagging.fields import TagField
from tagging.registry import register
import datetime, tagging, os

class Art(models.Model):
    """
    Class defining art work model
    """
    PHOTOGRAPHY = 1
    MODELLING = 2
    SKETCHES = 3
    ART_CHOICES = (
        (PHOTOGRAPHY, 'Photography'),
        (MODELLING, 'Modelling'),
        (SKETCHES, 'Sketches'),
    )

    def get_upload_path_high(instance, filename):
        return os.path.join(instance.art_type, "high", filename)

    def get_upload_path_low(instance, filename):
        return os.path.join(instance.art_type, "low", filename)

    title = models.CharField(max_length=250, help_text=u'Max 250 characters')
    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    art_type = models.IntegerField(choices=ART_CHOICES, default=SKETCHES)
    tags = TagField(help_text=u'Seperate tags with spaces.')
    url = models.URLField('URL', unique=True)
    image_highres = models.ImageField(upload_to=get_upload_path_high)
    image_lowres = models.ImageField(upload_to=get_upload_path_low)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        super(Art, self).save(force_insert, force_update)

    def image_tag(self):
        return markdown('<img src="/%s/%s/%s" width="100" height="100" />' % (self.art_type, "low", self.image_lowres))

register(Art, tag_descriptor_attr='atags')
