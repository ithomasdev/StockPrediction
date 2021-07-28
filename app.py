from flask import Flask, render_template, redirect, url_for, request, session


app = Flask(__name__)
app.secret_key = 'Stock prediction'


@app.route('/')
def home():
    return render_template('index.ejs')


@app.route('/login', methods=['POST', 'GET'])
def login(user, password):
    if request.methods == 'POST':
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


@app.route('/about/devs')
def about_devs(devs):
    return 'About the Devs'


@app.route('/featured stocks')
def featured_stocks():
    return "Featured Stocks"


@app.route('/featured_stocks/ticker', methods=['GET', 'POST', 'DELETE'])
def tickers(ticker):
    if request.methods == 'GET':
        return "Stock: " + ticker

    if request.methods == 'POST':
        return ticker

    if request.methods == 'DELETE':
        return ticker

    else:
        'Post Error 405 Method Not Allowed'


@app.route('/progress')
def progress():
    return 'Progress Updates'


if __name__ == '__main__':
    app.run(debug=True)
