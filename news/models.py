from django.db import models

# Create your models here.

class Category(models.Model):
    name =models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    name =models.CharField(max_length=255)
    content=models.TextField(blank=True,null=True)
    photo =models.TextField(blank=True,null=True)
    viewse=models.TextField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    published=models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name