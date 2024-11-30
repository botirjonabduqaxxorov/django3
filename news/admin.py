from django.contrib import admin

from.models import Author,book,Review

# Register your models here.

admin.site.register(Author)
admin.site.register(book)
admin.site.register(Review)