from flask import Flask, render_template, redirect, url_for, request, session
import dask.dataframe as df
import os
import set_up

app = Flask(__name__)
app.secret_key = 'Stock prediction'

Stocks = set_up.get_stocks()

@app.route('/')
def home():
    return 'Hello World!'


@app.route('/login', methods=['POST', 'GET'])
def login(user, password):
    if request.method == 'POST':
        user = request.form['']
        password = request.form['']
        session['user'] = user
        return redirect(url_for('user'))

    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template(login.html)


@app.route('/user')
def login_user(user):
    if 'user' in session:
        user = session['user']
        return user
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('User', None)
    return redirect(url_for('login'))


@app.route('/about')
def about():
    return 'About the Project'


@app.route('/about/<devs>')
def about_devs(devs):
    return 'About the Devs %s' % devs


@app.route('/Stock')
def featured_stocks():
    return "Featured Stocks"


@app.route('/Stock/<ticker>', methods=['GET', 'POST', 'DELETE'])
def tickers(ticker):
    if request.method == 'GET':
        return "Stock: %s" % ticker + "You are using a GET method"

    if request.method == 'POST':
        return "Stock: %s" % ticker

    if request.method == 'DELETE':
        return "Stock: %s" % ticker

    else:
        return 'Post Error 405 Method Not Allowed'


@app.route('/progress')
def progress():
    return 'Progress Updates'


if __name__ == '__main__':
    # prepares data before app runs
    set_up.set_up()
    app.run(debug=True)
