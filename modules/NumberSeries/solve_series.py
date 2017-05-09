#!/usr/bin/python3
import diff_AP as dif
import diff_GP as dig
import alphabetic_series as als
common_diff = 0;
def ap(series,index):
	i=0;
	global common_diff
	if(index != 0 and index <= len(series)):
		n=index-1;
	elif(index>len(series)-1):
		n = len(series)-1;
	else:
		n=0;
	flag=0;
	if((index!=1 and index!=0)):
		d=round((series[1]-series[0]),2)
	else:
		d=round((series[len(series)-1]-series[len(series)-2]),2)
	while (i<=n and flag<=1):
		if(i!=n):
			if (round(series[i+1]-series[i],2)!=round(d,2)):
				return False
			else:
				i=i+1;
		else:
			i=index+1;
			n=len(series)-1;
			flag=flag+1;
	common_diff=d;
	if d == 0:
		return False
	if index >= len(series):
		ans = series[0] + (index) * d
		return ans
	if index == 0:
		series[0] = series[1] - d;
	else:
		series[index] = series[index - 1] + d
	return series[index]


def hp(series,index):
	i=0;
	global common_diff
	try:
		if(index!=1 and index!=0):
			d=(round((1/series[1]),2) - round((1/series[0]),2))
		else:
			d=(round((1/series[len(series)-1]),2) - round((1/series[len(series)-2]),2))
		common_diff=d;
		if d == 0:
			return False
		if index >= len(series):
			ans = 1 / (series[0] + (index) * d)
		elif index == 0:
			series[0] = 1 / (1/series[1] - d)
			ans = series[0]
		else:
			series[index] = (1 / (1 / series[index - 1] + d))
			ans = series[index]
		while i < len(series) - 1 :
			if (round((1/series[i+1]),2)-round((1/series[i]),2)) != round(d,2):
				return False;
			else:
				i=i+1;
		return ans
	except ZeroDivisionError:
		return False
	return False



def gp(series,index):
	i=0;
	global common_diff
	if(index != 0 and index <= len(series)):
		n=index-1;
	elif(index>len(series)-1):
		n = len(series)-1;
	else:
		n=0;
	flag=0;
	if(index!=0 and index!=1):
		r=series[1]/series[0];
	else:
		r=series[3]/series[2];
	if index >= len(series):
		while(i < len(series) - 1):
			if(series[i+1]/series[i]!=r):
				return False
			else:
				i = i + 1
		common_diff = r
		return (series[0]*pow(r,index))
	if index == 0:
		series[0] = series[1] / r
	else:
		series[index] = series[0] * pow(r,index)

	while(i < len(series) - 1):
		if(series[i+1]/series[i]!=r):
			return False
		else:
			i = i + 1
	common_diff = r
	return series[index]

def even_odd(series, index):
#finding nth missing number
	new_series = []
	if(index % 2 != 0):
		#TRUE when missing number is in odd positionS
		#indexing through odd position
		#index starts from odd position, starts from 1 to length of series
		for odd_index in range(1,len(series),2):
			#copying odd position value to new_series array
			new_series.append(series[odd_index])
			#checking whether odd_series is in AP or GP or HP
		if len(new_series) >= 3:
		    if ap(new_series, int(index / 2)):
			#if it is AP return the value of missing number
			    return 1
		    elif gp(new_series, int(index / 2)):
			#if it is GP return the value of missing number
			    return 2
		    elif hp(new_series, int(index / 2)):
			#if it is HP return the value of missing number
			    return 3
		    else:
			    return False
		else:
			return False
	else:
		#FALSE when missing number is in even position
		#indexing through even position
		#index starts from odd position, starts from 0 to length of series
		for even_index in range(0,len(series),2):
			#copying even position value to odd-series array
			new_series.append(series[even_index])

		if len(new_series) > 3:
		    if ap(new_series, int(index / 2)):
			#if it is AP return the value of missing number
			    return 1
		    elif gp(new_series, int(index / 2)):
			#if it is GP return the value of missing number
			    return 2
		    elif hp(new_series, int(index / 2)):
			#if it is HP return the value of missing number
			    return 3
		    else:
			    return False
		else:
			return False

def addap(series,type,index):
	dict = {'result':' ','steps':' ','type':'1','stype':'1'}
	list = []
	#ignore this call
	ap(series,index)
	global common_diff
	if(type == 0):
			list = ['Series is in Arithmetic Progression']
			if(index == 0):
				term = series[1] - common_diff
				list.append("Formula to find 1st term : a2 - d")
				list.append('a2 = '+str(series[1])+', d = '+ str(common_diff))
				list.append(''+str(series[1])+' - '+str(common_diff))
			else:
				term = series[0] + index * common_diff
				list.append("Formula to find  nth term is :a + (n - 1) d")
				list.append("a = "+str(series[0])+", d = "+ str(common_diff)+", n = "+str(index + 1))
				list.append(''+str(series[0])+' + '+'( '+str(index+1)+' ) * '+str(common_diff))
			list.append('nth term is '+str(term))
			dict['result'] = 'Ans is '+str(term)
	elif(type == 1):
			sum = ((index+1) * (2 * series[0] + index  * common_diff))/2
			list=['Series is in Arithmetic Progression',
			'Formula to find sum upto '+str(index + 1)+'th term is : S = n/2[2a + (n - 1)d]',
			'a = '+str(series[0])+', d = '+ str(common_diff)+', n = '+str(index + 1),
			'S = '+str(index+1)+'/2[2*'+str(series[0])+' + ('+str(index + 1)+' - 1)'+str(common_diff),
			'Sum = '+str(sum)]
			dict['result'] = 'Sum = '+str(sum)
	dict['steps'] = list
	return dict



def addgp(series,type,index):
	global common_diff
	dict = {'result':' ','steps':' ','type':'1','stype':'2'}
	list = []
	#ignore this call
	gp(series,index)
	if(type == 0):
			list = ['Series is in Geometric Progression']
			if(index == 0):
				term = series[1] / common_diff
				list.append('Formula to find nth term is = a2 / r')
				list.append('a2= '+str(series[1])+', r = '+ str(common_diff))
				list.append(''+str(series[1])+' / '+str(common_diff))
			else:
				term = series[0] * common_diff ** (index+1-1)
				list.append('Formula to find '+str(index + 1)+'th term is = a * r^(n - 1)')
				list.append('a = '+str(1/series[0])+', r = '+ str(common_diff)+', n = '+str(index + 1))
				list.append(''+str(series[0])+' * '+str(common_diff)+'^('+str(index+1)+' - 1)')
			list.append('nth term is '+ str(term))
			dict['result'] = 'Ans is '+ str(term)
	if(type == 1):
			sum = (series[0] * (1 - common_diff ** (index+1)))/(1 - common_diff)
			list = ['Series is in Harmonic Progression',
			'Formula to Sum upto '+str(index + 1)+'th term is : Sn = [ a (1 - r^n) ] / [ 1 - r ]',
			'a = '+str(series[0])+', r = '+ str(common_diff)+', n = '+str(index + 1),
			'[ '+str(series[0])+'( 1 - '+str(common_diff)+'^'+str(index+1)+' ) ] / [ 1 - '+str(common_diff)+' ]',
			'Sum is '+ str(sum)]
			dict['result'] = 'Sum is '+ str(sum)
	dict['steps'] = list
	return dict


def addhp(series,type,index):
	global common_diff
	dict = {'result':' ','steps':' ','type':'1','stype':'3'}
	list = []
	#ignore this call
	hp(series,index)
	if(type == 0):
			list = ['Series is in Harmonic Progression']
			if(index == 0):
				term = 1/(1/series[1] - common_diff)
				list.append('Formula to find '+str(index + 1)+'th term is : 1 / [a2 - d]')
				list.append('a2 = '+str(1/series[1])+', d = '+ str(common_diff))
				list.append('1 / ['+str(1/series[1])+' - '+str(common_diff)+']')
			else:
				term = 1/(1/series[0] + index * common_diff)
				list.append('Formula to find '+str(index + 1)+'th term is : 1 / [a + (n - 1) d]')
				list.append('a = '+str(1/series[0])+', d = '+ str(common_diff)+', n = '+str(index + 1))
				list.append('1 / ['+str(1/series[0])+' + '+'( '+str(index+1)+' ) * '+str(common_diff)+']')
			if(isinstance(term,float)):
				term_str ="1 /"+str(int(1/term))+" or "+str(term);
			else:
				term_str = str(term);
			list.append(''+str(index+1)+'th term is  = '+ term_str)
			dict['result'] = 'Ans is '+ term_str
	if(type == 1):
			# pending
			print ("yet to code");
	dict['steps'] = list
	return dict

def addeven_odd(series, type, index):
	newlist = ['Series in the form odd even numbered terms followed by a different pattern']
	new_series = []
	if(index % 2 != 0):
		#missing number is in even position
		newlist.append('Missing term is in the even position')
		for odd_index in range(1,len(series)-1,2):
			#copying even position value to new_series array
			new_series.append(series[odd_index])
	else:
		#missing number is in odd position
		newlist.append('Missing term is in the odd position')
		for even_index in range(0,len(series)-1,2):
			#copying odd position value to new_series array
			new_series.append(series[even_index])

	#storing from list to string
	prt= ''
	i=0
	for n in new_series:
		if(i != int(index/2)):
			prt += ' '+str(n)
		else:
			prt += ' _'
		i+=1


	newlist.append('New series is '+prt)

	if type == 1: #type = 1 series is in AP
		d = addap(new_series,0,int(index/2))
		d['type'] = '1'
		d['stype'] = '4'
	elif type == 2: #type = 2 series is in GP
		d = addgp(new_series,0,int(index/2))
		d['type'] = '1'
		d['stype'] = '5'
	elif type == 3: #type = 3 series is in HP
		d = addhp(new_series,0,int(index/2))
		d['type'] = '1'
		d['stype'] = '6'

	#updating dictionary with new steps
	d['steps'] = newlist + d['steps']
	return d

# function to find
def solveSeries(series,index,type):
	# type = 0, find nth;find missing number; type = 1, find the sum
	#index starts from 0
	alpha = False
	for i in series:
		if isinstance(i,str):
			if i.isalpha():
				alpha = True
				break
	if alpha:
		return als.checkAlpha(series,type,index)
	else:
		n = len(series)
		if(ap(series,index)):
			d = addap(series,type,index)
			if(n==4 and (index==1 or index==2)):
				if(not (round(series[index]-series[index-1],2)!=common_diff or round(series[index+1]-series[index],2)!=common_diff)):
					return d
			else:
				return d


				#print (sum);
		if(gp(series,index)):
			d = addgp(series,type,index)
			return d
		if(hp(series,index)):
			d = addhp(series,type,index)
			return d


		if len(series) > index:
			if index < len(series):
				series[index]='x'
			if dif.solveSeries(series,index,type):
				d = dif.solveSeries(series,index,type)
				return d



		if len(series) > index:
			if index < len(series):
				series[index]='x'
			if dig.solveSeries(series,index,type):
				d = dig.solveSeries(series,index,type)
				return d


		ty = even_odd(series,index)
		if ty == 1 or ty == 2 or ty == 3:
			d = addeven_odd(series,ty,index)
			return d
		else:
			return False
