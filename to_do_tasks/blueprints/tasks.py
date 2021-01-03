from status import Status       
from priority import Priority
from flask import Flask, render_template, redirect, url_for, request, Blueprint
import sqlite3
import datetime
from functools import wraps
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TextAreaField

# define our blueprint
tasks_bp = Blueprint('tasks', __name__)

# task routing
# @tasks_bp.route("/tasks/<int:index>")
# def tasks_(index):
#     task_list = tasklists[index]["tasks"]
#     return render_template("tasks/tasks.html", tasks = tasks, task_list = task_list, general_index = index)



# @tasks_bp.route("/edittask/<int:index>/<int:general_index>", methods=["POST" , "GET"])
# def edit_task(index, general_index):

#     if request.method == "GET":
#         return render_template("tasks/edit_task.html")

#     else:
#         new_status= request.form["status"]
#         time_updated = datetime.datetime.now()
#         new_name = request.form["name"]
#         new_description = request.form["description"]        
#         tasks[index].update({'name': new_name , 'description' : new_description,'last_updated':time_updated , "status" : new_status})
#         return redirect(url_for('tasks_', index = general_index))

    



# @tasks_bp.route("/deletetask/<int:index>/<int:general_index>")
# def delete_task(index, general_index):
#     tasklists[general_index]["tasks"].remove(index)
#     tasks.pop(index)
#     return redirect(url_for("tasks_", index = general_index))

# @tasks_bp.route("/createtask/<int:index>", methods=["POST" , "GET"])
# def create_task(index):
#     if request.method == "GET":
#         return render_template("tasks/create_task.html" )
#     else:
#         priority = request.form["priority"] 
#         time_created = datetime.datetime.now()
#         time_updated = datetime.datetime.now()
#         new_name = request.form["name"]
#         new_description = request.form["description"]
#         tasklists[index]['tasks'].append('len(tasks) +1')
#         print(tasklists)
#         tasks.update({'len(tasks) +1':{'name': new_name,'last_updated':time_updated,'created_at':time_created ,'status':Status.NEW ,'priority':priority,'description':new_description}})
#         return redirect(url_for("tasks_",index = index))