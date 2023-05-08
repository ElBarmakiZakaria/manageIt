from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from .models import Tasks
from . import db


views = Blueprint('views', __name__)

@views.route('/Dashboard')
@login_required
def dashboard():
    #print(current_user.name)
    data = get_data()
    
    return render_template("Dashboard.html", user=current_user, data = data, lengt = len(data))


@views.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for("views.dashboard"))
    else:
        return render_template("home.html", user=current_user)
    

@views.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    #print(current_user.name)
    if request.method == 'POST':
            
        user_email = current_user.email
        Task_title = request.form.get("title")
        Task_description = request.form.get("description")
        Task_priority = request.form.get("priority")
        Task_status = request.form.get("status")
        Task_date = request.form.get("date")


        Tasks().add_task(user_email, Task_title, Task_description, Task_priority, Task_status, Task_date)
        return redirect(url_for('views.dashboard'))

    return redirect(url_for("views.dashboard"))





@views.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    #print(current_user.name)
    if request.method == 'POST':
            
        user_email = current_user.email
        id = request.form.get("id")
        Task_title = request.form.get("title")
        Task_description = request.form.get("description")
        Task_priority = request.form.get("priority")
        Task_status = request.form.get("status")
        Task_date = request.form.get("date")


        Tasks().update_task(id, Task_title, Task_description, Task_priority, Task_status, Task_date)
        return redirect(url_for('views.dashboard'))

    return redirect(url_for("views.dashboard"))


@views.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    #print(current_user.name)
    if request.method == 'POST':
            
        id = request.form.get("id")
        Tasks().delete_task(id)
        return redirect(url_for('views.dashboard'))

    return redirect(url_for("views.dashboard"))

def get_data():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Tasks WHERE User_email = %s', (current_user.email, ))
    data = cursor.fetchall()
    return data