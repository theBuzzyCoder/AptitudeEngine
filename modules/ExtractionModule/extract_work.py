#!/usr/bin/python3
import sys
import re
import os

import modules.ExtractionModule.extraction_abc as extraction_abc

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

import modules.TimeWork.ParseTimeWork


class TimeWorkExtractParameters(extraction_abc.ExtractParameters):
    """ A Extract parameter class which can extract parameters from time problems"""
    def extract_and_solve(self, question):
        d = ParseTimeWork.solve(question)
        if d:
            return d
        else:
            return {"error":"Could not solve this problem"}
