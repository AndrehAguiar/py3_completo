from flask import Flask, render_template_string, request, redirect, url_for, make_response
from View.ViewHome import Home
from View.ViewClient import Client
from View.ViewCheckout import Checkout
from View.ViewSale import Sale
from View.test import TestData

app = Flask(__name__)

def getCookies():
    email = request.cookies.get('userEmail')
    name = request.cookies.get('userName')
    points = request.cookies.get('userPoints')

    return dict(zip(['name','points','email'],[name, points, email]))

@app.route("/")
def index():
    home = Home()
    if request.cookies.get('userEmail') is not None:
        home._setClient(getCookies())

    home.setContent()
    return render_template_string(f'{home}')

@app.route("/client", methods = ['GET','POST'])
def client():
    client = Client()
    if request.method == "POST":
        user = request.form['email']
        client.setClient('email', user)
        resp = make_response(redirect(url_for('index')))

        if request.cookies.get('userName') != None:
            resp.delete_cookie('userName', path='/', domain='127.0.0.1')
            resp.delete_cookie('userPoints', path='/', domain='127.0.0.1')
            resp.delete_cookie('userEmail', path='/', domain='127.0.0.1')

        resp.set_cookie('userName', client.client.getName())
        resp.set_cookie('userPoints', str(client.client.getPoints()))
        resp.set_cookie('userEmail', client.client.getEmail())
        return resp
    else:
        if request.cookies.get('userName') != None:
            client._setClient(getCookies())

        client.setContent()
        return render_template_string(f'{client}')

@app.route("/confirm/<status>", methods=['GET','POST'])
def confirm(status):

    sale = Sale()
    if request.cookies.get('userEmail') is not None:
        sale._setClient(getCookies())

    if request.method == "POST" and status == "check":
        userSale = request.form["userShop"]

        if sale.setSale(userSale):
            return redirect(url_for('confirm', status='success'))
        else:
            return redirect(url_for('confirm', status='error'))

    if status == 'success':
        sale.setShop()

    sale.setContent(status)
    return render_template_string(f'{sale}')

    return redirect(url_for('index'))

@app.route("/checkout", methods = ['GET','POST'])
def checkOut():
    if request.method == "POST":
        checkout = Checkout()

        if request.cookies.get('userEmail') is not None:
            checkout._setClient(getCookies())

        shop = request.form['shop']
        checkout.setShop(shop)
        checkout.setContent()
        return render_template_string(f'{checkout}')

    return redirect(url_for('index'))


@app.route("/testData")
def test():
    test = TestData()
    return render_template_string(f'{test}')

if __name__ == '__main__':
    app.run(debug=True)
