#!/usr/bin/python3
from functools import reduce
import prime as p
multiplier = 1
max_dec = 0
#-----------------------------------------------------------------------------------------------------------------------------------------------
#To calculate LCM           call function => get_lcm_for(list)
#To calculate GCD or HCF    call function  => GCD_List(list)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#TypeA is to find greatest number of m digit that divisible by n numbers(array of numbers)
#Input : arr_n - list of n numbers(list), m - m digit(int)
def lcmNhcf_typeA(arr_n,m):
    greatestNnumber = 9

    num = 1
    #finding gretest number of m digit
    while num < m:
        greatestNnumber = greatestNnumber * 10 + 9
        num += 1

    #storing lcm of  array of n numbers
    lcmOfN = get_lcm_for(arr_n)
    dict = {'result':' ','steps':' ','type':'5','stype':'1'}
    list = ['Greatest number of '+str(m)+'-digits is'+str(greatestNnumber)]

    #formatting output string
    i = 0
    string_array = ''
    for n in arr_n:
        string_array += str(n)
        if i <= len(arr_n)-3:
            string_array += ", "
        elif i == (len(arr_n)-2):
            string_array += " and "
        i += 1

    list.append("L.C.M. of "+string_array+" is "+str(lcmOfN))
    list.append('On dividing '+str(greatestNnumber)+' by '+str(lcmOfN)+', the remainder is '+str(greatestNnumber % lcmOfN))
    list.append('Required number ('+str(greatestNnumber)+' - '+str(greatestNnumber % lcmOfN)+') = '+str(greatestNnumber - (greatestNnumber % lcmOfN))+'.')
    dict['result'] = 'Ans is '+str(greatestNnumber - (greatestNnumber % lcmOfN))
    dict['steps'] = list
    #print (dict)
    return dict

#-----------------------------------------------------------------------------------------------------------------------------------------------

#TypeB is to find the greatest number that will divide n numbers so as to leave the same remainder in each case.
#Input : arr_n - list of n numbers(list)
def lcmNhcf_typeB(arr_n):
    arr_n.sort()
    new_arr = []

    str_out = ""
    for i in range(0,len(arr_n)):
        if i < len(arr_n) - 1:
            new_arr.append(arr_n[i+1] - arr_n[i])
            str_out += "("+str(arr_n[i + 1])+" - "+str(arr_n[i])+")"
        else:
            new_arr.append(arr_n[i] - arr_n[0])
            str_out += "("+str(arr_n[i])+" - "+str(arr_n[0])+")"

    dict = {'result':' ','steps':' ','type':'5','stype':'2'}
    list = ['The greatest number that will divide numbers so as to leave the same remainder = H.C.F of '+str_out]

    i = 0
    string_array = ''
    for n in new_arr:
        string_array += str(n)
        if i <= len(new_arr)-3:
            string_array += ", "
        elif i == (len(new_arr)-2):
            string_array += " and "
        i += 1

    list.append('H.C.F of '+string_array+' is '+str(g.gcd_of_numbers(new_arr)))
    dict['result'] = 'Ans is '+str(gcd_of_numbers(new_arr))
    dict['steps'] = list
    #print (dict)
    return dict

#-----------------------------------------------------------------------------------------------------------------------------------------------

#TypeC is to find the greatest number if product of two number is given and the H.C.F of those number is given.
#Input : prd_number - product of number (int, hcf_number - hcf of those numbers(int))
def lcmNhcf_typeC(prd_number,hcf_number):
    dict = {'result':' ','steps':' ','type':'5','stype':'3'}
    list = ['Easy to get answer is to just dividing the product of the number with H.C.F']
    list.append('=> product of number / H.C.F')
    list.append('=>'+str(prd_number)+" / "+str(hcf_number))
    dict['result'] = 'Ans is '+str(prd_number/hcf_number)
    dict['steps'] = list
    return dict

#-----------------------------------------------------------------------------------------------------------------------------------------------

#TypeD to find the greatest number which divides x1,x2,... and leaves remainder a1,a2,... respectively
#Input : number_list - are list of number, rem_list - are their reminders respectively
def lcmNhcf_typeD(number_list,rem_list):

    new_list = []
    number_list_string =""
    i = 0
    for n in range(0,len(number_list)):
        new_list.append(number_list[n] - rem_list[n])
        number_list_string += "( "+str(number_list[n])+" - "+str(rem_list[n])+" )"
        if i <= len(number_list) - 3:
            number_list_string += ", "
        elif i == len(number_list) - 2:
            number_list_string += " and "
        i += 1

    new_list_string =""
    i = 0
    for num in new_list:
        new_list_string += str(num)
        if i < len(new_list) - 3:
            new_list_string += ", "
        elif i == len(new_list) -2:
            new_list_string += " and "
        i += 1

    steps = ["Required number = H.C.F. of "+number_list_string]
    steps.append("H.C.F. of "+new_list_string+" = "+str(g.GCD_List(new_list)))
    d = {'result': "Ans is "+str(g.GCD_List(new_list)),'steps':steps,'type':'5','stype':'4'}
    #print (d)
    return d

#-----------------------------------------------------------------------------------------------------------------------------------------------

#TypeE is to find HCF of number when ratios and LCM is given
#Input : ratios_arr - list of ratios(list), lcm_numbers - lcm of those number(int)
def lcmNhcf_typeE(ratios_arr,lcm_numbers):
    product = 1
    for n in ratios_arr:
        product *= n
    dict = {'result':' ','steps':' ','type':'5','stype':'5'}
    list = ['L.C.M = '+str(lcm_numbers)]
    list.append('Product of ratios ='+str(product))
    list.append('H.C.F = L.C.M / product of ratios')
    list.append('=>'+str(lcm_numbers)+' / '+str(product))
    dict['result'] = 'Ans is '+str(lcm_numbers/product)
    dict['steps'] = list
    return dict

#-----------------------------------------------------------------------------------------------------------------------------------------------
#TypeF to find The least number, which when divided by x, y,...   leaves in each case a remainder of a is
#input numberlist = x,y,... and rem is a
#Question number 25
def lcmNhcf_typeF(numberlist,rem):

    i = 1
    string_array = ""
    for n in numberlist:
        string_array += str(n)
        if i < len(numberlist):
            string_array += ", "
        i += 1
    steps = ["Required number = (L.C.M. of "+ string_array +") + "+str(rem)]
    steps.append(str(get_lcm_for(numberlist))+" + "+str(rem))
    steps.append(str(get_lcm_for(numberlist) + rem))
    d = {'result': 'Ans is '+str(get_lcm_for(numberlist) + rem),'steps':steps,'type':'5','stype':'6'}
    #print (d)
    return d

#----------------------------------------------------------------------------------------------------------------------------------------------

#TypeG is to find the larger of n numbers when H.C.F and factors of number is given
#Question no. 2 in indiabix.com
#input :c_num => count of number for which HCF is given, hcf_number => HCF of the numbers, f_of_lcm => factors of LCM
def lcmNhcf_typeG(c_num,hcf_number,f_of_lcm):
    fac_list = []
    for num in f_of_lcm:
        fac_list.append(hcf_number * num)

    largest = max(fac_list)
    index = fac_list.index(largest)

    numbers_string = ""
    alp = ord('a')
    for i in range(0,c_num):
        numbers_string += ""+chr(alp)
        if i < c_num-1:
            numbers_string += " * "
        alp += 1

    alp = ord('a')
    factors_string = ""
    mul_factors_string = ""
    each_value_string = ""
    for i in range(0,len(f_of_lcm)):
        mul_factors_string += "( "+str(hcf_number)+" * "+str(f_of_lcm[i])+" )"
        each_value_string += ""+chr(alp)+" = ( "+str(hcf_number)+" * "+str(f_of_lcm[i])+" )"
        factors_string += ""+str(f_of_lcm[i])
        if i< len(f_of_lcm)-1:
            mul_factors_string += " * "
            factors_string += " * "
            each_value_string += " * "
        alp += 1

    solution_string = ""+chr(65+index)+" = ( "+str(hcf_number)+" * "+str(f_of_lcm[index])+") "

    dict = {'result':' ','steps':' ','type':'5','stype':'7'}
    list = ['H.C.F * L.C.M = '+numbers_string]
    list.append(''+str(hcf_number)+' * ( '+factors_string+' ) = '+numbers_string)
    list.append(''+mul_factors_string+' = '+numbers_string)
    list.append(''+each_value_string)
    list.append('Therfore '+solution_string+'is the greatest')
    dict['result'] = 'Ans is '+str(largest)
    dict['steps'] = list
    return dict
    #print(dict)

#-----------------------------------------------------------------------------------------------------------------------------------------------
#TypeH is to find the HCF or GCD of numbers (also used to find the GCD OR HCF of floating numbers)
#Input : arr - list of numbers
def lcmNhcf_typeH(arr):
    dict = {'result':' ','steps':' ','type':'5','stype':'8'}
    i = 0
    string_array = ''
    for n in arr:
        string_array += str(n)
        if i <= len(arr)-3:
            string_array += ", "
        elif i == (len(arr)-2):
            string_array += " and "
        i += 1
    ans = gcd_of_numbers(arr)
    list = ['Given numbers are '+string_array]
    if max_dec != 0:
        i = 0
        string_array_mul = ''
        for n in arr:
            string_array_mul += str(n * multiplier)
            if i <= len(arr)-3:
                string_array_mul += ", "
            elif i == (len(arr)-2):
                string_array_mul += " and "
            i += 1

        list.append('H.C.F or G.C.D of '+string_array_mul+' is '+str(gcd_of_numbers(arr) * multiplier))
    list.append('H.C.F. or G.C.D of given numbers = '+str(gcd_of_numbers(arr)))
    dict['result'] = 'Ans is '+str(gcd_of_numbers(arr))
    dict['steps'] = list
    return dict
#-----------------------------------------------------------------------------------------------------------------------------------------------
#TypeI is to find the least multiple of n, which leaves a remainder of m, when divided by x1,x1,x3....,xk is:
#Input : num = n ,rem = remainder, num_list = list of x1,x2,...,xk
def lcmNhcf_typeI(num,rem,num_list):
    lcm_value = get_lcm_for(num_list)
    i = 0
    while True:
        if (lcm_value * i + rem) % num == 0:
            break
        i += 1
    least_number = i

    i = 0
    num_string = ''
    for n in num_list:
        num_string += str(n)
        if i <= len(num_list)-3:
            num_string += ", "
        elif i == (len(num_list)-2):
            num_string += " and "
        i += 1

    dict = {'result':' ','steps':' ','type':'5','stype':'9'}
    list = ['L.C.M of '+num_string+' is '+str(lcm_value)]
    list.append('Let required number be '+str(lcm_value)+'k + '+str(rem)+', which is multiple of '+str(num))
    list.append('Least value of k for which ('+str(lcm_value)+'k + '+str(rem)+' ) is divisible by '+str(rem)+' is k = '+str(least_number))
    list.append(' Required number = ('+str(lcm_value)+' x '+str(least_number)+' ) + '+str(rem)+' = '+str(lcm_value * least_number + rem))
    dict['result'] = 'Ans is '+str(lcm_value * least_number + rem)
    dict['steps'] = list
    return dict
#-----------------------------------------------------------------------------------------------------------------------------------------------
#TypeJ is to find the lcm of numbers
#Input:  num_list = list of number for which lcm is be found
def lcmNhcf_typeJ(num_list):
    prm = p.Prime()
    i = 0
    num_string = ''
    for k in num_list:
        num_string += str(k)
        if i <= len(num_list)-2:
            num_string += ", "
        i += 1
    dict = {'result':' ','steps':' ','type':'5','stype':'10'}
    list = ['LCM of the numbers '+num_string]

    prime_num = 2
    index = 0
    first_time = 0
    prime_list = []
    while True:
        flag1 = 0
        flag2 = 0
        first_time += 1
        for n in num_list:
            if(prm.is_prime(n) or n == 1):
                flag1 += 1
        print(prime_num)

        if flag1 != len(num_list):
            while True:
                for m in num_list:
                    if m % prime_num == 0:
                        flag2 += 1
                if flag2 == 0:
                    prime_num = prm.next()
                else:
                    prime_list.append(prime_num)
                    break

        i = 0
        num_string = ''
        for k in num_list:
            num_string += str(k)
            if i <= len(num_list)-2:
                num_string += ", "
            i += 1

        if flag1 != len(num_list):
            list.append(''+str(prime_num)+'| '+num_string)
        else:
            for l in num_list:
                prime_list.append(l)
            if first_time > 1:
                list.append('    | '+num_string)
            else:
                list.append('All the numbers are prime hence we obtain the LCM by multiplying all numbers')
            break

        for index in range(0,len(num_list)):
            if num_list[index] % prime_num == 0:
                num_list[index] = int (num_list[index] / prime_num)

    i = 0
    ans = 1
    num_string = ''
    for num in prime_list:
        ans *= num
        num_string += str(num)
        if i <= len(prime_list)-2:
            num_string += " x "
        i += 1


    list.append('L.C.M = '+num_string+' = '+str(ans))
    dict['result'] = 'Ans is '+str(ans)
    dict['steps'] = list
    return dict

#-----------------------------------------------------------------------------------------------------------------------------------------------
#LCM logic
#start
def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

def get_lcm_for(n_list):
    return reduce(lambda x, y: lcm(x, y), n_list)
#End
#-----------------------------------------------------------------------------------------------------------------------------------------------
#GCD or HCF logic
#start
def gcd_of_numbers(arr):
    global multiplier
    global max_dec
    max_dec = num_after_point(arr[0])
    #finding max number of digit after the decimal point
    for i in range(1,len(arr)):
        if max_dec < num_after_point(arr[i]):
            max_dec = num_after_point(arr[i])

    if max_dec != 0:
        #if decimal point is present
        multiplier = 1
        #finding the muliples of 10 to make whole number
        for i in range(1,max_dec+1):
            multiplier *= 10

        new_arr = []
        #converting each number to whole number
        for n in arr:
            new_arr.append(n * multiplier)

        return GCD_List(new_arr) / multiplier #again converting to decimal number
    else:
        return GCD_List(arr)

#func to find the number of digits after decimal
def num_after_point(x):
    s = str(x)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1

def GCD(a,b):
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b%a, a
    return b

def GCD_List(list):
	return reduce(GCD, list)
#End
#-----------------------------------------------------------------------------------------------------------------------------------------------
