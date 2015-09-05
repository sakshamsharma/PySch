
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


qdict = {'mauthors': 'Manindra', 'view_op': 'search_authors'}
query = 'google scholar' + raw_input('Enter author:')
f = {'q' : query}
q = urllib.urlencode(f)
#request.author
#author='google scholar' + raw_input('Enter author:')
#autho = urllib.urlencode(author)
html = getPage('https://www.google.co.in/search?'+q, {})
html1 = ' ' 
a= ''
b= ''

# Parse this data and find url for the author's homepage
soup = BeautifulSoup(html)
for tag in soup.findAll('a',href=True):
        b= tag['href']
        if b.startswith('http://scholar.google.com/citations?user='):
            print a+"""----------------
            --------------
            -----------"""
            html1= getPage(b,{})
            break
#html1 = getPage(authUrl, {})
# Create dher saare objects and add each paper object to the class of the author
# Also scrape the author h-index and the i-index
# Return author.toJSON();
#print url
f = open ( 'open.html', 'w+')
print >> f, (soup.prettify().encode('utf-8'))
f.close()
soup1=BeautifulSoup(html1)
f1 = open ( 'open1.html', 'w+')
print >> f1, (soup1.prettify().encode('utf-8'))
f1.close()