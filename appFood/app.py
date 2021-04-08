from flask import Flask, render_template_string, url_for, redirect
from View.Home import Home
from View.test import TestData

app = Flask(__name__)

@app.route("/")
def index():
    home = Home()
    return render_template_string(f'{home}')

@app.route("/testData")
def test():
    test = TestData()
    return render_template_string(f'{test}')

if __name__ == '__main__':
    app.run(debug=True)
