from flask import Flask, session, request, render_template, redirect, flash
app = Flask(__name__)
app.secret_key = "PenguinsonIce"
import re, datetime, time
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/results', methods=['POST'])
def result():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d')
    if len(request.form['first_name']) < 1:
        flash("First name cannot be empty!")
        return redirect('/')
    else:
        session['first'] = request.form['first_name']
    
    if len(request.form['last_name']) < 1:
        flash("Last Name has to have at least one character")
        return redirect('/')
    else:
        session['last'] = request.form['last_name']

    if len(request.form['email']) < 1:
        flash("You will need to enter at least one digit for email address")
        return redirect('/')
    elif re.search('[0-9]', request.form['password']) is None:
        flash("your password should include at least one Number")
        return redirect('/')
    elif re.search('[A-Z]', request.form['password']) is None:
        flash("Your password should have one capital letter")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address")
        return redirect('/')
    else:
        session['email'] = request.form['email']

    if len(request.form['password']) < 8:
        flash("Your password must be at least 8 characters long")
        return redirect('/')
    elif request.form['password'] != request.form['confirm']:
        flash("Your passwords do not match")
        return redirect('/')
    
    if timestamp < request.form['birthday']:
        flash("That birthday is invalid")
        return redirect('/')
    else:
        session['birthday'] = request.form['birthday']
    
    flash("Thank you for submitting your information")
    
    return redirect('/')
    
app.run(debug=True)