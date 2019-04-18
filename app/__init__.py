from flask import Flask,render_template
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify
from flask import url_for
    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
   


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

@app.route("/Further Readings.html")
def references():
    return render_template("Further Readings.html")

@app.route("/Quizzes.html")
def quizzes():
    return render_template("Quizzes.html")

@app.route("/Feedback.html")
def feedback():
    return render_template("Feedback.html")

if __name__ == "__main__":
    app.run(debug=True)
