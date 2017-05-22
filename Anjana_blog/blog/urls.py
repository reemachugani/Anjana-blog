from django.conf.urls import url, include, patterns
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.blog_home, name='blog_home'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive_by_month, name="blog_archive_by_month"),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.entry_detail, name="blog_entry_detail"),
    url(r'^tag/(?P<tag>[-\w]+)/$', views.tag_page, name="blog_tag_page"),
]