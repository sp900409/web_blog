from flask import Flask
from flask import render_template
from flask import request
from flask import session

from src.common.database import Database
from src.models.user import User

app = Flask(__name__)
app.secret_key = "1234"

@app.route('/')
def home_template():
    return render_template('home.html')


@app.route('/login')
def hello_method():
    return render_template("login.html")


@app.route('/register')
def register_method():
    return render_template("register.html")

@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    if User.login_valid(email, password):
        User.login(email)
        session['email'] = email
        print "session set to: " + email
    else:
        session['email'] = None
    return render_template("profile.html", email=session['email'])


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']
    User.register(email, password)
    return render_template("profile.html", email=session['email'])

@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def user_blogs(user_id=None):
    print "user_id is " + str(user_id) + "session[email] is: " + session['email']
    if user_id is not None:
        user = User.get_by_id()
    else:
        print "Getting User class by session email!!!"
        user = User.get_by_email(session['email'])

    blogs = user.get_blogs()
    return render_template("user_blogs.html", blogs = blogs, email=user.email)



if __name__=='__main__':
    app.run(port=4989, debug=True)
