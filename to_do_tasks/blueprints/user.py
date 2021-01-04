from flask import Flask, render_template, redirect, url_for, request, Blueprint
import sqlite3
import datetime
from functools import wraps
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, TextAreaField,RadioField , SelectField
from to_do_tasks.db import get_db

# define our blueprint
user_bp = Blueprint('user', __name__)

class LoginForm(FlaskForm):
    username = StringField("Username : ", [validators.InputRequired()])
    password = PasswordField("Password : ", [validators.InputRequired()])
    submit = SubmitField("Log In")


@user_bp.route('/', methods =['POST','GET'])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        # read values from the login wtform
        username = login.username.data
        password = login.password.data
        
        # get the DB connection
        db = get_db()
        
        # insert user into db
        try:
            # get user by username
            user= db.execute('SELECT * FROM users WHERE username LIKE ?',(username,)).fetchone()
            # check if username exists
            if user  != None:
                # check if credentials are valid
                if user['username'] == username and user['password'] == password:
                    # store the user ID in the session  
                    session['uid'] = user['id']  
                    session['username'] = user['username']
            return redirect(url_for('taskslist.task_lists'))

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404") 
        # render the login template
        
    return render_template('login/login.html', form = login)    