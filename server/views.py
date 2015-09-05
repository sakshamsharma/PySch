from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import urllib
import urlparse
import json

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
    qdict = {'mauthors': request.author, 'view_op': 'search_authors'}
    html = getPage('https://scholar.google.com/citations?', qdict)
    # Parse this data and find url for the author's homepage
    html1 = getPage(authUrl, {})
    # Create dher saare objects and add each paper object to the class of the author
    # Also scrape the author h-index and the i-index
    # Return author.toJSON();
    return Response(data)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
