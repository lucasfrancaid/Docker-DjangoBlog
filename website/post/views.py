from django.shortcuts import render, redirect
from .models import Post
from .form import PostForm

import datetime

def home(request):
    data = {}
    data['posts'] = Post.objects.all()
    
    return render(request, 'post/index.html', data)

def create(request):
    form = PostForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('url_index')
    return render(request, 'post/form.html', {'form':form})

def read(request, pk):
    post = Post.objects.get(pk=pk)
    
    return render(request, 'post/read.html', {'post':post})

def update(request, pk):
    data = {}
    post = Post.objects.get(pk=pk)
    form = PostForm(request.POST or None, instance=post)
    
    if form.is_valid():
        form.save()
        return redirect('url_index')
    
    data['form'] = form
    data['post'] = post
    return render(request, 'post/form.html', data)

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    
    return redirect('url_index')