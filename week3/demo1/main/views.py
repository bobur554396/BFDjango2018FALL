from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    name = "Test name"
    students = [{'id': i, 'name': 'Student {}'.format(i)} for i in range(0, 5)]
    context = {
        'name': name,
        'dd': datetime.datetime.now(),
        'student':
            {
                'id': 1,
                'name': 'Student 1',

            },
        'is_weekend': False,
        'numbers': [i for i in range(0, 10)],
        'students': students
    }

    return render(request, 'index.html', context)


def hello(request):
    return HttpResponse("hello")


def about(request):
    return render(request, 'about.html')


def current_time(request):
    now = datetime.datetime.now()
    html = '<html><body>Time: {}.</body></html>'.format(now)
    return HttpResponse(html)


def hour_ahead(request, offset):
    offset = int(offset)
    new_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In {} hour(s), will be: {}</body></html>'.format(offset, new_time)
    return HttpResponse(html)
