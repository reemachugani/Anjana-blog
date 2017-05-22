from django.shortcuts import render
from .models import Singlepage
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def single_page(request, slug):
    singlepage = get_object_or_404(Singlepage, slug=slug)
    return render_to_response('singlepage/single_page.html', {'singlepage': singlepage}, context_instance=RequestContext(request))
