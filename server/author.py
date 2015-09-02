# import requests

# def getAuthor(author, i_year, f_year):
    # r = requests.get('https://scholar.google.co.in/scholar?q=author%3Amani&btnG=&hl=en&as_sdt=0%2C5')
    # print (r.text)
    # return (r.text)

from urllib import FancyURLopener

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'

def getAuthor(author, i_year, f_year):
    openurl = MyOpener().open
    url = 'https://scholar.google.co.in/scholar?hl=en&q=author%3Amani&btnG='
    res = openurl(url).read()
    print (res)
    return res
