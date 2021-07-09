from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('books', views.books),
    path('books/add', views.add_book),
    path('books/<int:book_id>', views.show_book),
    path('books/<int:book_id>/update', views.update_book),
    path('books/<int:book_id>/destroy', views.delete_book),
    path('books/<int:book_id>/favorite', views.favorite),
    path('books/<int:book_id>/unfavorite', views.unfavorite)
]