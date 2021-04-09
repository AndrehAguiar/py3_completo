from flask import Flask, render_template_string, request, redirect, url_for, make_response
from View.Home import Home
from View.Client import Client
from View.test import TestData

app = Flask(__name__)

@app.route("/")
def index():
    home = Home()
    if request.cookies is not None:
        email = request.cookies.get('userEmail')
        name = request.cookies.get('userName')
        points = request.cookies.get('userPoints')
        home._setClient(dict(zip(['name','points','email'],[name, points, email])))

    home.setContent()
    return render_template_string(f'{home}')

@app.route("/client", methods = ['GET','POST'])
def client():
    client = Client()
    if request.method == "POST":
        user = request.form['email']
        client.setClient(user)
        resp = make_response(redirect(url_for('index')))
        print(request.cookies)
        if request.cookies.get('userName') != None:
            resp.delete_cookie('userName', path='/', domain='127.0.0.1')
            resp.delete_cookie('userPoints', path='/', domain='127.0.0.1')
            resp.delete_cookie('userEmail', path='/', domain='127.0.0.1')

        resp.set_cookie('userName', client.client.getName())
        resp.set_cookie('userPoints', str(client.client.getPoints()))
        resp.set_cookie('userEmail', client.client.getEmail())
        return resp
    else:
        client.setContent()
        return render_template_string(f'{client}')

@app.route("/testData")
def test():
    test = TestData()
    return render_template_string(f'{test}', test=True)

if __name__ == '__main__':
    app.run(debug=True)
