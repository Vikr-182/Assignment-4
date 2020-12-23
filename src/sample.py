from flask import Flask, render_template, url_for,flash, redirect, request
#from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import UserMixin, login_user, logout_user

class ComputerSystemsQuestion(db.Model):

    __tablename__='computersystemsquestion'

    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(200),unique=True, nullable=False)
    answer=db.Column(db.String(100), unique=True, nullable=False)
    computersystemsmultiplechoices=db.relationship('ComputerSystemsMultipleChoice',backref= 'questionandmultiplechoice',lazy=True)

    def __repr__(self):
        return f"ComputerSystemsQuestion('{self.question}', '{self.answer}')"

class ComputerSystemsMultipleChoice(db.Model):

    __tablename__='computersystemsmultiplechoice'

    id=db.Column(db.Integer, primary_key=True)
    wrong_answer1=db.Column(db.String(100),unique=True, nullable=True)
    wrong_answer2=db.Column(db.String(100),unique=True, nullable=True)
    computersystemsquestion_id=db.Column(db.Integer, db.ForeignKey('computersystemsquestion.id'))

    def __repr__(self):
        return f"ComputerSystemsMultipleChoice('{self.wrong_answer1}', '{self.wrong_answer2}')"

    @app.route("/computersystems", methods=['GET','POST'])
    def computersystems():
        if request.method== 'POST':
            computersystems=ComputerSystemsQuestions.query.filter_by
            return
