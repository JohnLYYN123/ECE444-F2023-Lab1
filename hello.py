# this file is used for Activity 2

from flask import Flask
app = Flask(__name__)


# hello world homepage
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

# example 2.2 part
@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)


