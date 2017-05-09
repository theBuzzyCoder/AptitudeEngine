#!/usr/bin/python3
import extraction_abc
import sys
import re
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../NumberSeries'))
import solve_series as s
class NumbersExtractParameters(extraction_abc.ExtractParameters):
    """ A Extract parameter class which can extract parameters from number series problems"""

    def extract_and_solve(self, question):
        find_pos = -1
        tp = 0
        if re.search(r" sum ",question,re.I|re.M):
            tp = 1
        #extract the part which contains series 1,2,3,_,5,.....
        matchObj = re.search(r"(((\-?\d+|_|\-|\-?\d+\/\d+|\-?\d+\.\d+|[a-zA-Z]|-?\(\d+\/\d+\))\,)+)",question,re.I|re.M)
        if matchObj:
            #series found
            series = matchObj.group(1);
            series_list = series.split(',')
            series_list = series_list[:len(series_list)-1]
            for i in range(len(series_list)):
                if series_list[i] == '-' or series_list[i] == '_':
                    #position of - or _ if present
                    #since last item contains ...
                     find_pos = i
                else:
                    if not(series_list[i].isalpha()):
                        series_list[i] = eval(series_list[i])
            if find_pos != -1:
                odict = s.solveSeries(series_list,find_pos,tp)
            else:
                #find the position in other possible ways
                #check if they have asked the term to find in question
                matchObj = re.search(r"(\d+)(st|nd|rd|th) term",question)
                #position for tn present like 1st term,2nd term ,3rd term ,4th term extract
                if matchObj:
                    #position found
                    find_pos = int(matchObj.group(1))-1
                    odict = s.solveSeries(series_list,find_pos,tp)
                else:
                    # find the next term
                    find_pos = len(series_list)
                    try:
                        odict = s.solveSeries(series_list,find_pos,tp)
                        print(odict)
                    except:
                        print("Error in solve series")
            return odict
