import random
from enum import Enum
from django.shortcuts import render, redirect

class Result(Enum):
    NEW = 0
    CORRECT = 1
    LOW = 2
    HIGH = 3
    LOSE = 4

# Create your views here.
def index(request):
    if 'answer' not in request.session:
        request.session['answer'] = random.randint(1, 100)
        print("Answer:", request.session['answer'])
        request.session['result'] = Result.NEW.value
        request.session['attempts'] = 0
    return render(request, "index.html")

def guess(request):
    guess = int(request.POST['guess'])
    if guess == request.session['answer']:
        request.session['result'] = Result.CORRECT.value
    elif guess < request.session['answer']:
        request.session['result'] = Result.LOW.value
    else:
        request.session['result'] = Result.HIGH.value
    
    request.session['attempts'] += 1

    if request.session['attempts'] == 5 and request.session['result'] is not Result.CORRECT.value:
        request.session['result'] = Result.LOSE.value
    return redirect("/")

def restart(request):
    if 'answer' in request.session:
        del request.session['answer']
    if 'result' in request.session:
        del request.session['result']
    if 'attempts' in request.session:
        del request.session['attempts']
    return redirect("/")