from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "some secret key shhhh"

@app.route("/")
def counter():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1

    if 'value' in session:
        session['value'] += 1
    else:
        session['value'] = 1
    return render_template("index.html")

@app.route("/destroy_session")
def destroy_session():
    if 'visits' in session:
        session.pop('visits')
    if 'value' in session:
        session.pop('value')
    return redirect("/")

@app.route("/double")
def double():
    session['value'] += 1
    return redirect("/")

@app.route("/add", methods=["POST"])
def add():
    session['value'] += (int(request.form['add'])-1)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)