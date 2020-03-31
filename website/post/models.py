from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50, default='Lucas França')
    bio = models.CharField(max_length=80, default='Full Stack Developer - https://github.com/lucasfrancaid')
    email = models.EmailField(max_length=254, default='lucas@lucas.com.br')
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    photo_url = models.URLField(max_length=200)
