# from django.shortcuts import render

# from django.shortcuts import render
# from django.core.handlers.wsgi import WSGIRequest
# from django.http import HttpResponse

# from .models import Category, Post


# def home(request:WSGIRequest):
#     posts =Post.objects.all()
#     return render(request,'index.html',context={"posts":posts})


# # def home(request:WSGIRequest):
# #     return render(request, template_name= 'home.html')


# def about(request:WSGIRequest):
#     return render(request, template_name= '2.html')

# def guruh(request:WSGIRequest):
#     return render(request, template_name= '3.html')


# def address(request:WSGIRequest):
#     return render(request,template_name='4.html')


# def number(request:WSGIRequest):
#     return render(request,template_name='5.html')


# def mac(request:WSGIRequest):
#     return render(request,template_name='6.html')

# def iphone(request:WSGIRequest):
#     return render(request,template_name='7.html')

# def mercedes(request:WSGIRequest):
#     return render(request,template_name='8.html')

# def GTR(request:WSGIRequest):
#     return render(request,template_name='9.html')

# def info(request:WSGIRequest):
#     return render(request,template_name='10.html')

# def contact(request):
#     return HttpResponse("Contact")


# Create your views here.






from django.shortcuts import render
from .models import Author, book, Review


def author_list(request):
    authors = Author.objects.all() 
    return render(request, 'author_list.html', {'authors': authors})

def book_list(request):
    books = book.objects.all()  
    return render(request, 'book_list.html', {'books': books})

def review_list(request):
    reviews = Review.objects.all()  
    return render(request, 'review_list.html', {'reviews': reviews})
