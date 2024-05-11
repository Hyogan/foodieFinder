from django.shortcuts import  render
from django.template import RequestContext
# Create your views here.

def index(request) :
    return render(request,'core/index.html')




def handler404(request, *args, **argv):
    return render(request, '404.html', status=500)


def handler500(request, *args, **argv):
    return render(request, '404.html', status=500)