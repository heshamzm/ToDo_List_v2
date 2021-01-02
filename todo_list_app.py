# from status import Status       # Remember to import status and priority from the provided files
# from priority import Priority
from status import Status       # Remember to import status and priority from the provided files
from priority import Priority
from flask import Flask, render_template, redirect, url_for, request
import time
import datetime

app = Flask(__name__)

# task lists

tasklists = {
    1: {
        "name": "Python list",
        "last_updated": "2012-04-23 18:25:43.511000",
        "created_at": "2012-04-23 18:25:43.511000",
        "tasks": [1,2,3]
        },
    2: {
        "name": "Home list",
        "last_updated": "2012-04-23 18:25:43.511000",
        "created_at": "2012-04-23 18:25:43.511000",
        "tasks": [4,5]
    }
}

# tasks

tasks = {
    1: {
        "name": "learn flask blueprints",
        "last_updated": "2012-04-23 18:25:43.511000",
        "created_at": "2012-04-23 18:25:43.511000",
        "status": Status.DONE,
        "priority": Priority.HIGH,
        "description": "Etiam"
    },
    2: {
        "name": "learn Python enums",
        "last_updated": "2012-04-23 18:25:43.511000",
        "created_at": "2012-04-23 18:25:43.511000",
        "status": Status.IN_PROGRESS,
        "priority": Priority.MEDIUM,
        "description": "hello"

    },
    3:  {
        "name": "revise OOP concepts",
        "last_updated": "2012-04-23 18:25:43.511000",
        "created_at": "2012-04-23 18:25:43.511000",
        "status": Status.DONE,
        "priority": Priority.HIGH,
        "description": "Ut "
    },
    4:  {
        "name": "clean keyboard",
        "last_updated": "2012-04-23 18:25:43.511000",
        "created_at": "2012-04-23 18:25:43.511000",
        "status": Status.DONE,
        "priority": Priority.HIGH,
        "description": "Donec"
    },
    5:  {
        "name": "water plants",
        "last_updated": "2012-04-23 18:25:43.511000",
        "created_at": "2012-04-23 18:25:43.511000",
        "status": Status.DONE,
        "priority": Priority.HIGH,
        "description": "Nam "
    }
      
    
}

# tasklist routing
@app.route("/")
def task_lists():
    return render_template("tasklists.html", tasklists = tasklists)

@app.route("/editname/<int:index>" , methods=["POST" , "GET"])
def edit_tasklist_name(index):
    if request.method == "GET":
        return render_template("edit_name.html")

    else:
        new_name=request.form["name"]
        time_updated = datetime.datetime.now()
        tasklists[index].update({'name': new_name, 'last_updated':time_updated})
        return redirect(url_for('task_lists'))



@app.route("/deletetasklist/<int:index>")
def delete_tasklist(index):
    tasklists.pop(index)
    return redirect(url_for("task_lists"))



@app.route("/createtasklist" , methods = ["GET","POST"])
def create_tasklist():
    if request.method == "GET":
        return render_template("create_tasklist.html")
    else:
        
        time_created = datetime.datetime.now()
        time_updated = datetime.datetime.now()
        new_name=request.form["name"]
        tasklists.update({'len(tasklists) +1':{'name': new_name,'last_updated':time_updated,'created_at':time_created}})
        return redirect(url_for('task_lists'))


# task routing
@app.route("/tasks/<int:index>")
def tasks_(index):
    task_list = tasklists[index]["tasks"]
    return render_template("tasks.html", tasks = tasks, task_list = task_list, general_index = index)



@app.route("/edittask/<int:index>/<int:general_index>", methods=["POST" , "GET"])
def edit_task(index, general_index):

    if request.method == "GET":
        return render_template("edit_task.html")

    else:
        new_status= request.form["status"]
        time_updated = datetime.datetime.now()
        new_name = request.form["name"]
        new_description = request.form["description"]        
        tasks[index].update({'name': new_name , 'description' : new_description,'last_updated':time_updated , "status" : new_status})
        return redirect(url_for('tasks_', index = general_index))

    



@app.route("/deletetask/<int:index>/<int:general_index>")
def delete_task(index, general_index):
    tasklists[general_index]["tasks"].remove(index)
    tasks.pop(index)
    return redirect(url_for("tasks_", index = general_index))

@app.route("/createtask/<int:index>", methods=["POST" , "GET"])
def create_task(index):
    if request.method == "GET":
        return render_template("create_task.html" )
    else:
        priority = request.form["priority"] 
        time_created = datetime.datetime.now()
        time_updated = datetime.datetime.now()
        new_name = request.form["name"]
        new_description = request.form["description"]
        tasklists[index]['tasks'].append('len(tasks) +1')
        print(tasklists)
        tasks.update({'len(tasks) +1':{'name': new_name,'last_updated':time_updated,'created_at':time_created ,'status':Status.NEW ,'priority':priority,'description':new_description}})
        return redirect(url_for("tasks_",index = index))
    



if __name__ == "__main__":
    app.run(debug=True)