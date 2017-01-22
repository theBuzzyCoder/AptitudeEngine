#!/usr/bin/python3
def GeometricProgession(series,index):\
	#a = first term, r = common ratio
	a = series[0]
	r = series[1] / series[0]
	term = a * r ** (index-1)
	return term

ser = [2,6,18]
pos = 4
print("term = ",GeometricProgession(ser,pos))