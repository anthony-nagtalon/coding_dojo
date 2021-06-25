from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    print(request.POST)
    context = {
        "name": request.POST['name'],
        "location": request.POST['location'],
        "fav_lang": request.POST['favLang'],
        "stack": request.POST['curStack'],
        "exp": ', '.join(request.POST.getlist('expIn')),
        "comment": request.POST['comment']
    }
    return render(request, "result.html", context)