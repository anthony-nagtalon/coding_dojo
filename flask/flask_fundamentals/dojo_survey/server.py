from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def display_result():
    name = request.form['name']
    location = request.form['location']
    fav_lang = request.form['favLang']
    stack = request.form['curStack']
    exp = request.form.getlist('expIn')
    comment = request.form['comment']

    return render_template('result.html',
        name=name, location=location, fav_lang=fav_lang,
        stack=stack, exp=", ".join(exp), comment=comment)

if __name__ == "__main__":
    app.run(debug=True)