from django.db import models
import json

# Create your models here.

class Paper:
    def __init__(self, name, cites, year, under, url):
        self.name   = name
        self.cites  = cites
        self.year   = year
        self.under  = under
        self.hindex = "0"
        self.iindex = "0"
        self.url    = url

class Author:
    def __init__(self, name, cites):
        self.name   = name
        self.cites  = cites
        self.papers = []
        self.hindex = 0
        self.iindex = 0

    def addPaper(self, paper):
        self.papers.append(paper)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def seth(self, h):
        self.hindex = h

    def seti(self, i):
        self.iindex = i
