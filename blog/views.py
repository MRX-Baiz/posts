from django.shortcuts import render
from .models import Post


# Create your views here.



def index(request):
    post = Post.objects.all()
    return render(request, 'blog/index.html', {'post' : post})

def about(request):
    return render(request, 'blog/about.html')