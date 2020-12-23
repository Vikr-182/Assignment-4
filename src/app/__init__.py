# Import flask and template operators
from flask import Flask, jsonify, render_template
from flask_cors import CORS

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
CORS(app)

# Configurations
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Import a module / component using its blueprint handler variable
from app.quiz.controllers import mod_ques

# Register blueprint(s)2
app.register_blueprint(mod_ques)

# Build the database:
db.create_all()


@app.route('/')
@app.route('/Introduction.html')
def intro():
    return render_template('Introduction.html')

@app.route('/Theory.html')
def theory():
        return render_template('Theory.html')

@app.route('/Objective.html')
def objective():
    return render_template('Objective.html')

@app.route('/Experiment.html')
def experiment():
    sentencesA=['EOS','I','YOU','CAN','HIM','NEAR','SIT']
    sentencesB=['EOS','YOU','BOOK','A','CAR','I','CAN', 'READ','IN','THE','PARK']
    sentencesC=['']
    return render_template('Experiment.html')

@app.route('/Quizzes.html')
def quiz():
    return render_template('Quizzes.html')

@app.route('/Procedure.html')
def procedure():
    return render_template('Procedure.html')


@app.route('/Further Readings.html')
def furtherReadings():
    return render_template('Further Readings.html')

@app.route('/Feedback.html')
def feedback():
    return render_template('Feedback.html')

@app.route('/Quiz_add.html')
def quizadd():
    return render_template('Quiz_add.html')

