from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('html/index.jinja')

app.run(host="0.0.0.0", port="5000", debug=True)