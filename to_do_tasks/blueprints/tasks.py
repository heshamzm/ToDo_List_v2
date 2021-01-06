from flask import Flask, render_template, redirect, url_for, request, Blueprint
import sqlite3
import datetime
from functools import wraps
from to_do_tasks.db import get_db
from ..forms import EditTaskForm, CreateTaskForm
from .taskslist import login_required

#Define our blueprint
tasks_bp = Blueprint('tasks', __name__)

#Tasks routing
@tasks_bp.route("/tasks/<int:list_index>")
@login_required
def tasks_(list_index):

    #Get the DB connection
    db = get_db()

    tasklist = db.execute(f"SELECT * FROM taskslist WHERE id = {list_index}").fetchone()

    #Get tasks by tasks list id
    tasks = db.execute(f"SELECT * FROM tasks WHERE taskslist_id = {list_index}").fetchall()

    #Render the tasks template
    return render_template("tasks/tasks.html", tasklist = tasklist, tasks = tasks, list_index = list_index)


#Edit task routing
@tasks_bp.route("/edittask/<int:index>", methods=["POST" , "GET"])
@login_required
def edit_task(index):
    #Create instance from edit form 
    edit_task_form = EditTaskForm()

    if edit_task_form.validate_on_submit():

        new_name = edit_task_form.new_name.data
        new_description = edit_task_form.new_description.data
        status = edit_task_form.status.data
        priority = edit_task_form.priority.data
        db = get_db()
        
        #Get tasks list id from tasks table by tasks id
        task_list_id = db.execute("SELECT taskslist_id FROM tasks WHERE id LIKE ? " ,(index,)).fetchone()

        #Values update
        db.execute(f"UPDATE tasks SET name = '{new_name}',status = '{status}',priority = '{priority}' , last_updated = '{datetime.datetime.now()}', description = '{new_description}' WHERE id = '{index}' ")
            
        db.commit()

        return redirect(url_for('tasks.tasks_', list_index = task_list_id['taskslist_id']))

        
    return render_template("tasks/edit_task.html", form = edit_task_form)

    
#Delete task routing
@tasks_bp.route("/deletetask/<int:index>")
@login_required
def delete_task(index):

    db = get_db()

    task_list_id = db.execute("SELECT taskslist_id FROM tasks WHERE id LIKE ? " ,(index,)).fetchone()   
    
    #Deleye value from database
    db.execute(f"DELETE FROM tasks WHERE id = '{index}' ")
        
    db.commit()

    return redirect(url_for('tasks.tasks_' , list_index = task_list_id['taskslist_id']))


#Create task routing
@tasks_bp.route("/createtask/<int:index>", methods=["POST" , "GET"])
@login_required
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


#Sort task routing
@tasks_bp.route("/sorttask/<int:list_index>")
@login_required
def sort(list_index):

    #Connecting to the database
    db = get_db()

    tasklist = db.execute(f"SELECT * FROM taskslist WHERE id = {list_index}").fetchone()

    tasks = db.execute("""SELECT id, name, last_updated, created_at, status, priority, description 
FROM tasks
WHERE taskslist_id LIKE ? 
ORDER BY name ASC""",(list_index,)
    ).fetchall()

    return render_template("tasks/tasks.html", tasklist = tasklist, tasks = tasks, list_index = list_index)
