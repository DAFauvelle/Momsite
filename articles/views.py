from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import Context, loader
from .models import Article, Family, Reference, Liens, Photos, ImagePDF

# Create your views here.
"""def index(resquest):
    return HttpResponse("Hello, world. This is my mom's site!")"""
    
def index(request):
    return render_to_response('articles/homepage.html', {'famillies': Family.objects.all()})
    
def famille(request, famille):
    articles = Article.objects.filter()
    famillies = Family.objects.all()

    les_articles = []
    for f in famillies:
        if (f.name == famille):
            famille_choisi = f
    for a in articles:
        if (a.family == famille_choisi):
            les_articles.append(a)
    les_articles.sort(key=lambda x: x.my_order)
    photos = Photos.objects.all()
    imagesPdf = ImagePDF.objects.all()
    return render_to_response('articles/famille.html',{
        'articles':les_articles,
        'famillies': Family.objects.all(),
        'famille': famille_choisi,
        'photos': photos,
        'imagesPdf': imagesPdf
    })

def bibliographie(request):
    articles = Article.objects.filter()
    famillies = Family.objects.all()
    refs = Reference.objects.all()
    return render_to_response('articles/bibliographie.html',{
        'articles': articles,
        'famillies': famillies,
        'refs': refs
        })

def liens(request):
    liens = Liens.objects.filter()
    famillies = Family.objects.all()
    return render_to_response('articles/liens.html',{
        'liens':liens,
        'famillies':famillies,
        })
    