from django.shortcuts import render

# Create your views here.

def index(request) :
    return render(request,'foodief/index.html')


def register(request) :
    pass

def authenticate(request) :
    pass