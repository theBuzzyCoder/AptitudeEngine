#!/usr/bin/python3
import math

#returns the diffrence list
def newlist(series, index):
    diffrence_series = []
    for i in range(len(series) - 1):
        if (series[i] != 'x' and series[i + 1] != 'x'):
            val = series[i + 1] - series[i]
            diffrence_series.insert(i, val)
        else:
            diffrence_series.insert(i, 'x')
    return diffrence_series

#calculating r using a and any value in list
def find_r(diffrence_series):
    for i in range(len(diffrence_series) - 1 ):
        if diffrence_series[i + 1] != 'x':
            r = int(math.pow(diffrence_series[i + 1] / diffrence_series[0], 1 / (i + 1)))
            break
    return round(r,2)

#filling missing terms in list using a and r
def fill_terms(diffrence_series, r):
    for i in range(len(diffrence_series) - 1):
        if diffrence_series[i + 1] == 'x':
            #missing value contains x
            diffrence_series[i + 1] = int(diffrence_series[0] * math.pow(r, i + 1))
        else:
            if diffrence_series[i + 1] != int(diffrence_series[0] * math.pow(r, i + 1)):
                return False
    return diffrence_series

#finds 'a' of series if its missing
def find_a(diffrence_series):
    flag = 1
    #serching for two neighbouring values in series
    for i in range(len(diffrence_series)):
        if diffrence_series[i] != 'x':
            if flag == 1:
                term1 = diffrence_series[i]
                i1 = i
                flag = 2
            else:
                term2 = diffrence_series[i]
                i2 = i
                break
    #using two consecutive values in list finding a and r
    r = int(math.pow(term2 / term1, 1 / (i2 - i1)))
    a = int(term1 / math.pow(r, i1))
    return a


#fills the original series and checks if the original series is in diffrence GP
def fill_check_original_series(series, diffrence_series):
    if series[0] == 'x':
        series[0] = series[1] - diffrence_series[0]
    for i in range(len(series)):
        if series[i] == 'x':
            series[i] = series[i - 1] + diffrence_series[i - 1]
    #checking if difrence is in GP in original series
    for i in range(len(series) - 1):
        if round(series[i] + diffrence_series[i],6) != round(series[i + 1],6):
            return False
    return True

def solveSeries(series,index,type):
	d = {'result':' ','steps':' ','type':'1','stype':'11'}
	diffrence_series=newlist(series,index)
        #checking if first term in series is missing
	if diffrence_series[0] == 'x':
		a = find_a(diffrence_series)
		diffrence_series[0] = a
	r = find_r(diffrence_series)

        #filling missing terms in list using a and r
	diffrence_series = fill_terms(diffrence_series, r)
	if diffrence_series == False:
		return False

        #filling the original series using difrence series

	if fill_check_original_series(series, diffrence_series):
		dict = ["The diffrence of series is in GP, Diffrence series is "]
		dict.append(diffrence_series)
		dict.append("Therefore the missing term is")
		if index == 1:
			dict.append(" "+str(series[1])+" - "+str(diffrence_series[0]+" = "+series[1] - diffrence_series[0]))
			d["result"] = series[1] - diffrence_series[0]
		elif index == len(series) - 1 :
			dict.append(" "+str(series[len(series) - 2])+" + "+str(diffrence_series[len(diffrence_series) - 1])+" = "+str(series[len(series) -2] + diffrence_series[len(diffrence_series) - 1]))
			d["result"] = series[len(series) -2] + diffrence_series[len(diffrence_series) - 1]
		else:
			dict.append(" "+str(series[index + 1])+" - "+str(diffrence_series[index])+" = "+str(series[index]-diffrence_series[index - 1]))
			d["result"] = series[index + 1] - diffrence_series[index]
		d['steps'] = dict
		return d
	else:
		return {"error":"Could not solve the series"}
