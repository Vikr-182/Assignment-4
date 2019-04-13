from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify
    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rollnumber=db.Column(db.Integer, unique=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    
    def __init__(self, rollnumber, name, email):
        self.username = username
        self.email = email
        self.rollnumber = rollnumber
    
    def __repr__(self):
        return '<User %r>' % self.username

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(120), unique=True)

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.code

@app.route("/students/create", methods=["POST"])
def userAdd():
    rollnumber=request.form['rollnumber']
    user=request.form['username']
    email= request.form['email']
    db.create_all()
    new_person=User(rollnumber, user, email)
    db.session.add(new_person)
    print("newperson")
    db.session.commit()
    temp ={}
    temp['status']=(type(new_person)==User)
    return jsonify(temp)
    
@app.route("/students/<rollnumber>/")
def userFetch():
    db.create_all()
    allUsers=User.query.all()
    strf = {}
    for user in allUsers:
        strf['rollnumber'] = user.rollnumber
        strf['name'] = user.username
        strf['email'] = user.email
    return jsonify(strf)

@app.route("/students/delete/")
def userDelete():
    rollnumber=request.form['rollnumber']
    db.create_all()
    allUsers=User.query.all()
    for user in allUsers:
        if user.rollnumber == rollnumber:
            db.session.delete(user)
            db.session.commit()
    return
@app.route("/students/update/")
def update():
    rollnumber=request.form['rollnumber']
    username=request.form['username']
    email=request.form['email']
    db.create_all()
    allUsers=User.query.all()
    for user in allUsers:
        if user.rollnumber == rollnumber:
            user.username='newName'
            user.email='newEmail'
    return 

@app.route("/courses/create", methods=["POST"])
def CoursesAdd():
    code=request.form['code']
    name=request.form['name']
    db.create_all()
    new_person=User(code,name)
    db.session.add(new_person)
    db.session.commit()
    temp ={}
    temp['status']=(type(new_person)==Courses)
    return jsonify(temp)

@app.route("/courses/<code>/")
def coursesFetch():
    code=request.form['code']
    db.create_all()
    allUsers=Courses.query.all()
    strf = {}
    for user in allUsers:
        strf['code']=user.code
        strf['name']=user.name
    return jsonify(strf)

@app.route("/courses/delete/")
def coursesDelete():
    code=request.form['code']
    db.create_all()
    allUsers=Courses.query.all()
    for user in allUsers:
        if user.code == code:
            db.session.delete(user)
            db.session.commit()
    return

@app.route("/courses/update/")
def coursesupdate():
    code=request.form['rollnumber']
    name=request.form['username']
    db.create_all()
    allUsers=Courses.query.all()
    for user in allUsers:
        if user.code == code:
            user.name = "name"
    return 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

