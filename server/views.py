from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import urllib
import urlparse
import json
from bs4 import BeautifulSoup

from .models import Author, Paper
from .author import *
from .gethtml import *

paper1 = Paper("AKS", 1000, 2003, "Manindra Agarwal")
paper2 = Paper("PID", 100, 2005, "Manindra Agarwal")
author = Author("Manindra Agarwal", 1100)
author.addPaper(paper1)
author.addPaper(paper2)

@api_view(['GET', 'POST'])
def getPapers(request):
    data = author.toJSON();
    # data = getAuthor(request.GET['author'], 2001, 2003)
    return Response(data)

@api_view(['GET', 'POST'])
def auth1(request):
    
    f = {'mauthors': request.GET['author'], 'view_op': "search_authors"}
    html = getPage('https://scholar.google.com/citations?', f)
    soup = BeautifulSoup(html, "lxml")
    html1 = ""
    for tag in soup.findAll('a',href=True):
        b= tag['href']
        if b.startswith('/citations?user='):
            html1 = getPage('https://scholar.google.com' + b, {})
            break

    for item in soup.findAll('a',{"class":"gsc_a_at"}):
        print item

    # Create dher saare objects and add each paper object to the class of the author
    # Also scrape the author h-index and the i-index
    # Return author.toJSON();
    return Response(html)

def auth2(request):
    a=1
def auth3(request):
    a=1
def auth4(request):
    a=1
    
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
