from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, PostUpdate, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
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


@login_required
def post_details(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('details-page', pk=post.id)
    else:
        comment_form = CommentForm()
    context = {
            'post': post,
            'comment_form': comment_form,
    }

    return render(request, 'blog/post_details.html', context)


@login_required
def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdate(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('details-page', pk=post.id)
    else:
        form = PostUpdate(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)


@login_required
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home-page')
    context = {
        'post': post,
    }
    return render(request, 'blog/post_delete.html', context)