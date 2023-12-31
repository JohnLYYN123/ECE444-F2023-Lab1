from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'good morning buenos dias'


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


# homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')

        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')

        session['name'] = form.name.data

        email_invalid = False

        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email')

        if 'utoronto' not in form.email.data:
            email_invalid = True

        session['email'] = form.email.data
        session['email_invalid'] = email_invalid
        return redirect(url_for('index'))
    return render_template("index.html", form=form, name=session.get('name'),
                           email=session.get('email'), email_invalid=session.get('email_invalid'))


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






