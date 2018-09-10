from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    name = "Test name"
    return render(request, 'index.html', {'name': name})


def hello(request):
    return HttpResponse("hello")


def current_time(request):
    now = datetime.datetime.now()
    html = '<html><body>Time: {}.</body></html>'.format(now)
    return HttpResponse(html)


def hour_ahead(request, offset):
    offset = int(offset)
    new_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In {} hour(s), will be: {}</body></html>'.format(offset, new_time)
    return HttpResponse(html)
