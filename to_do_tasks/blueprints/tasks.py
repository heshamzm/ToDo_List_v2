# from status import Status       
# from priority import Priority
from flask import Flask, render_template, redirect, url_for, request, Blueprint
import sqlite3
import datetime
from functools import wraps
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TextAreaField,RadioField
from to_do_tasks.db import get_db

# define our blueprint
tasks_bp = Blueprint('tasks', __name__)

class EditTaskForm(FlaskForm):
    new_name = StringField("New Name: ", [validators.InputRequired()])
    new_description = TextAreaField("New Description: ", [validators.InputRequired()])
    status = RadioField('Status:', choices=['New','In progress','Done'])
    priority = RadioField('Priority:', choices=['Low','Medium','High'])
    submit = SubmitField("Edit Task")

class CreateTaskForm(FlaskForm):
    new_name = StringField("New Name: ", [validators.InputRequired()])
    new_description = TextAreaField("New Description: ", [validators.InputRequired()])
    priority = RadioField('Priority:', choices=['Low','Medium','High'])
    submit = SubmitField("Create Task")

# task routing
@tasks_bp.route("/tasks/<int:list_index>")
def tasks_(list_index):

    db = get_db()
    tasks = db.execute(f"SELECT * FROM tasks WHERE taskslist_id = {list_index}").fetchall()


    return render_template("tasks/tasks.html", tasks = tasks, list_index = list_index)



@tasks_bp.route("/edittask/<int:index>", methods=["POST" , "GET"])
def edit_task(index):

    edit_task_form = EditTaskForm()

    if edit_task_form.validate_on_submit():

        new_name = edit_task_form.new_name.data
        new_description = edit_task_form.new_description.data
        status = edit_task_form.status.data
        priority = edit_task_form.priority.data
        # connecting to the database
        db = get_db()

        # when return to view we have to till him which tasklist we are in.
        task_list_id = db.execute("SELECT taskslist_id FROM tasks WHERE id LIKE ? " ,(index,)).fetchone()

        db.execute(f"UPDATE tasks SET name = '{new_name}',status = '{status}',priority = '{priority}' , last_updated = '{datetime.datetime.now()}', description = '{new_description}' WHERE id = '{index}' ")
            
        db.commit()

        return redirect(url_for('tasks.tasks_', list_index = task_list_id['taskslist_id']))

        
    return render_template("tasks/edit_task.html", form = edit_task_form)

    



@tasks_bp.route("/deletetask/<int:index>")
def delete_task(index):

    db = get_db()

    task_list_id = db.execute("SELECT taskslist_id FROM tasks WHERE id LIKE ? " ,(index,)).fetchone()   
    db.execute(f"DELETE FROM tasks WHERE id = '{index}' ")
    print(task_list_id)     
    db.commit()

    return redirect(url_for('tasks.tasks_' , list_index = task_list_id['taskslist_id']))
    #https://stackoverflow.com/questions/53126234/why-does-a-database-query-in-python-not-return-an-integer-value




@tasks_bp.route("/createtask/<int:index>", methods=["POST" , "GET"])
def create_task(index):
    
    create_task = CreateTaskForm()
    if create_task.validate_on_submit():

        new_name = create_task.new_name.data
        new_description = create_task.new_description.data
        priority = create_task.priority.data

        # connecting to the database
        db = get_db()

        db.execute("INSERT INTO tasks (name,status,priority,description,taskslist_id) VALUES (?,?,?,?,?);" , (new_name,"New",priority,new_description,index,))
            
        db.commit()
          
        return redirect(url_for("tasks.tasks_",list_index = index))
    return render_template("tasks/create_task.html", form = create_task)