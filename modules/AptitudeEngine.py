#!/usr/bin/python3
import sys
import question_analyser as q
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), './ExtractionModule'))
sys.path.append(os.path.join(os.path.dirname(__file__), './MySqlDB'))
import extract_numbers
import extract_train
import extract_clock
import extract_lcm
import extract_work
#used to format the solution dictionary
import aptitude_engine_db as ae
dataset_labels = ["number_series","relative_speed","clock","lcm","TimeWork"]
dataset_location ="/home/ashish/AptitudeEngine/AptitudeEngine/modules/Dataset/jsons"
dataset_files = ["numseries.json","train.json","clock.json","lcm.json","TimeWork.json"]
extract_parameters = {}
extract_parameters['number_series'] = extract_numbers.NumbersExtractParameters();
extract_parameters['relative_speed'] = extract_train.TrainsExtractParameters();
extract_parameters['clock'] = extract_clock.ClockExtractParameters();
extract_parameters['lcm'] = extract_lcm.LCMExtractParameters();
extract_parameters['TimeWork'] = extract_work.TimeWorkExtractParameters();
def format_solution(sol_dict):
    if not sol_dict:
        print("The above problem is not supported")
        sys.exit(0)
    print(str(sol_dict['result']))
    steps = sol_dict['steps']
    for i in range(len(steps)):
        print("Step"+str(i+1)+" : "+str(steps[i]))

total_count = 0
count = 0
def batch_process():
    global total_count,count
    analyser = q.QuestionAnalyser(dataset_location,dataset_files,dataset_labels)
    analyser.train()
    ae.connect()
    for file in dataset_files:
        with open(dataset_location+"/"+file,'r') as f:
            questions = json.load(f)
            total_count = total_count + len(questions)
            for question in questions:
                solve(analyser,question)
    ae.disconnect()
    print("Total records %d" %(total_count))
    print("Successfull records %d" %(count))
    print("Acuuracy %.2f"%(count / total_count * 100))

def solve(analyser,question):
    global count
    label = analyser.predict(question)
    ae.connect()
    try:
            output = extract_parameters[label].extract_and_solve(question)
            if type(output) == dict:
                if not 'error' in output:
                        count = count + 1
                        id = ae.check_question(question)
                        if id == False:
                            output['id'] = ae.insert_question(question,output)
                        else:
                             output['id'] = id

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        output = {"error": "Oops! I can't solve it"}
    ae.disconnect()
    return output

def main():
    print("Aptitude Engine v0.5 beta")
    print("Works for AP,GP,HP, Difference in AP,GP,HP and even odd relations")
    question = input("Question:")
    analyser = q.QuestionAnalyser(dataset_location,dataset_files,dataset_labels)
    solve(analyser,question)

if __name__ == '__main__':
    analyser = q.QuestionAnalyser(dataset_location,dataset_files,dataset_labels)
    analyser.train()
    batch_process()
