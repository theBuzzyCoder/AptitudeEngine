#!/usr/bin/python3

def lcm(x, y):
	if x > y:
		greater = x
	else:
		greater = y

	while(True):
		if((greater % x == 0) and (greater % y == 0)):
			lcm = greater
			break
		greater += 1

	return lcm

def sol_prob(Work,Value,SubValue1,SubValue2,ToFind):
	steps = []
	Efficiency = {'A':' ','B':' ','C':'N','AB':' ','BC':'N','AC':'N','ABC':'N'}
	#if only two persons involved and A,B is known
	if Work['A'] != '-' and Work['B'] != '-' and Work['C'] == 'N':
		TotalWork = lcm(Work['A'] , Work['B'])
		steps.append("TotalWork = LCM("+str(Work['A'])+','+str(Work['B'])+")")
		steps.append(" = "+str(TotalWork))
		steps.append("Find the efficiency of A, B and AB using the formula TotalWork/Number of days taken")
		Efficiency['A'] = TotalWork / Work['A']
		Efficiency['B'] = TotalWork / Work['B']
		Efficiency['AB'] = Efficiency['A'] + Efficiency['B']
		steps.append("Efficiency of A "+str(Efficiency['A']))
		steps.append("Efficiency of B "+str(Efficiency['B']))
		steps.append("Efficiency of AB together (A + B)"+str(Efficiency['AB']))

    #if only two persons involved and A,AB is known
	elif Work['A'] != '-' and Work['AB'] != '-' and Work['C'] == 'N':
		TotalWork = lcm(Work['A'] , Work['AB'])
		steps.append("TotalWork = LCM("+str(Work['A'])+','+str(Work['AB'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['A'] = TotalWork / Work['A']
		Efficiency['AB'] = TotalWork / Work['AB']
		Efficiency['B'] = Efficiency['AB'] - Efficiency['A']
		steps.append("Find the efficiency of A, B and AB using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of A "+str(Efficiency['A']))
		steps.append("Efficiency of B (AB - A) "+str(Efficiency['B']))
		steps.append("Efficiency of AB together "+str(Efficiency['AB']))
	#if only two persons involved and B,AB is known
	elif Work['B'] != '-' and Work['AB'] != '-' and Work['C'] == 'N':
		TotalWork = lcm(Work['B'] , Work['AB'])
		steps.append("TotalWork = LCM("+str(Work['B'])+','+str(Work['AB'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['B'] = TotalWork / Work['B']
		Efficiency['AB'] = TotalWork / Work['AB']
		Efficiency['A'] = Efficiency['AB'] - Efficiency['B']
		steps.append("Find the efficiency of A, B and AB using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of A (AB - B)"+str(Efficiency['A']))
		steps.append("Efficiency of B "+str(Efficiency['B']))
		steps.append("Efficiency of AB together "+str(Efficiency['AB']))

    #if 3 persons are involved and A,B,C is known
	elif Work['A'] != '-' and Work['B'] != '-' and Work['C'] != '-':
		Val = lcm(Work['A'] , Work['B'])
		TotalWork = lcm(Work['C'] , Val)
		steps.append("TotalWork = LCM("+str(Work['A'])+','+str(Work['B'])+','+str(Work['C'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['A'] = TotalWork / Work['A']
		Efficiency['B'] = TotalWork / Work['B']
		Efficiency['C'] = TotalWork / Work['C']
		Efficiency['AB'] = Efficiency['A'] + Efficiency['B']
		Efficiency['BC'] = Efficiency['C'] + Efficiency['B']
		Efficiency['AC'] = Efficiency['A'] + Efficiency['C']
		Efficiency['ABC'] = Efficiency['A'] + Efficiency['B'] + Efficiency['C']
		steps.append("Find the efficiency of A, B, AB, BC, AC and ABC using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of A "+str(Efficiency['A']))
		steps.append("Efficiency of B "+str(Efficiency['B']))
		steps.append("Efficiency of C "+str(Efficiency['C']))
		steps.append("Efficiency of AB together (A+B)"+str(Efficiency['AB']))
		steps.append("Efficiency of BC together (B+C)"+str(Efficiency['BC']))
		steps.append("Efficiency of AC together (A+C) "+str(Efficiency['AC']))
		steps.append("Efficiency of ABC together (A+B+C)"+str(Efficiency['ABC']))

    #if 3 persons are involved and A,B,ABC is known
	elif Work['A'] != '-' and Work['B'] != '-' and Work['ABC'] != '-' and Work['C'] == '-':
		Val = lcm(Work['A'] , Work['B'])
		TotalWork = lcm(Work['ABC'] , Val)
		steps.append("TotalWork = LCM("+str(Work['A'])+','+str(Work['B'])+','+str(Work['ABC'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['A'] = TotalWork / Work['A']
		Efficiency['B'] = TotalWork / Work['B']
		Efficiency['ABC'] = TotalWork / Work['ABC']
		Efficiency['AB'] = Efficiency['A'] + Efficiency['B']
		Efficiency['C'] = Efficiency['ABC'] - Efficiency['AB']
		Efficiency['AC'] = Efficiency['A'] + Efficiency['C']
		Efficiency['BC'] = Efficiency['C'] + Efficiency['B']
		steps.append("Find the efficiency of A, B, AB, BC, AC and ABC using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of A "+str(Efficiency['A']))
		steps.append("Efficiency of B "+str(Efficiency['B']))
		steps.append("Efficiency of ABC together "+str(Efficiency['ABC']))
		steps.append("Efficiency of C (ABC-AB) "+str(Efficiency['C']))
		steps.append("Efficiency of AB together (A+B)"+str(Efficiency['AB']))
		steps.append("Efficiency of BC together (B+C)"+str(Efficiency['BC']))
		steps.append("Efficiency of AC together (A+C) "+str(Efficiency['AC']))


    #if 3 persons are involved and A,B,ABC is known
	elif Work['A'] != '-' and Work['C'] != '-' and Work['ABC'] != '-' and Work['B'] == '-':
		Val = lcm(Work['A'] , Work['C'])
		TotalWork = lcm(Work['ABC'] , Val)
		steps.append("TotalWork = LCM("+str(Work['A'])+','+str(Work['C'])+','+str(Work['ABC'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['A'] = TotalWork / Work['A']
		Efficiency['C'] = TotalWork / Work['C']
		Efficiency['ABC'] = TotalWork / Work['ABC']
		Efficiency['AC'] = Efficiency['A'] + Efficiency['C']
		Efficiency['B'] = Efficiency['ABC'] - Efficiency['AC']
		Efficiency['AB'] = Efficiency['A'] + Efficiency['B']
		Efficiency['BC'] = Efficiency['B'] + Efficiency['C']
		steps.append("Find the efficiency of A, B, AB, BC, AC and ABC using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of A "+str(Efficiency['A']))
		steps.append("Efficiency of C "+str(Efficiency['C']))
		steps.append("Efficiency of ABC together "+str(Efficiency['ABC']))
		steps.append("Efficiency of B (ABC-AC) "+str(Efficiency['B']))
		steps.append("Efficiency of AB together (A+B)"+str(Efficiency['AB']))
		steps.append("Efficiency of BC together (B+C)"+str(Efficiency['BC']))
		steps.append("Efficiency of AC together (A+C) "+str(Efficiency['AC']))

    #if 3 persons are involved and A,B,ABC is known
	elif Work['C'] != '-' and Work['B'] != '-' and Work['ABC'] != '-' and Work['A'] == '-':
		Val = lcm(Work['C'] , Work['B'])
		TotalWork = lcm(Work['ABC'] , Val)
		steps.append("TotalWork = LCM("+str(Work['C'])+','+str(Work['B'])+','+str(Work['ABC'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['C'] = TotalWork / Work['C']
		Efficiency['B'] = TotalWork / Work['B']
		Efficiency['ABC'] = TotalWork / Work['ABC']
		Efficiency['BC'] = Efficiency['C'] + Efficiency['B']
		Efficiency['A'] = Efficiency['ABC'] - Efficiency['BC']
		Efficiency['AC'] = Efficiency['A'] + Efficiency['C']
		Efficiency['AB'] = Efficiency['A'] + Efficiency['B']
		steps.append("Find the efficiency of A, B, AB, BC, AC and ABC using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of C "+str(Efficiency['C']))
		steps.append("Efficiency of B "+str(Efficiency['B']))
		steps.append("Efficiency of ABC together "+str(Efficiency['ABC']))
		steps.append("Efficiency of A (ABC-BC) "+str(Efficiency['A']))
		steps.append("Efficiency of AB together (A+B)"+str(Efficiency['AB']))
		steps.append("Efficiency of BC together (B+C)"+str(Efficiency['BC']))
		steps.append("Efficiency of AC together (A+C) "+str(Efficiency['AC']))

    #if 3 persons are involved and AB,BC,AC is known
	elif Work['AC'] != '-' and Work['BC'] != '-' and Work['AB'] != '-':
		Val = lcm(Work['AB'] , Work['BC'])
		TotalWork = lcm(Work['AC'] , Val)
		steps.append("TotalWork = LCM("+str(Work['AB'])+','+str(Work['BC'])+','+str(Work['AC'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['AB'] = TotalWork / Work['AB']
		Efficiency['BC'] = TotalWork / Work['BC']
		Efficiency['AC'] = TotalWork / Work['AC']
		Efficiency['ABC'] = ( Efficiency['AB'] + Efficiency['BC'] + Efficiency['AC'] ) / 2
		Efficiency['A'] = Efficiency['ABC'] - Efficiency['BC']
		Efficiency['B'] = Efficiency['ABC'] - Efficiency['AC']
		Efficiency['C'] = Efficiency['ABC'] - Efficiency['AB']
		steps.append("Find the efficiency of A, B, AB, BC, AC and ABC using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of AB together (A+B)"+str(Efficiency['AB']))
		steps.append("Efficiency of BC together (B+C)"+str(Efficiency['BC']))
		steps.append("Efficiency of AC together (A+C) "+str(Efficiency['AC']))
		steps.append("Efficiency of ABC together (AB+BC+AC)/2 "+str(Efficiency['ABC']))
		steps.append("Efficiency of A (ABC_BC)"+str(Efficiency['A']))
		steps.append("Efficiency of B (ABC-AC)"+str(Efficiency['B']))
		steps.append("Efficiency of C (ABC-AB) "+str(Efficiency['C']))

    #if 3 persons are involved and A,B,AC is known
	elif Work['A'] != '-' and Work['B'] != '-' and Work['AC'] != '-':
		Val = lcm(Work['A'] , Work['B'])
		TotalWork = lcm(Work['AC'] , Val)
		steps.append("TotalWork = LCM("+str(Work['A'])+','+str(Work['B'])+','+str(Work['AC'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['A'] = TotalWork / Work['A']
		Efficiency['B'] = TotalWork / Work['B']
		Efficiency['AC'] = TotalWork / Work['AC']
		Efficiency['AB'] = Efficiency['A'] + Efficiency['B']
		Efficiency['C'] = ( Efficiency['AB'] + Efficiency['AC'] ) - Efficiency['B'] - ( 2 * Efficiency['A'])
		Efficiency['BC'] = Efficiency['B'] + Efficiency['C']
		Efficiency['ABC'] =  Efficiency['A'] + Efficiency['B'] + Efficiency['C']
		steps.append("Find the efficiency of A, B, AB, BC, AC and ABC using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of A "+str(Efficiency['A']))
		steps.append("Efficiency of B "+str(Efficiency['B']))
		steps.append("Efficiency of AC "+str(Efficiency['AC']))
		steps.append("Efficiency of AB together (A+B)"+str(Efficiency['AB']))
		steps.append("Efficiency of C (AB + AC ) -B -2A "+str(Efficiency['C']))
		steps.append("Efficiency of BC together (B+C)"+str(Efficiency['BC']))
		steps.append("Efficiency of ABC together  "+str(Efficiency['ABC']))

    #if 3 persons are involved and A,B,BC is known
	elif Work['A'] != '-' and Work['B'] != '-' and Work['BC'] != '-':
		Val = lcm(Work['A'] , Work['B'])
		TotalWork = lcm(Work['BC'] , Val)
		steps.append("TotalWork = LCM("+str(Work['A'])+','+str(Work['B'])+','+str(Work['BC'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['A'] = TotalWork / Work['A']
		Efficiency['B'] = TotalWork / Work['B']
		Efficiency['BC'] = TotalWork / Work['BC']
		Efficiency['AB'] = Efficiency['A'] + Efficiency['B']
		Efficiency['C'] = ( Efficiency['AB'] + Efficiency['BC'] ) - Efficiency['A'] - ( 2 * Efficiency['B'])
		Efficiency['AC'] = Efficiency['A'] + Efficiency['C']
		Efficiency['ABC'] =  Efficiency['A'] + Efficiency['B'] + Efficiency['C']
		steps.append("Find the efficiency of A, B, AB, BC, AC and ABC using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of A "+str(Efficiency['A']))
		steps.append("Efficiency of B "+str(Efficiency['B']))
		steps.append("Efficiency of BC "+str(Efficiency['BC']))
		steps.append("Efficiency of AB together (A+B)"+str(Efficiency['AB']))
		steps.append("Efficiency of C (AB + BC ) -A -2B "+str(Efficiency['C']))
		steps.append("Efficiency of AC together (A+C)"+str(Efficiency['AC']))
		steps.append("Efficiency of ABC together  "+str(Efficiency['ABC']))

    #if 3 persons are involved and B,C,AB is known
	elif Work['B'] != '-' and Work['C'] != '-' and Work['AB'] != '-':
		Val = lcm(Work['B'] , Work['C'])
		TotalWork = lcm(Work['AB'] , Val)
		steps.append("TotalWork = LCM("+str(Work['B'])+','+str(Work['C'])+','+str(Work['AB'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['C'] = TotalWork / Work['C']
		Efficiency['B'] = TotalWork / Work['B']
		Efficiency['AB'] = TotalWork / Work['AB']
		Efficiency['BC'] = Efficiency['C'] + Efficiency['B']
		Efficiency['A'] = ( Efficiency['AB'] + Efficiency['BC'] ) - Efficiency['C'] - ( 2 * Efficiency['B'])
		Efficiency['AC'] = Efficiency['A'] + Efficiency['C']
		Efficiency['ABC'] =  Efficiency['A'] + Efficiency['B'] + Efficiency['C']
		steps.append("Find the efficiency of A, B, AB, BC, AC and ABC using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of C "+str(Efficiency['C']))
		steps.append("Efficiency of B "+str(Efficiency['B']))
		steps.append("Efficiency of AB "+str(Efficiency['AB']))
		steps.append("Efficiency of BC together (B+C)"+str(Efficiency['BC']))
		steps.append("Efficiency of A (AB + BC ) -C -2B "+str(Efficiency['A']))
		steps.append("Efficiency of AC together (A+C)"+str(Efficiency['AC']))
		steps.append("Efficiency of ABC together  "+str(Efficiency['ABC']))

    #if 3 persons are involved and B,C,AC is known
	elif Work['B'] != '-' and Work['C'] != '-' and Work['AC'] != '-':
		Val = lcm(Work['B'] , Work['C'])
		TotalWork = lcm(Work['AC'] , Val)
		steps.append("TotalWork = LCM("+str(Work['B'])+','+str(Work['C'])+','+str(Work['AC'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['C'] = TotalWork / Work['C']
		Efficiency['B'] = TotalWork / Work['B']
		Efficiency['AC'] = TotalWork / Work['AC']
		Efficiency['BC'] = Efficiency['C'] + Efficiency['B']
		Efficiency['A'] = ( Efficiency['AC'] + Efficiency['BC'] ) - Efficiency['B'] - ( 2 * Efficiency['C'])
		Efficiency['AB'] = Efficiency['A'] + Efficiency['B']
		Efficiency['ABC'] =  Efficiency['A'] + Efficiency['B'] + Efficiency['C']
		steps.append("Find the efficiency of A, B, AB, BC, AC and ABC using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of C "+str(Efficiency['C']))
		steps.append("Efficiency of B "+str(Efficiency['B']))
		steps.append("Efficiency of AC "+str(Efficiency['AC']))
		steps.append("Efficiency of BC together (B+C)"+str(Efficiency['BC']))
		steps.append("Efficiency of A (BC + AC ) -B -2C "+str(Efficiency['A']))
		steps.append("Efficiency of AB together (B+A)"+str(Efficiency['AB']))
		steps.append("Efficiency of ABC together  "+str(Efficiency['ABC']))

    #if 3 persons are involved and A,C,BC is known
	elif Work['A'] != '-' and Work['C'] != '-' and Work['BC'] != '-':
		Val = lcm(Work['A'] , Work['C'])
		TotalWork = lcm(Work['BC'] , Val)
		steps.append("TotalWork = LCM("+str(Work['A'])+','+str(Work['C'])+','+str(Work['BC'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['A'] = TotalWork / Work['A']
		Efficiency['C'] = TotalWork / Work['C']
		Efficiency['BC'] = TotalWork / Work['BC']
		Efficiency['AC'] = Efficiency['A'] + Efficiency['C']
		Efficiency['B'] = ( Efficiency['AC'] + Efficiency['BC'] ) - Efficiency['A'] - ( 2 * Efficiency['C'])
		Efficiency['AB'] = Efficiency['A'] + Efficiency['B']
		Efficiency['ABC'] =  Efficiency['A'] + Efficiency['B'] + Efficiency['C']
		steps.append("Find the efficiency of A, B, AB, BC, AC and ABC using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of A "+str(Efficiency['A']))
		steps.append("Efficiency of C "+str(Efficiency['C']))
		steps.append("Efficiency of BC "+str(Efficiency['BC']))
		steps.append("Efficiency of AC together (A+C)"+str(Efficiency['AC']))
		steps.append("Efficiency of B (BC + AC ) -A -2C "+str(Efficiency['B']))
		steps.append("Efficiency of AB together (A+B)"+str(Efficiency['AB']))
		steps.append("Efficiency of ABC together  "+str(Efficiency['ABC']))

    #if 3 persons are involved and A,C,AB is known
	elif Work['A'] != '-' and Work['C'] != '-' and Work['AB'] != '-':
		Val = lcm(Work['A'] , Work['C'])
		TotalWork = lcm(Work['AB'] , Val)
		steps.append("TotalWork = LCM("+str(Work['A'])+','+str(Work['C'])+','+str(Work['AB'])+")")
		steps.append(" = "+str(TotalWork))
		Efficiency['A'] = TotalWork / Work['A']
		Efficiency['C'] = TotalWork / Work['C']
		Efficiency['AB'] = TotalWork / Work['AB']
		Efficiency['AC'] = Efficiency['A'] + Efficiency['C']
		Efficiency['B'] = ( Efficiency['AC'] + Efficiency['AB'] ) - Efficiency['C'] - ( 2 * Efficiency['A'])
		Efficiency['BC'] = Efficiency['C'] + Efficiency['B']
		Efficiency['ABC'] =  Efficiency['A'] + Efficiency['B'] + Efficiency['C']
		steps.append("Find the efficiency of A, B, AB, BC, AC and ABC using the formula TotalWork/Number of days taken")
		steps.append("Efficiency of A "+str(Efficiency['A']))
		steps.append("Efficiency of C "+str(Efficiency['C']))
		steps.append("Efficiency of AB "+str(Efficiency['AB']))
		steps.append("Efficiency of AC together (A+C)"+str(Efficiency['AC']))
		steps.append("Efficiency of B (AB + AC ) -C -2A "+str(Efficiency['B']))
		steps.append("Efficiency of BC together (B+C)"+str(Efficiency['BC']))
		steps.append("Efficiency of ABC together  "+str(Efficiency['ABC']))
	else:
		return False



	for i,val in Efficiency.items():
		if Efficiency[i] == '-':
			return False

    #if number of days taken by x has to find
	if ToFind == 1:
		result = round( TotalWork / Efficiency[SubValue1], 2)
		steps.append("Number of days taken by "+str(SubValue1)+" "+str(TotalWork)+"/"+str(Efficiency[SubValue1]))
    #if number of days remaining to complete the work has to find for 3 persons
	elif ToFind == 2:
		days = Value
		WorkDone = Efficiency[SubValue1] * days
		steps.append("Work done = Efficiency of "+SubValue1 +"*"+str(days))
		WorkRemaining = TotalWork - WorkDone
		steps.append("WorkRemaining = TotalWork - WorkDone = "+str(WorkRemaining))
		result = round(WorkRemaining / Efficiency[SubValue1], 2)
		steps.append("Days remaining = WorkRemaining / Efficiency of "+SubValue1+" ="+str(result))
    #if fraction of work remaining to complete the work has to find for 2 persons
	elif ToFind == 3:
		days = Value
		WorkDone = Efficiency[SubValue1] * days
		steps.append("Work done = Efficiency of "+SubValue1 +"*"+str(days))
		WorkRemaining = TotalWork - WorkDone
		steps.append("WorkRemaining = TotalWork - WorkDone = "+str(WorkRemaining))
		result = round(WorkRemaining / TotalWork, 2)
		steps.append("Fraction of work remaining = WorkRemaining / TotalWork  ="+str(result))

    #if to find share of A for 2 persons
	elif ToFind == 10:
		result = (TotalWork / Efficiency[Question['SubValue1']]) * (Efficiency[Question['SubValue2']] / TotalWork) * Value
    # number of days to finish work if x is assisted by y on every z day
	elif ToFind == 5:
		WorkDone = 0
		turn = 0
		days = 0
		while TotalWork != WorkDone:
			days = days + 1
			if days % Value == 0:
				WorkDone = WorkDone + Efficiency[SubValue1]
			else:
				WorkDone = WorkDone + Efficiency[SubValue2]
		result = days
	else:
		return False
	d = {'result':result,'steps':' ','type':' ','stype':' '}
	d['steps'] = steps
	d['type'] = 4
	d['stype'] = 1
	return d
