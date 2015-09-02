from django.db import models
import json

# Create your models here.

class Paper:
    def __init__(self, name, cites, year):
        self.name   = name
        self.cites  = cites
        self.year   = year

class Author:
    def __init__(self, name):
        self.name   = name
        self.papers = []

    def addPaper(self, paper):
        self.papers.append(paper)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
