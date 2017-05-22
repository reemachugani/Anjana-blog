from django.conf.urls import url, include, patterns
from . import views

app_name = 'singlepage'
urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.single_page, name='single_page'),
]