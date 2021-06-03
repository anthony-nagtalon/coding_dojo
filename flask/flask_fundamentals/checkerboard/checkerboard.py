from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default_board():
    return render_template('index.html', height = 8, width = 8)

@app.route('/<height>')
def diff_height_board(height):
    return render_template('index.html', height = int(height), width = 8)

@app.route('/<height>/<width>')
def variable_board(height, width):
    return render_template('index.html', height = int(height), width = int(width))

if __name__ == "__main__":
    app.run(debug=True)