from art.models import Art, Art_Category
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def art_home(request):
    arts = Art.objects.all()
    categories = Art_Category.objects.all()
    return render_to_response('art/art_home.html', {'arts': arts, 'categories': categories}, context_instance=RequestContext(request))

def art_by_category(request, category_name):
    all_arts = Art.objects.all()
    category_arts = all_arts.filter(art_type__category = category_name)
    # if not category_arts:
    #     return redirect('art.views.art_home')
    categories = Art_Category.objects.all()
    return render_to_response('art/art_home.html', {'arts': category_arts, 'categories': categories}, context_instance=RequestContext(request))

def art_detail_page(request, slug):
    """
    Displays detailed project page
    """
    art = get_object_or_404(Art, slug=slug)
    categories = Art_Category.objects.all()
    return render_to_response('singlepage/art_detail_page.html', {'art': art, 'categories': categories}, context_instance=RequestContext(request))