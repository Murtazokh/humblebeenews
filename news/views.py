from urllib.request import urlopen
from django.shortcuts import render, redirect
from news.models import *
from django.core.paginator import Paginator


def index(req):
    """This function renders scraped information to html file"""
    # n = News.objects.all()[::-1]
    n = Post.objects.all()[::-1]
    p = Paginator(Post.objects.all(), 10)
    page = req.GET.get('page')
    new = p.get_page(page)
    context = {
       "object_list":n,
       "new":new
    }
    return render(req, 'news/index.html', context )

def sport(req):
    """This function renders scraped information to html file that about sport"""
    sport = Sport.objects.all()
    context = {
       "object_list":sport
    }
    return render(req, 'news/sport.html', context )

def siyosat(req):
    """This function renders scraped information to html file that about politics"""
    n = Politics.objects.all()[::-1]
    context = {
       "object_list":n
    }
    return render(req, 'news/siyosat.html', context )

def economy(req):
    """This function renders scraped information to html file that about economics"""
    objects = Economy.objects.all()[::-1]
    context = {
       "object_list":objects
    }
    return render(req, 'news/jahon.html', context )    

def body(request, pk):
    body = Post.objects.get(pk = pk)
    context = {
        "body":body,
    }
    return render(request,"content.html", context)

def body_sport(request, pk):
    body = Sport.objects.get(pk = pk)
    context = {
        "body":body,
    }
    return render(request,"sport_body.html", context)  

def body_politics(request, pk):
    body = Politics.objects.get(pk = pk)
    context = {
        "body":body,
    }
    return render(request,"politics_body.html", context) 

def body_economy(request, pk):
    body = Economy.objects.get(pk = pk)
    context = {
        "body":body,
    }
    return render(request,"economy_body.html", context)           