import solve_series as s
def checkAlpha(series,type,index):
    new_series = []
    #loop through series
    for i in range(0,len(series)):
        #if series element is in capital letter (65 is ASCII value of A and 90 is the ASCII value of Z)
        if ord(series[i]) >= 65 and ord(series[i]) <= 90:
            # converting ASCII values to the alphabetic position
            new_series.append(ord(series[i]) - 64)
            #cap is TRUE when series in capital letters
            cap = True
        #if series element is in small letter (97 is ASCII value of a and 122 is the ASCII value of z)
        elif ord(series[i]) >= 97 and ord(series[i]) <= 122:
            new_series.append(ord(series[i]) - 96)
            #cap is False when series in capital letters
            cap = False
        else:
            #copy ' _ ' to missing position
            new_series.append('_')
            index = i
    #check wheather alphabetic position  in AP
    if s.ap(new_series,index):
        flag = 1
        #storing missing value in variable value
        value = s.ap(new_series,index)
    #check wheather alphabetic position  in HP
    if s.hp(new_series,index):
        flag = 2
        #storing missing value in variable value
        value = s.hp(new_series,index)
    #check wheather alphabetic position  in GP
    if s.gp(new_series,index):
        flag = 3
        #storing missing value in variable value
        value = s.gp(new_series,index)
    if index < len(new_series):
        new_series[index] = '_'
    else:
        new_series.append('_')
    print(new_series)
    newlist = ['Check the position of the alphabetic series']
    new_series_strng = ''
    i=0
    #converting each digit to string
    for num in new_series:
        new_series_strng += str(num)
        #checking end of series
        if i != (len(new_series) - 1):
            #adding ' , ' after each digits
            new_series_strng += ', '
        i += 1

    newlist.append(''+new_series_strng)

    #flag = 1 series is in AP
    if flag == 1:
        #getting dictionary and storing it d
        d = s.addap(new_series,type,index)
        d['type'] = '1'
        d['stype'] = '7'
    #flag = 2 series is in HP
    elif flag == 2:
        d = s.addhp(new_series,type,index)
        d['type'] = '1'
        d['stype'] = '8'
    #flag = 3 series is in GP
    elif flag == 3:
        d = s.addgp(new_series,type,index)
        d['type'] = '1'
        d['stype'] = '9'

    #Appending dictionary value d['steps'] to new dictionary newlist
    d['steps'] = newlist + d['steps']
    newlist1 = []
    if cap:
        #is character is capital add 64 to make its ASCII equivalent and converted to character
        value = chr(value + 64)
        newlist1.append('Missing character is '+value)
    else:
        #is character is capital add 64 to make its ASCII equivalent and converted to character
        value = chr(value + 96)
        newlist1.append('Missing character is '+value)
    d['steps'] = d['steps'] + newlist1
    d['result'] = 'Ans is '+value
    return d
