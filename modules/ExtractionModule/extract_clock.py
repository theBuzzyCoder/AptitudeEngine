#!/usr/bin/python3
import nltk
import extraction_abc
import sys
import re
import os
from nltk.tokenize import sent_tokenize,word_tokenize

sys.path.append(os.path.join(os.path.dirname(__file__), '../Clock'))
import clock
class ClockExtractParameters(extraction_abc.ExtractParameters):
    """ A Extract parameter class which can extract parameters from clock problems"""

    def extract_and_solve(self, question):
        error = {"error":"Invalid time in question","type":2}
        question = question.lower()
        sentences = sent_tokenize(question)
        words = [w for sen in sentences for w in word_tokenize(sen)]
        hour = 0
        minute = 0
        match = re.search(r".* (\d+) and \d+.*",question,re.I|re.M)
        if match:
            #together ,seperate
            start = int(match.group(1))
            if "straight" in words or "opposite" in words:
                format = 2
            else:
                format = 1
            hour = int(match.group(1))
            if hour < 1 or hour > 12:
                return error
            param = {"from":hour,"type":format}
            return clock.calculate_angle(param)
        else:
            if "angle" in words :
                format = 1
                hour = "hour" in words and "hand" in words
                minute = "minute" in words and "hand" in words
                if hour and minute:
                    format = 1
                else:
                    if hour:
                        format = 2
                    elif minute:
                        format = 3
                match = re.search(r".* (\d+)(\.|:|-| )(\d+).*",question,re.I|re.M)
                hour = 0
                minute = 0
                if match:
                    hour = int(match.group(1))
                    minute = int(match.group(3))
                    if hour < 1 or hour > 12 or minute < 0 or minute > 60:
                        return error
                else:
                    match = re.search(r".* (\d+) minutes (past|to) (\d+).*",question,re.I|re.M)
                    if match:
                        if match.group(2) == "past":
                            hour = int(match.group(3))
                            minute = int(match.group(1))
                            if hour < 1 or hour > 12 or minute < 0 or minute > 60:
                                error
                        else:
                            hour = int(match.group(3))
                            if hour == 1:
                                hour = 12
                                minutes = 60 - int(match.group(1))
                                if hour < 1 or hour > 12 or minute < 0 or minute > 60:
                                    return error
                            else:
                                hour = hour - 1
                                minutes = 60 - int(match.group(1))
                                if hour < 1 or hour > 12 or minute < 0 or minute > 60:
                                    return error

                    else:
                        match = re.search(r".*(\d+) o'clock.*",question,re.I|re.M)
                        if match:
                            hour = int(match.group(1))
                            if hour < 1 or hour > 12 or minute < 0 or minute > 60:
                                return {"error":"Invalid time in question","type":2}
            param = {'hour':hour,'min':minute,'type':format}
            return clock.calculate_angle(param)
