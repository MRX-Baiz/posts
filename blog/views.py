from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.



def index(request):
    posts = Post.objects.all()
    if request.method == 'POST': 
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home-page')
    else:
        form = PostForm()
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html')