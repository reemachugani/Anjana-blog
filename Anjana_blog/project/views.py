from .models import Project 
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def project_home(request):
    projects = Project.objects.all()
    return render_to_response('project/project_home.html', {'projects': projects}, context_instance=RequestContext(request))

def project_detail_page(request, slug):
    """
    Displays detailed project page
    """
    project = get_object_or_404(Project, slug=slug)
    return render_to_response('singlepage/project_detail_page.html', {'project': project }, context_instance=RequestContext(request))