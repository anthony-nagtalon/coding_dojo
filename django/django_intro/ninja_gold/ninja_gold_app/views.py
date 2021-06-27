import random
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        request.session.save()
    return render(request, "index.html")

def process(request):
    earned = 0
    if request.POST['option'] == "farm":
        earned = random.randint(10, 20)
        request.session['activities']
    elif request.POST['option'] == "cave":
        earned = random.randint(5, 10)
    elif request.POST['option'] == "house":
        earned = random.randint(2, 5)
    else: # option = "casino"
        earned = random.randint(-50, 50)

    request.session['gold'] += earned

    if earned > 0:
        request.session['activities'].append({"content": "Earned {} golds from the {}! {}".format(
            earned, request.POST['option'], datetime.now().strftime("%d/%m/%Y %I:%M %p")), "type": "positive"})
    elif earned < 0:
        request.session['activities'].append({"content": "Entered a casino and lost {} golds... Ouch.. {}".format(
            earned * -1, datetime.now().strftime("%d/%m/%Y %I:%M %p")), "type": "negative"})
    else:
        request.session['activities'].append({"content": "Entered a casino and broke even.. Phew, it could be worse! {}".format(
            datetime.now().strftime("%d/%m/%Y %I:%M %p")), "type": "negative"})

    request.session.save()

    return redirect("/")