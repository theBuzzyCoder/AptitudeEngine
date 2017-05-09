#!/usr/bin/python3
import nltk
import extraction_abc
import sys
import re
import os
from nltk.tokenize import sent_tokenize,word_tokenize

sys.path.append(os.path.join(os.path.dirname(__file__), '../TimeWork'))
import ParseTimeWork
class TimeWorkExtractParameters(extraction_abc.ExtractParameters):
    """ A Extract parameter class which can extract parameters from time problems"""
    def extract_and_solve(self, question):
        d = ParseTimeWork.solve(question)
        if d:
            return d
        else:
            return {"error":"Could not solve this problem"}
