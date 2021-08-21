from django import template
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context, loader
from .models import Author
from django.http import Http404
# Create your views here.

def index(request):
    return HttpResponse("Anasayfa")


def authors(request):
    context = {
        'authors_list' : Author.objects.all()
    }
    return render(request, "authors.html", context)

def books(request):
    return HttpResponse("Kitaplar")

def authorDetails(request, authorId):
    try:
        context = {
            'author_detail' : Author.objects.get(pk=authorId)
        }
    except:
        raise Http404("YAZAR BULUNAMADI")
    return render(request, "authorDetail.html", context)


#def authors(request):
#    template = loader.get_template('authors.html')
#    context = {
#        'authors_list' : Author.objects.all()
#    }
#    return HttpResponse(template.render(context, request))