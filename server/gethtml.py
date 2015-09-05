import urlparse
import urllib
import urllib2
from bs4 import BeautifulSoup
from lxml import etree

def getPage(url, f):
    q = urllib.urlencode(f)
    urln = url + q
    print("****" + urln)
    htmltext = urllib2.urlopen(urln).read()
    return htmltext
