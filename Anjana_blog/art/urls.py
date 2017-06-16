from django.conf.urls import url, include, patterns
from . import views

app_name = 'art'
urlpatterns = [
    url(r'^$', views.art_home, name='art_home'),
    url(r'^(?P<category_name>[-\w]+)/$', views.art_by_category, name='art_by_category'),
    url(r'^(?P<slug>[-\w]+)/$', views.art_detail_page, name='art_detail_page'),
]