# from status import Status       
# from priority import Priority
from flask import Flask, render_template, redirect, url_for, request, Blueprint
import sqlite3
import datetime
from functools import wraps
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TextAreaField
from to_do_tasks.db import get_db

# define our blueprint
taskslist_bp = Blueprint('taskslist', __name__)


class EditNameForm(FlaskForm):
    new_name = StringField("New Name: ", [validators.InputRequired()])
    submit = SubmitField("Edit Name")



# tasklist routing
@taskslist_bp.route("/")
def task_lists():

    # connecting to the database
    db = get_db()

    lists = db.execute("SELECT * FROM taskslist").fetchall()

    return render_template("tasks_list/tasklists.html", lists = lists)



@taskslist_bp.route("/editname/<int:index>" , methods=["POST" , "GET"])
def edit_tasklist_name(index):

    edit_name_form = EditNameForm()

    if edit_name_form.validate_on_submit():

        new_name = edit_name_form.new_name.data

        # connecting to the database
        db = get_db()

        db.execute(f"UPDATE taskslist SET name = '{new_name}' WHERE id = '{index}' ")
            
        db.commit()

        return redirect(url_for('taskslist.task_lists'))

    return render_template("tasks_list/edit_name.html", form = edit_name_form)



@taskslist_bp.route("/deletetasklist/<int:index>")
def delete_tasklist(index):

    # connecting to the database
    db = get_db()

    db.execute(f"DELETE FROM taskslist WHERE id = '{index}' ")
            
    db.commit()

    return redirect(url_for("taskslist.task_lists"))



# @taskslist_bp.route("/createtasklist" , methods = ["GET","POST"])
# def create_tasklist():
#     if request.method == "GET":
#         return render_template("tasks_list/create_tasklist.html")
#     else:
        
#         time_created = datetime.datetime.now()
#         time_updated = datetime.datetime.now()
#         new_name=request.form["name"]
#         tasklists.update({'len(tasklists) +1':{'name': new_name,'last_updated':time_updated,'created_at':time_created}})
#         return redirect(url_for('task_lists'))