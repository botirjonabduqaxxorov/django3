from django.shortcuts import render

from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def home(request:WSGIRequest):
    return render(request, template_name= 'home.html')


def about(request:WSGIRequest):
    return render(request, template_name= '2.html')

def guruh(request:WSGIRequest):
    return render(request, template_name= '3.html')


def address(request:WSGIRequest):
    return render(request,template_name='4.html')


def number(request:WSGIRequest):
    return render(request,template_name='5.html')


def mac(request:WSGIRequest):
    return render(request,template_name='6.html')

def iphone(request:WSGIRequest):
    return render(request,template_name='7.html')

def mercedes(request:WSGIRequest):
    return render(request,template_name='8.html')

def GTR(request:WSGIRequest):
    return render(request,template_name='9.html')

def info(request:WSGIRequest):
    return render(request,template_name='10.html')

def contact(request):
    return HttpResponse("Contact")


# Create your views here.
