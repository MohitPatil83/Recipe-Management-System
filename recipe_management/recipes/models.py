from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Recipe(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    description= models.TextField()
    ingredients=models.TextField()
    category=models.CharField(max_length=199)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        
        return reverse("recipes-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
   


    