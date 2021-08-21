from django.contrib import admin

# Register your models here.
from .models import Author
from .models import Book

admin.site.register(Author)
admin.site.register(Book)