from django.http import HttpResponse
from main.models import Publisher
import json


def index(request):
    a = Publisher.objects.all()
