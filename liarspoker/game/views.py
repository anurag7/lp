__author__ = 'anuragsaxena'
import requests
from django.http import HttpResponse
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')