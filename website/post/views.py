from django.shortcuts import render, redirect
from .models import Post
from .form import PostForm

def home(request):
    data = {}
    data['posts'] = Post.objects.all()
    
    return render(request, 'post/home.html', data)

def post_list(request):
    data = {}
    data['posts'] = Post.objects.all()
    
    return render(request, 'post/list.html', data)

def post_create(request):
    form = PostForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('url_home')
    return render(request, 'post/form.html', {'form':form})

def post_read(request, pk):
    post = Post.objects.get(pk=pk)
    
    return render(request, 'post/read.html', {'post':post})

def post_update(request, pk):
    data = {}
    post = Post.objects.get(pk=pk)
    form = PostForm(request.POST or None, instance=post)
    
    if form.is_valid():
        form.save()
        return redirect('url_home')
    
    data['form'] = form
    data['post'] = post
    return render(request, 'post/form.html', data)

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    
    return redirect('url_home')