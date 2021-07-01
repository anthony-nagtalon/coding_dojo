from django.shortcuts import render, redirect
from books_authors_app.models import *

# Create your views here.
def books(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, "books.html", context)

def add_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect("/")

def display_book(request, id):
    context = {
        "book": Book.objects.get(id=id),
        "authors": Author.objects.all()
    }
    return render(request, "book_page.html", context)

def add_author_to_book(request):
    book = Book.objects.get(id=request.POST['book-id'])
    book.authors.add(Author.objects.get(id=request.POST['author-id']))
    return redirect("/books/{}".format(request.POST['book-id']))

def authors(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def add_author(request):
    Author.objects.create(first_name=request.POST['first-name'],
        last_name=request.POST['last-name'], notes=request.POST['notes'])
    return redirect("/authors")

def display_author(request, id):
    context = {
        "author": Author.objects.get(id=id),
        "books": Book.objects.all()
    }
    return render(request, "author_page.html", context)

def add_book_to_author(request):
    author = Author.objects.get(id=request.POST['author-id'])
    author.books.add(Book.objects.get(id=request.POST['book-id']))
    return redirect("/authors/{}".format(request.POST['author-id']))