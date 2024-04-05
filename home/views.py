from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home/homepage.html')


def posts(request):
    pass


def single_post(request):
    pass
