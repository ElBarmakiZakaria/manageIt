from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.form.get("user_email")
        password = request.form.get("user_password")

        the_user = User().check_logging(user_email)
        if the_user:
            if check_password_hash(the_user[0][3], password):
                flash('logged in successfully!', category='success')
                loggedin_user = User(the_user[0][0], the_user[0][1], the_user[0][2], the_user[0][3])
                login_user(loggedin_user, True)
                return redirect(url_for('views.dashboard'))
            else:
                flash('Incorect password, try again.', category='error')
        else:
            flash("Email does not exist.", category='error')


    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        email = request.form.get('user_email')
        password = request.form.get("user_password")

        print(f"{user_name}  {email}  {password}")
        is_user_exists = User().check_logging(email)
        if is_user_exists:
            flash("this email already exists!", category='error')
        else:
            User().add_user(Username=user_name, Email=email, Password=generate_password_hash(password, method='sha256'))
            the_user = User().check_logging(email)
            flash('Account is created succesfully!', category="success")
            loggedin_user = User(the_user[0][0], the_user[0][1], the_user[0][2], the_user[0][3])
            login_user(loggedin_user, True)
            
            return redirect(url_for('views.dashboard'))

    return render_template("register.html", user=current_user)
