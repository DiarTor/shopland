from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home/homepage.html')


def posts(request):
    return render(request, 'home/all-posts.html')


def single_post(request, slug):
    return render(request, 'home/post-detail.html', {"slug": slug})
