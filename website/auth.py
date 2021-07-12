from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods = ['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return('<p>Logout</p>')

@auth.route('/sign-up',methods = ['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        passwor1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len (email) < 4:
            flash('Email must be larger than 3 character',category='error')
        elif len (firstName) <2:
            flash('The name must be larger than 1 character',category='error')
        elif passwor1 != passwor2:
            flash("Password Dont/'t match",category='error')
        elif len(passwor1) < 7:
            flash('Password must be at least 7 characters.',category='error')
        else:
            #add user to the database
            flash('Account created!',category='success')

    return render_template('sign_up.html')