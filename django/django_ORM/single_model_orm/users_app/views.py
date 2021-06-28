from django.shortcuts import render, redirect
from users_app.models import *

# Create your views here.
def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "index.html", context)

def process(request):
    first_name = request.POST['first-name']
    last_name = request.POST['last-name']
    email = request.POST['email']
    age = int(request.POST['age'])

    new_user = User.objects.create(first_name=first_name, last_name=last_name, email_address=email, age=age)

    return redirect("/")