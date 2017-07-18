from flask import Flask, render_template, request , redirect, flash
app = Flask(__name__)
app.secret_key="key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods=['POST'])
def register():
    fname=request.form['first_name']
    if len(fname)>1 and fname.isalpha():
        print fname
    elif len(fname)<1:
        flash("Error, First Name cannot be blank")
        return redirect("/")
    else:
        flash("Error, First Name cannot contain numbers")
        return redirect('/')

    lname=request.form['last_name']
    if len(lname)>1 and lname.isalpha():
        print lname
    elif len(lname)<1:
        flash("Error, Last Name cannot be blank")
        return redirect("/")
    else:
        flash("Error, Last Name cannot contain numbers")
        return redirect('/')

    password=request.form['password']
    confirm_password=request.form['confirm_password']
    if password == confirm_password:
        if len(password)<8:
            flash("Error, Password must contain atleast 8 characters")
            return redirect("/")
    else:
        flash("Error, password and confirm password must match")
        return redirect("/")

    flash("Success, Thanks")
    return redirect("/")





app.run(debug=True)
