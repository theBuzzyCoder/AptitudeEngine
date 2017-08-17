# -*- coding: utf-8 -*-
'''
Python Version: 3.6
Created By: AByteCoder
Last Edited By: theBuzzyCoder
Edited On: Aug 17, 2017
'''
import os
import json
import modules.AptitudeEngine as AptitudeEngine
import modules.question_analyser as question_analyser
import modules.MySqlDB.aptitude_engine_db as aptitude_engine_db
from flask import Flask, render_template, url_for, request

app = Flask(__name__)
ANALYSER = False
DATASET_LABELS = [
    "number_series", "relative_speed", "clock",
    "lcm", "TimeWork"
]
DATASET_LOCATION = os.path.abspath("modules/Dataset/jsons")
DATASET_FILES = [
    "numseries.json", "train.json", "clock.json",
    "lcm.json", "TimeWork.json"
]


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route('/')
def main():
    '''
    This loads index.html a Static Page.
    '''
    return render_template('index.html')


@app.route('/modules')
def get_modules():
    '''
    Gets the available modules
    '''
    aptitude_engine_db.connect()
    data = aptitude_engine_db.get_all_types()
    aptitude_engine_db.disconnect()
    for mod in data:
        filename = os.path.join("images", mod['image'])
        mod['image'] = url_for('static', filename=filename)
    return json.dumps(data)


@app.route('/solve', methods=['POST'])
def wrap():
    '''
    Solves and return the solution as well as
    the steps involved to solve the problem.
    '''
    question = request.form.get("question")
    status = AptitudeEngine.solve(ANALYSER, question)
    if status == -1:
        output_dict = dict(error='Invalid Question')
        return json.dumps(output_dict)
    elif not status:
        output_dict = dict(error="Oops! I can't solve it")
        return json.dumps(output_dict)
    elif 'error' in status:
        return json.dumps(status)
    else:
        aptitude_engine_db.connect()
        output_dict = {}
        output_dict['solution'] = status
        status['steps'] = list(status['steps'])
        status['type'], status['stype'] = aptitude_engine_db.get_type(
            int(status['type']),
            int(status['stype'])
        )
        output_dict['related'] = aptitude_engine_db.related_question(
            status['type'], status['stype']
        )
        aptitude_engine_db.disconnect()
    return json.dumps(output_dict)


@app.route('/questions/<category>')
def view_questions(category):
    '''
    Gives sample questions
    '''
    aptitude_engine_db.connect()
    data = aptitude_engine_db.view_questions(category)
    aptitude_engine_db.disconnect()
    return json.dumps(data)


@app.route('/feedback', methods=['POST'])
def feedback():
    '''
    Allows to retrieve feedback on the product
    '''
    data = request.form.get("data")
    data = json.loads(data)
    aptitude_engine_db.connect()
    aptitude_engine_db.feedback(data)
    aptitude_engine_db.disconnect()
    return "submitted"


if __name__ == '__main__':
    question_analyser.QuestionAnalyser(
        DATASET_LOCATION, DATASET_FILES, DATASET_LABELS
    )
    app.run('0.0.0.0', 8085, debug=True)
