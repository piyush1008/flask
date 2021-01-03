from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/info.html')
def info():
    return render_template('info.html')

@app.route('/register.html')
def register():
    return render_template('register.html')




if __name__ == "__main__":
    app.run(debug=True)
