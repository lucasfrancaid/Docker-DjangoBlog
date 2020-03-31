from django.db import models 

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name
