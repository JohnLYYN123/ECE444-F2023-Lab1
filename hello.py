
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)


# hello world homepage
@app.route('/')
def index():
    return render_template("index.html")

# example 2.2 part
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)





