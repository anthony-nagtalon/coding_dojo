from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse("Placeholder to display blog number: {}".format(number))

def edit(request, number):
    return HttpResponse("Placeholder to edit blog {}".format(number))

def destroy(request, number):
    return redirect("/blogs")

def jsonExample(request):
    return JsonResponse({"title": "App Title", "content": "Placeholder for content"})