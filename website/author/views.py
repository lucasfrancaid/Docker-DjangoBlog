from django.shortcuts import render, redirect
from .models import Author
from .form import AuthorForm

def author_list(request):
    data = {}
    data['authors'] = Author.objects.all()
    
    return render(request, 'author/list.html', data)

def author_create(request):
    form = AuthorForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('url_home')
    return render(request, 'author/form.html', {'form':form})

def author_read(request, pk):
    author = Author.objects.get(pk=pk)
    
    return render(request, 'author/read.html', {'author':author})

def author_update(request, pk):
    data = {}
    author = Author.objects.get(pk=pk)
    form = AuthorForm(request.POST or None, instance=author)
    
    if form.is_valid():
        form.save()
        return redirect('url_home')
    
    data['form'] = form
    data['author'] = author
    return render(request, 'author/form.html', data)

def author_delete(request, pk):
    author = Author.objects.get(pk=pk)
    author.delete()
    
    return redirect('url_home')