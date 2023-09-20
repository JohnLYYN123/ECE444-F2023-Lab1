
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


# homepage
@app.route('/')
def index():
    return render_template("index.html", current_time=datetime.utcnow())


# example 2.2 part
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500






