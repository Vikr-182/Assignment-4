from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify
from flask import render_template

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Student(db.Model):
    rollnumber = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(128), unique = True)

    def _init_(self, name, email):
        self.name = name
        self.email = email

    def _repr_(self):
        return f"Student {self.name}"

class Course(db.Model):
    code = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True)

    def _init_(self, name):
        self.name = name


# Student Starts here

@app.route("/students/create", methods=['POST', 'GET'])
def addStudent():
    if request.method == 'GET':
        db.create_all()
        check_rollnumber = request.form['rollnumber']
        check_name = request.form['name']
        check_email = request.form['email']
        isPresent = db.session.query(db.session.query(Student).filter_by(rollnumber=check_rollnumber).exists()).scalar() \
             and db.session.query(db.session.query(Student).filter_by(email=check_email).exists()).scalar() \ 
                 and db.session.query(db.session.query(Student).filter_by(name=check_name).exists()).scalar()
        req = {'status': isPresent}
        return jsonify(req)
    else :
        name = request.form['name']
        email = request.form['email']
        db.create_all()
        new_student = Student(name, email)
        db.session.add(new_student)
        db.session.commit()
        isPresent = db.session.query(db.session.query(Student).filter_by(email=check_email).exists()).scalar() \
            and db.session.query(db.session.query(Student).filter_by(name=check_name).exists()).scalar()        
        state = {'status': isPresent}
        return jsonify(state)

@app.route('/students')
def retrieveStudents():
    db.create_all()
    allStudents = Student.query.all()
    students = []
    for student in allStudents:
        eachStudent = {}
        eachStudent['rollnumber'] = student.rollnumber
        eachStudent['name'] = student.name
        eachStudent['email'] = student.email
        students.append(eachStudent)
    req = {'students': students}
    return jsonify(req)

@app.route('/students/<rollnumber>', methods = ['GET', 'POST'])
def particularStudent(rollnumber):
    if request.method == 'GET':
        db.create_all()
        thisStudent = Student.query.filter(Student.rollnumber == rollnumber).first()
        student = {}
        student['rollnumber'] = thisStudent.rollnumber
        student['name'] = thisStudent.name
        student['email'] = thisStudent.email
        req = {'student': student}
        return jsonify(req)
    else :
        db.create_all()
        new_name = request.form['name']
        new_email = request.form['email']
        thisStudent = Student.query.filter(Student.rollnumber == rollnumber).update(dict(email=new_email, name=new_name))
        db.session.commit()
        checker = Student.query.filter(Student.rollnumber == rollnumber).first()
        state = {'updated': (checker.name == new_name and checker.email == new_email)}
        return jsonify(state)

@app.route('/students/delete', methods=['POST'])
def deleteStudent():
    to_delete_rollnumber = request.form['rollnumber']
    db.create_all()
    Student.query.filter(Student.rollnumber == to_delete_rollnumber).delete()
    db.session.commit()
    isStillPresent = db.session.query(db.exists().where(Student.rollnumber == to_delete_rollnumber)).scalar()
    state = {'status': not isStillPresent}
    return jsonify(state)

# Course Starts here


@app.route("/courses/create", methods=['POST', 'GET'])
def addCourse():
    if request.method == 'GET':
        db.create_all()
        check_code = request.form['code']
        check_name = request.form['name']
        isPresent = db.session.query(db.session.query(Course).filter_by(name=check_name).exists()).scalar() \
            and db.session.query(db.session.query(Course).filter_by(code=check_code).exists()).scalar()
        req = {'status': isPresent}
        return jsonify(req)
    else :
        name = request.form['name']
        db.create_all()
        new_course = Course(name)
        db.session.add(new_course)
        db.session.commit()
        isPresent = db.session.query(db.session.query(Course).filter_by(name=check_name).exists()).scalar()
        state = {'status': isPresent}
        return jsonify(state)

@app.route('/courses')
def retrieveCourses():
    db.create_all()
    allCourses = Course.query.all()
    courses = []
    for course in allCourses:
        eachCourse = {}
        eachCourse['code'] = course.code
        eachCourse['name'] = course.name
        courses.append(eachCourse)
    req = {'courses': courses}
    return jsonify(req)

@app.route('/courses/<code>', methods = ['GET', 'POST'])
def particularCourse(code):
    if request.method == 'GET':
        db.create_all()
        thisCourse = Course.query.filter(Course.code == code).first()
        course = {}
        course['code'] = thisCourse.code
        course['name'] = thisCourse.name
        req = {'course': course}
        return jsonify(req)
    else :
        db.create_all()
        new_name = request.form['name']
        thisCourse = Course.query.filter(Course.code == code).update(dict(name=new_name))
        db.session.commit()
        checker = Course.query.filter(Course.code == code).first()
        state = {'updated': (checker.name == new_name)}
        return jsonify(state)

@app.route('/courses/<code>/delete', methods=['POST'])
def deleteCourse(code):
    to_delete_code = code
    db.create_all()
    Course.query.filter(Course.code == to_delete_code).delete()
    db.session.commit()
    isStillPresent = db.session.query(db.exists().where(Course.code == to_delete_code)).scalar()
    state = {'status': not isStillPresent}
    return jsonify(state)

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)
