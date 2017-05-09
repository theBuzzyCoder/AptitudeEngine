#!/usr/bin/python
# Written by Abytecoder
import sys
sys.path.append('../')
import AptitudeEngine
import tsd
objec1  = {'name':'Police','length':0,'l-unit':'m','speed':20,'s-unit':'m'}
objec2  = {'name':'Thief','length':0,'l-unit':'m','speed':10,'s-unit':'m'}
output ={}
output['unit'] = "k"
output['what'] = "time"
given = {'distance':100,'unit':'k'}
objec2  = {'name':'Thief','length':0,'l-unit':'m','speed':10,'s-unit':'m'}
AptitudeEngine.format_solution(tsd.relative_speed(objec1,objec2,given,output,False))
