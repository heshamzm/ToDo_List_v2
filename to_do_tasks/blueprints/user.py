from flask import Flask, render_template, redirect, url_for, request, Blueprint,session
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

class AddUser(FlaskForm):
    username = StringField("Username : ", [validators.InputRequired()])
    password = PasswordField("Password : ", [validators.InputRequired()])
    first_name = StringField("first name : ", [validators.InputRequired()])
    last_name = StringField("last name : ", [validators.InputRequired()])
    submit = SubmitField("Add User")

@user_bp.route('/add/user', methods=['GET', 'POST'])
def add_user():

    user = AddUser()

    if user.validate_on_submit():
    
        username = user.username.data
        password = user.password.data
        first_name = user.first_name.data
        last_name = user.last_name.data
        
        # get the DB connection
        db = get_db()

        # insert user into DB
        try:
            # execute our insert SQL statement
            db.execute("INSERT INTO users (username, password , firstname , lastname  ) VALUES (?, ? , ? , ?);", (username, password, first_name,last_name,))

            # write changes to DB
            db.commit()
            
            return redirect(url_for('taskslist.task_lists'))

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")

    return render_template('user/add.html' , form = user )



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

@user_bp.route('/logout')
def logout():
    # pop 'uid' from session
    session.clear()

    # redirect to index
    return redirect("/")

@user_bp.route('/session')
def show_session():
    return dict(session)