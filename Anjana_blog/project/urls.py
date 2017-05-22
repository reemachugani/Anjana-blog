from django.conf.urls import url, include, patterns
from . import views

app_name = 'project'
urlpatterns = [
    url(r'^$', views.project_home, name='project_home'),
    url(r'^(?P<slug>[-\w]+)/$', views.project_detail_page, name='project_detail_page'),
]