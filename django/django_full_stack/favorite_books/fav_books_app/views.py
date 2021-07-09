from django.shortcuts import render, redirect
from django.contrib import messages
from fav_books_app.models import *
import bcrypt

# Create your views here.
def index(request):
    if "id" in request.session:
        return redirect("/books")
    return render(request, "index.html")

def register(request):
    errors = User.objects.registration_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value, extra_tags='register')
        return redirect("/")
    else:
        pw_hash=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=request.POST['first-name'],
            last_name=request.POST['last-name'],
            email=request.POST['email'],
            password=pw_hash
        )
        request.session["id"] = new_user.id
        return redirect("/books")

def login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value, 'login')
    else:
        user = User.objects.filter(email=request.POST['email'])
        if user:
            cur_user = user[0]
            if bcrypt.checkpw(request.POST['pw'].encode(), cur_user.password.encode()):
                request.session["id"] = cur_user.id
                return redirect("/books")
            else:
                messages.add_message(request, messages.ERROR, "Password is incorrect!", extra_tags='login')
        else:
            messages.add_message(request, messages.ERROR, "This email is currently not registered!", 'login')
    return redirect("/")

def logout(request):
    if "id" in request.session:
        del request.session['id']
    return redirect("/")

def books(request):
    if "id" not in request.session:
        return redirect("/")

    context = {
        "logged_user": User.objects.get(id = request.session['id']),
        "books": Book.objects.all()
    }
    return render(request, "books.html", context)

def add_book(request):
    errors = Book.objects.book_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value)
    else:
        new_book = Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            uploaded_by=User.objects.get(id=request.session['id'])
        )
        new_book.users_who_like.add(User.objects.get(id=request.session['id']))
    return redirect("/books")

def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session["id"])
    context = {
        "logged_user": user,
        "book": book
    }
    if user == book.uploaded_by:
        return render(request, "book_edit.html", context)
    else:
        return render(request, "book_details.html", context)

def favorite(request, book_id):
    book = Book.objects.get(id=book_id)
    book.users_who_like.add(User.objects.get(id=request.session["id"]))
    return redirect("/books")

def unfavorite(request, book_id):
    book = Book.objects.get(id=book_id)
    book.users_who_like.remove(User.objects.get(id=request.session["id"]))
    return redirect("/books")

def update_book(request, book_id):
    errors = Book.objects.book_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value)
        return redirect("/books/{}".format(book_id))
    else:
        book = Book.objects.get(id=book_id)
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.save()
        return redirect("/books")

def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect("/books")