PySch
=====

Meant as a demonstration for a simple Django application using REST calls.

Includes a lot of BeautifulSoup magic, to be found in `server/views.py`


Rajputs pool entry for Web Development event in Takneek'15

To run frontend server:
```
python2 -m SimpleHTTPServer 8001
```
(or python for Ubuntu users)
Open the app at localhost port 8001

To run the backend (currently not connected):
```
python2 manage.py runserver
```

Packages needed:
djangorestframework
rest_framework
markdown
mechanize
django-cors-headers
