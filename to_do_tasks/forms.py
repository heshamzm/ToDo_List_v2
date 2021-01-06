from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TextAreaField, RadioField, SelectField, PasswordField

#Create edit WTForm
class EditTaskForm(FlaskForm):
    new_name = StringField("New Name: ", [validators.InputRequired()])
    new_description = TextAreaField("New Description: ", [validators.InputRequired()])
    status = RadioField('Status:', choices=['New','In progress','Done'])
    priority = RadioField('Priority:', choices=['Low','Medium','High'])
    submit = SubmitField("Edit Task")

#Create task WTForm
class CreateTaskForm(FlaskForm):
    new_name = StringField("New Name: ", [validators.InputRequired()])
    new_description = TextAreaField("New Description: ", [validators.InputRequired()])
    priority = RadioField('Priority:', choices=['Low','Medium','High'])
    submit = SubmitField("Create Task")



#Create edit task list WTForm
class EditNameForm(FlaskForm):
    new_name = StringField("New Name: ", [validators.InputRequired()])
    submit = SubmitField("Edit Name")

#Create create task list WTForm
class CreateTaskList(FlaskForm):
    name = StringField("Name : ", [validators.InputRequired()])
    submit = SubmitField("Create")



#Create login WTForm
class LoginForm(FlaskForm):
    username = StringField("Username : ", [validators.InputRequired()])
    password = PasswordField("Password : ", [validators.InputRequired()])
    submit = SubmitField("Log In")

#Create user WTForm
class AddUser(FlaskForm):
    username = StringField("Username : ", [validators.InputRequired()])
    password = PasswordField("Password : ", [validators.InputRequired()])
    first_name = StringField("First Name : ", [validators.InputRequired()])
    last_name = StringField("Last Name : ", [validators.InputRequired()])
    submit = SubmitField("Sign Up")
