from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'contact.html'


class ContactView(AboutView):
    pass


class HomeView(View):

    def get(self, request):
        print(request.method == "get")
        return HttpResponse('<h1>Class based Home page</h1>')


def home(request):
    return HttpResponse('<h1>Function based Home page</h1>')
