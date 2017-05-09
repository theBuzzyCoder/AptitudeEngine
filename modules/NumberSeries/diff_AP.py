#!/usr/bin/python3

#returns a difrence list calculated from original list

def newlist(series, index):
    diffrence_series = []
    for i in range(len(series) - 1):
        if (series[i] != 'x' and series[i + 1] != 'x'):
            val = series[i + 1] - series[i]
            diffrence_series.insert(i, val)
        else:
            diffrence_series.insert(i, 'x')
    return diffrence_series

#returns the common diffrence of the new diffrence list
def common_diffrence(series):
    if series[0] != 'x' and series[1] != 'x':
        d = series[1] - series[0]
        return d
    if series[1] != 'x' and series[2] != 'x':
        d = int((series[2] - series[1]) / 2)
        return d
    if series[len(series) - 1] != 'x' and series[len(series) - 2] != 'x':
        d = int((series[len(series) - 1] - series[len(series) - 2]) / (len(series) - 1))
        return d

#fills the diffrence series using d
def fill_series(series, d):
    if series[0] == 'x':
        for i in range(len(series)):
            if (series[i + 1] != 'x' ):
                val = int((series[i + 1] - d) / (i + 1))
                series[0] = val
                break

    for i in range(len(series) ):
        if (series[i] == 'x' ):
            val = series[0] + (i) * d
            series[i] = val

    return series

#fills the original series using diffrence series and checks if diffrence is in AP
def fill_check_original_series(series, diffrence_series):
    if series[0] == 'x':
        series[0] = series[1] - diffrence_series[0]
    for i in range(len(series)):
        if series[i] == 'x':
            series[i] = series[i - 1] + diffrence_series[i - 1]
    for i in range(len(series) - 1):
        if series[i] + diffrence_series[i] != series[i + 1]:
            return False
    return True

def check(series,comm_diff):
	for i in range(len(series)):
		if series[i] != series[0] + ((i) * comm_diff):
			return False
	return True

def solveSeries(series,index,type):
	d = {'result':' ','steps':' ','type':'1','stype':'10'}
	diffrence_series=newlist(series,index)
	comm_diff = common_diffrence(series)
	diffrence_series=fill_series(diffrence_series,comm_diff)
	dict = ["The diffrence of series is in AP"]
	dict.append("Difference series is : "+str(diffrence_series)[1:-1]);
	dict.append("Therefore the missing term is")
	if index == 0:
		dict.append(" "+str(series[1])+" - "+str(diffrence_series[0])+" = "+str(series[1] - diffrence_series[0]))
		d["result"] = str(series[1] - diffrence_series[0])
	elif index == 1:
		dict.append(" "+str(series[0])+" - "+str(diffrence_series[0])+" = "+str(series[0] + diffrence_series[0]))
		d["result"] = str(series[0]+diffrence_series[0])
	elif index == len(series) :
		dict.append(" "+str(series[len(series) - 2])+" + "+str(diffrence_series[len(diffrence_series) - 1])+" = "+str(series[len(series) -2] + diffrence_series[len(diffrence_series) - 1]))
		d["result"] = str(series[len(series) -2] + diffrence_series[len(diffrence_series) - 1])
	else:
		dict.append(str(series[index - 1])+" - "+str(diffrence_series[index - 1])+" = "+str(series[index - 1] + diffrence_series[index - 1]))
		d["result"] = str(series[index - 1] + diffrence_series[index - 1])
	if check(diffrence_series,comm_diff):
		if fill_check_original_series(series,diffrence_series):
			d["steps"] = dict
			if type == 3:
				return int(d['result'])
			else:
				return d
		else:
			return {"error":"Could not solve the series"}
	else:
		return {"error":"Could not solve the series"}
