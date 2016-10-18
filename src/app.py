from flask import Flask
from flask import render_template
from flask import request
from flask import session

from src.common.database import Database
from src.models.user import User

app = Flask(__name__)
app.secret_key = "1234"

@app.route('/')
def hello_method():
    return render_template("login.html")

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    print str(email) + "  " + str(password)

    if User.login_valid(email, password):
        User.login(email)

    return render_template("profile.html", email=session['email'])

if __name__=='__main__':
    app.run(port=4999, debug=True)



