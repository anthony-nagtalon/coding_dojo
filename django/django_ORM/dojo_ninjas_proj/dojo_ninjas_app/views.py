from django.shortcuts import render, redirect
from dojo_ninjas_app.models import *

# Create your views here.
def index(request):
    context = {
        "dojos": Dojo.objects.all(),
        "ninjas": Ninja.objects.all()
    }
    return render(request, "index.html", context)

def create_dojo(request):
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect("/")

def create_ninja(request):
    Ninja.objects.create(dojo=Dojo.objects.get(id=request.POST['dojo-id']), 
        first_name=request.POST['first-name'], 
        last_name=request.POST['last-name'])
    return redirect("/")