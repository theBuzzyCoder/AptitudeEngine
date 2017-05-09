#!/usr/bin/python3
import question_analyser

location = "./Dataset/jsons"
filenames = ["timespeed1.json","timespeed2.json","direc.json"]
labels = ["time","train","direction"]
ques = question_analyser.QuestionAnalyser(location,filenames,labels)
ques.train()
