#!/usr/bin/python3
import sys,json
sys.path.append('./modules')
sys.path.append('./modules/MySqlDB')
import AptitudeEngine
import question_analyser as q
import aptitude_engine_db as ae
from flask import Flask, render_template,url_for,request

app = Flask(__name__)
analyser = False
dataset_labels = ["number_series","relative_speed","clock","lcm","TimeWork"]
dataset_location ="/home/ashish/AptitudeEngine/AptitudeEngine/modules/Dataset/jsons"
dataset_files = ["numseries.json","train.json","clock.json","lcm.json","TimeWork.json"]

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
  return render_template('index.html')
@app.route('/modules')
def get_modules():
    ae.connect()
    data = ae.get_all_types()
    for mod in data:
        mod['image'] = url_for('static',filename = "images/" + mod['image'])
    return json.dumps(data)
    ae.disconnect()

@app.route('/solve',methods = ['POST'])
def wrap():
    question = request.form.get("question")
    dict = AptitudeEngine.solve(analyser,question)
    if dict == -1:
        dict = {"error":"Invalid Question"}
        return json.dumps(dict)
    elif not dict:
        dict = {"error":"Oops! I can't solve it"}
        return json.dumps(dict)
    elif 'error' in dict:
        return json.dumps(dict)
    else:
        ae.connect()
        d = {}
        d['solution'] = dict
        dict['steps'] = list(dict['steps'])
        dict['type'],dict['stype'] = ae.get_type(int(dict['type']),int(dict['stype']))
        d['related'] = ae.related_question(dict['type'],dict['stype'])
        return json.dumps(d)
        ae.disconnect()
@app.route('/questions/<category>')
def view_questions(category):
    ae.connect()
    data = ae.view_questions(category)
    ae.disconnect()
    return json.dumps(data)
@app.route('/feedback',methods = ['POST'])
def feedback():
    data = request.form.get("data")
    data = json.loads(data)
    ae.connect()
    ae.feedback(data)
    ae.disconnect()
    return "submitted"

if __name__ == '__main__':
    analyser = q.QuestionAnalyser(dataset_location,dataset_files,dataset_labels)
    app.run('0.0.0.0',8085,debug=True)
