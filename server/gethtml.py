import urlparse
import urllib
import mechanize
from bs4 import BeautifulSoup
from lxml import etree
import time
import webbrowser

def getPage(url, f):
    br=mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders=[('User-agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.19985.125 Safari/537.36'),('Accept', '*/*')]
    br.set_proxies({"http:": "cseguest:natraj25@nknproxy.iitk.ac.in:3128"})

    q = urllib.urlencode(f)
    urln = url + q
    htmltext = br.open(url).read()
    return htmltext
