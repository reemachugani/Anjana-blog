from singlepage.models import Singlepage

def singlepages(request):
    singlepages = Singlepage.objects.all()
    return {'singlepages': singlepages}