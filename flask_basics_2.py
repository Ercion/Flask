from flask import Flask,redirect,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Heyyy!'


@app.route('/admin')
def hello_admin():
    return 'Welcome Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Welcome %s' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__=='__main__':
    app.run(debug=True)


'''
:redirect --> To redirect a user to another endpoint, use the redirect() function

:url_for --> To build a URL to a specific function, use the url_for() function. 
It accepts the name of the function as its first argument and any number of keyword arguments,
 each corresponding to a variable part of the URL rule. 


'''