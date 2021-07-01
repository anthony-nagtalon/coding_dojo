from django.shortcuts import render, redirect
from tv_shows_app.models import *

# Create your views here.
def shows(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "shows.html", context)

def add_show_page(request):
    return render(request, "add_show.html")

def add_show(request):
    new_show = Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release-date'],
        desc=request.POST['desc']
    )
    return redirect("/shows/{}".format(new_show.id)) # Switch to new entry ID

def display_show(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "show_page.html", context)

def edit_show_page(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "edit_show.html", context)

def edit_show(request, id):
    show = Show.objects.get(id=id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release-date']
    show.desc = request.POST['desc']
    show.save()
    return redirect("/shows/{}".format(id)) # Switch to new entry ID

def delete_show(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/shows")