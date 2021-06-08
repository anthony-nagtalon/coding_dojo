import random
from enum import Enum
from flask import Flask, render_template, request, redirect, session

class Result(Enum):
    NEW = 0
    CORRECT = 1
    LOW = 2
    HIGH = 3
    LOSE = 4

app = Flask(__name__)
app.secret_key = "this_is_my_secret_key_ehehe"

@app.route("/")
def default():
    if 'answer' not in session:
        session['answer'] = random.randint(1, 100)
        print("Answer:" + str(session['answer']))
        session['result'] = Result.NEW.value
        session['attempts'] = 0
    return render_template('index.html')

@app.route("/guess", methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if guess == session['answer']:
        session['result'] = Result.CORRECT.value
    elif guess < session['answer']:
        session['result'] = Result.LOW.value
    else:
        session['result'] = Result.HIGH.value

    session['attempts'] += 1

    if session['attempts'] == 5 and session['result'] is not Result.CORRECT.value:
        session['result'] = Result.LOSE.value
    return redirect("/")

@app.route("/restart")
def restart():
    if 'answer' in session:
        session.pop('answer')
    if 'result' in session:
        session.pop('result')
    if 'attempts' in session:
        session.pop('attempts')
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)