from django.shortcuts import render, redirect
from django.contrib import messages
from wall_app.models import *
import bcrypt

# Create your views here.
def index(request):
    if "id" in request.session:
        return redirect("/wall")
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
        return redirect("/wall")

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
                return redirect("/wall")
            else:
                messages.add_message(request, messages.ERROR, "Password is incorrect!", extra_tags='login')
        else:
            messages.add_message(request, messages.ERROR, "This email is currently not registered!", 'login')
    return redirect("/")

def wall(request):
    if "id" not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id = request.session["id"]),
        "messages": Message.objects.all().order_by("-created_at")
    }
    return render(request, "wall.html", context)

def message(request):
    errors = Message.objects.input_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors:
            messages.add_message(request, messages.ERROR, value)
    else:
        Message.objects.create(
            user=User.objects.get(id=request.session['id']),
            message=request.POST['message']
        )
    return redirect("/wall")

def comment(request):
    errors = Comment.objects.input_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors:
            messages.add_message(request, messages.ERROR, value)
    else:
        Comment.objects.create(
            user=User.objects.get(id=request.session['id']),
            message=Message.objects.get(id=request.POST['message-id']),
            comment=request.POST['comment']
        )
    return redirect("/wall")

def logout(request):
    if "id" in request.session:
        del request.session["id"]
    return redirect("/")