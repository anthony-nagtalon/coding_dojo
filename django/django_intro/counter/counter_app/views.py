from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 1
    
    if 'value' in request.session:
        request.session['value'] += 1
    else:
        request.session['value'] = 1
    
    return render(request, "index.html")

def destroy_session(request):
    if 'visits' in request.session:
        del request.session['visits']
    if 'value' in request.session:
        del request.session['value']
    return redirect("/")

def double(request):
    request.session['value'] += 1
    return redirect("/")

def add(request):
    request.session['value'] += (int(request.POST['add']) - 1)
    return redirect("/")