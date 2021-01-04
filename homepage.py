from flask import Flask,render_template,flash,request,url_for,redirect
from content_management import Content
import os

TOPIC_DICT=Content()

app=Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/about.html')
def about():
    flash("FLASH TEST")
    return render_template('about.html',TOPIC_DICT=TOPIC_DICT)


@app.route('/info.html')
def info():
    return render_template('info.html')

@app.route('/register.html')
def register():
    return render_template('register.html') 

@app.route('/login.html',methods=['GET','POST'])
def login():
    error=None
    try:
        if request.method=="POST":
            attempted_username=request.form['username']
            attempted_password=request.form['password']

            if attempted_username=="admin" and attempted_password=="pass":
                return redirect(url_for("about"))
            else:
                error="INVALID CREDENTIALS"

        return render_template("login.html",error=error)
        

    except Exception as e:
        flash(e)
        return render_template("login.html",error=error)





if __name__ == "__main__":
    app.run(debug=True)
