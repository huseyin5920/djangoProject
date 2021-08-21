from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name = 'index'),
     path('books', views.books, name = 'books'),
     path('authors', views.authors, name = 'authors'),
     path('authordetails/<int:authorId>', views.authorDetails, name = 'authordetail')

]