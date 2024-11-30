from django.db import models

# Create your models here.

class Author(models.Model):
    name =models.CharField(max_length=50,unique=True)
    first_name = models.CharField(max_length=100)  
    last_name = models.CharField(max_length=100)   
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)  

    def __str__(self):
        return self.name

class book(models.Model):
    name =models.CharField(max_length=255)
    title = models.CharField(max_length=200) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    publication_date = models.DateField()  
    isbn = models.CharField(max_length=13, unique=True) 
    genre = models.CharField(max_length=100)  
    summary = models.TextField(blank=True) 
    # category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Review(models.Model):
    book = models.ForeignKey(book, related_name='reviews', on_delete=models.CASCADE)  
    reviewer_name = models.CharField(max_length=100)  
    rating = models.PositiveSmallIntegerField()  
    comment = models.TextField(blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name