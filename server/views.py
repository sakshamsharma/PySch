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

    soup1 = BeautifulSoup(html1, "lxml")
    
    authorname = ""
    for divs in soup1.findAll('div', {"id": "gsc_prf_in"}):
        authorname = divs.contents[0].encode()

    author = Author(authorname, 100)

    for item in soup1.findAll('tr', {"class": "gsc_a_tr"}):
        tds = item.findChildren()
        # Paper name
        # print(str(tds[0].findChildren()[0].contents[0]))
        name = tds[0].findChildren()[0].contents[0]
        # Paper authors
        # print(str(tds[0].findChildren()[1].contents[0]))
        authors = tds[0].findChildren()[1].contents[0]
        # Paper journal
        # print(str(tds[3].contents[0])[:-3])
        journal = tds[3].contents[0][:-3]
        # Paper year
        # print(str(tds[4].contents[0])[2:])
        year = tds[4].contents[0][2:]
        # Paper cites
        # print(str(tds[5].findChildren()[0].contents[0]))
        cites = tds[5].findChildren()[0].contents[0]
        # print("****")

        paper = Paper(name, cites, year, authors)
        author.addPaper(paper)


    # Create dher saare objects and add each paper object to the class of the author
    # Also scrape the author h-index and the i-index
    # Return author.toJSON();
    return Response(author.toJSON())

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
