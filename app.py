from flask import Flask,render_template
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify
from flask import url_for
    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
   
class Quizzes(db.Model):
  
    __tablename__='contextfree-grammer-question'

    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(200),unique=True, nullable=False)
    answer=db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self,question,answer):
        self.question = question
        self.answer = answer
    
    def __repr__(self):
        return '<User %r>' % self.username

class Quizzesmcq(db.Model):

    __tablename__='contextfree-grammer-question'
    wrong_answer1=db.Column(db.String(100),unique=True, nullable=True)
    wrong_answer2=db.Column(db.String(100),unique=True, nullable=True)
    computersystemsquestion_id=db.Column(db.Integer, db.ForeignKey('context-free-grammer-question.id'))


@app.route("/")
def intro():
    return render_template("index.html")

@app.route("/Introduction.html")
def introduction():
    return render_template("Introduction.html")

@app.route("/Theory.html")
def thoery():
    return render_template("Theory.html")

@app.route("/Objective.html")
def objective():
    return render_template("Objective.html")

@app.route("/Experiment.html")
def experiment():
    return render_template("Experiment.html")

@app.route("/Procedure.html")
def procedure():
    return render_template("Procedure.html")

@app.route("/References.html")
def references():
    return render_template("References.html")

@app.route("/Quizzes.html")
def quizzes():
    return render_template("Quizzes.html")

@app.route("/Feedback.html")
def feedback():
    return render_template("Feedback.html")

if __name__ == "__main__":
    app.run(debug=True)
