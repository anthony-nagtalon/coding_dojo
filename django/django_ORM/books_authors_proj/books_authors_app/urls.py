from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('add_book', views.add_book),
    path('books/<int:id>', views.display_book),
    path('add_author_to_book', views.add_author_to_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('authors/<int:id>', views.display_author),
    path('add_book_to_author', views.add_book_to_author)
]