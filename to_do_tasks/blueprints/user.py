from flask import Flask, render_template, redirect, url_for, request, Blueprint,session
import sqlite3
import datetime
from functools import wraps
from to_do_tasks.db import get_db
from ..forms import LoginForm, AddUser
from .taskslist import login_required

# define our blueprint
user_bp = Blueprint('user', __name__)


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
            db.execute("INSERT INTO users (username, password , firstname , lastname) VALUES (?, ? , ? , ?);", (username, password, first_name, last_name,))

            # write changes to DB
            db.commit()
            
            return redirect(url_for('user.login'))

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")

    return render_template('user/add.html' , form = user )


@user_bp.route('/login', methods =['POST','GET'])
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
            user = db.execute('SELECT * FROM users WHERE username LIKE ?',(username,)).fetchone()
            
            # check if user exists in db
            if user != None:

                # check if password is correct
                if user['password'] == password :
                    
                    # store the user id and username in the session  
                    session['uid'] = user['id']  
                    session['username'] = user['username']

                    return redirect(url_for('taskslist.task_lists'))

                else:
                    print("Wrong Password!")
                    
            else:
                return redirect(url_for('user.add_user'))

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404") 

        
    return render_template('user/login.html', form = login)
          

@user_bp.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect("/")


@user_bp.route('/session')
@login_required
def show_session():
    return dict(session)