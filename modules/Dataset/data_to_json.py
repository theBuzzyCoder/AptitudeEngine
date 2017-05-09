#!/usr/bin/python3
import json
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]
for f_name in onlyfiles:
    if f_name[-4:] == ".txt":
        with open(f_name,'r') as file:
            uques = file.read()
            questions = uques.split('\n')
            for i in range(len(questions)):
                if questions[i] == "":
                    del questions[i]
            with open(f_name[:-4]+".json",'w') as out_file:
                out_file.write(json.dumps(questions))
