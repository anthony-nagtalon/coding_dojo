from django.shortcuts import render, redirect
from django.contrib import messages
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
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
        new_show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release-date'],
            desc=request.POST['desc']
        )
        messages.success(request, "Show successfully added")
        return redirect("/shows/{}".format(new_show.id))

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
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/{}/edit".format(id))
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release-date']
        show.desc = request.POST['desc']
        show.save()
        return redirect("/shows/{}".format(id))

def delete_show(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/shows")