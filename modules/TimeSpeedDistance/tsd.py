#!/usr/bin/python
# Written by Abytecoder
import formula as f
import custom_time as t
import speed as s
import distance as d
#ques format
# to calculate speed
#{"distance":100,"unit":"m","time":[h,m,s],"output-unit" :"m","output":"s"}
# to calculate time
#{"distance":100,"unit":"m","speed":100,"speed-unit":"k","output-unit" :"m","output":"t"}
# to calculate distance
#{"unit":"m","speed":100,"time":[h,m,s],"output-unit" :"m","output":"d"}
#distance options m-meters,mi-miles,k-kilo-meters
#time array h-hour,m-minutes,s-seconds
#output what format they need output as

def time_distance(ques):
    answer = {'result':'','type':2,'stype':1}
    steps = []

    if ques['output'] == "s":
        time = t.Time(ques['time'][0],ques['time'][1],ques['time'][2])
        dis = d.Distance(ques['distance'],ques['unit'])
        speed = f.speed(dis,time,ques['output-unit'])
        speed_unit = s.units(ques['output-unit'])
        steps.append("Formula to calculate speed is"+ f.get_formula("s") + "\n"+ f.note)
        steps.append( f.get_conversion("d") )
        steps.append( f.get_conversion("t") )
        steps.append("So the speed is %.2f%s" %(speed ,speed_unit))
        answer['result'] = "The speed is %.2f%s" %(speed ,speed_unit);
    elif ques['output'] == "t":
        dis = d.Distance(ques['distance'],ques['unit'])
        speed = s.Speed(ques['speed'],ques['speed-unit'])
        time = f.time(dis,speed,ques['output-unit'])
        time_unit = t.units(ques['output-unit'])
        steps.append("Formula to calculate time is"+ f.get_formula("t") + "\n"+ f.note)
        steps.append( f.get_conversion("d") )
        steps.append( f.get_conversion("s") )
        steps.append("So the time is %.2f%s" %(time ,time_unit))
        answer['result'] = "The time is %.2f%s" %(time ,time_unit)
    else:
        speed = s.Speed(ques['speed'],ques['speed-unit'])
        time = t.Time(ques['time'][0],ques['time'][1],ques['time'][2])
        distance_unit = d.units(ques['output-unit'])
        dis = f.distance(speed,time,ques['output-unit'])
        steps.append("Formula to calculate distance is"+ f.get_formula("d") + "\n"+ f.note)
        steps.append( f.get_conversion("s") )
        steps.append( f.get_conversion("t") )
        steps.append("So the distance is %.2f%s" %(dis ,distance_unit))
        answer['result'] = "The distance is %.2f%s" %(dis ,distance_unit);
    answer['steps'] = steps
    return answer

# function which solves the relative speed between two objects
# train - train
# train -pole
# train - human
# police - theif
# function will take two dictionary describing two objects
# function will also take 3 more parameters consits of
# given - an dictionary which tells what detail is given ?like time taken or
# distance between two ojects or both
# output describes what should be the solved by function is it speed,length,time etc
# opposite - true if two objects are moving in same direction else false
# dictionary will have following items
# name - tells the name of object ex train,man etc
# length - tells the length of the object
# l-unit - unit of the length
# speed - an speed object
# s-unit - unit of speed

def relative_speed(object1,object2,given,output,opposite):
    answer = {'result':'','type':2,'stype':2}
    steps = []
    distance_unit = d.units(output['unit'])
    time_unit = t.units(output['unit'])
    speed_unit = s.units(output['unit'])
    if output['what'] == "time":
        l1 = d.Distance(object1['length'],object1['l-unit'])
        l2 = d.Distance(object2['length'],object2['l-unit'])
        dis = d.Distance(given['distance'],given['unit'])
        total_dis = 0
        if output['unit'] == "m":
            total_dis = l1.to_mtr() + l2.to_mtr() + dis.to_mtr()
        elif output['unit'] == "k":
            total_dis = l1.to_km() + l2.to_km() + dis.to_km()
        else:
            total_dis = l1.to_mi() + l2.to_mi() + dis.to_mi()


        rel_speed = add_relative_speed_step(steps,object1,object2,opposite,output['unit'])
        time = f.rd(total_dis / rel_speed)
        steps.append("The distance between %s and %s (including their length) is %.2f%s" %(object1['name'],object2['name'],total_dis,distance_unit))
        steps.append("Formula to calculate time is" + f.get_formula("t") + "\n"+ f.note)
        steps.append( f.get_conversion("d") )
        steps.append( f.get_conversion("s") )
        steps.append("So the time taken to cover distance between %s and %s (including their length) is %.2f%s" %(object1['name'],object2['name'],time,time_unit))
        answer['result'] = "The time taken to cover distance between %s and %s (including their length) is %.2f%s" %(object1['name'],object2['name'],time,time_unit)
    elif output['what'] == "distance" :
        l1 = d.Distance(object1['length'],object1['l-unit'])
        l2 = d.Distance(object2['length'],object2['l-unit'])
        time = t.Time(given['time'][0], given['time'][1], given['time'][2])
        dis = 0
        if output['unit'] == "m":
            time = time.to_secs()
            dis = l1.to_mtr() + l2.to_mtr()
        else:
            time = time.to_hours()
            if output['unit'] == "k":
                dis = l1.to_km() + l2.to_km()
            else:
                dis = l1.to_mi() + l2.to_mi()

        rel_speed = add_relative_speed_step(steps,object1,object2,opposite,output['unit'])
        steps.append("The time taken to cover distance between %s and %s (including their length) is %.2f%s" %(object1['name'],object2['name'],time,time_unit))
        steps.append("Formula to calculate distance is"+ f.get_formula("d") + "\n"+ f.note)
        steps.append( f.get_conversion("s") )
        steps.append( f.get_conversion("t") )
        steps.append("The length of  %s and %s is %.2f%s" %(object1['name'],object2['name'],dis,distance_unit))
        total_dis = f.rd( rel_speed * time )
        steps.append("The distance between %s and %s (including their length) is %.2f%s" %(object1['name'],object2['name'],total_dis,distance_unit))
        steps.append("So the distance between %s and %s is %.2f%s" %(object1['name'],object2['name'],total_dis - dis,distance_unit))
        answer['result'] = "The distance between %s and %s is %.2f%s" %(object1['name'],object2['name'],total_dis - dis,distance_unit)
    else:
        object_to_solve = False
        object_given = False
        if output['what'] == "speed-1" or output['what'] == "length-1":
            object_to_solve = object1
            object_given = object2
        else:
            object_to_solve = object2
            object_given = object1

        if output['what'].startswith("speed"):
            dis = d.Distance(given['distance'],given['unit'])
            speed_given = s.Speed(object_given['speed'],object_given['s-unit'])
            length_given = d.Distance(object_given['length'],object_given['l-unit'])
            length_solve = d.Distance(object_to_solve['length'],object_to_solve['l-unit'])
            time = t.Time(given['time'][0], given['time'][1], given['time'][2])
            total_dis = 0
            if output['unit'] == "m":
                total_dis = dis.to_mtr() + length_given.to_mtr() + length_solve.to_mtr()
                time = time.to_secs()
            elif output['unit'] == "k":
                total_dis = dis.to_km() + length_given.to_km() + length_solve.to_km()
                time = time.to_hours()
            else:
                total_dis = dis.to_mi() + length_given.to_mi() + length_solve.to_mi()
                time = time.to_hours()

            steps.append("The distance between %s and %s (including their length) is %.2f%s" %(object_to_solve['name'],object_given['name'],total_dis,distance_unit))
            steps.append("Formula to calculate relative speed is"+ f.get_formula("s") + "\n"+ f.note)
            steps.append( f.get_conversion("d") )
            steps.append( f.get_conversion("t") )
            speed = f.rd(total_dis / time)
            steps.append("So the relative speed is %.2f%s" %(speed ,speed_unit))
            msg = "But relative speed is nothing but \n"
            if opposite:
                steps.append(msg + f.get_formula("rs-2"))
                speed_solve = speed - speed_given
                steps.append("So speed of %s is relative speed - speed of %s = %.2f%s" %(object_to_solve['name'],object_given['name'],speed_solve,speed_unit))
                answer['result'] = "Speed of %s is relative speed - speed of %s = %.2f%s" %(object_to_solve['name'],object_given['name'],speed_solve,speed_unit)
            else:
                steps.append(msg + f.get_formula("rs-1"))
                speed_solve = speed + speed_given
                steps.append("So speed of %s is relative speed + speed of %s = %.2f%s" %(object_to_solve['name'],object_given['name'],speed_solve,speed_unit))
                answer['result'] = "Speed of %s is relative speed + speed of %s = %.2f%s" %(object_to_solve['name'],object_given['name'],speed_solve,speed_unit)

        else:
                dis = d.Distance(given['distance'],given['unit'])
                length_given = d.Distance(object_given['length'],object_given['l-unit'])
                time = t.Time(given['time'][0], given['time'][1], given['time'][2])
                rel_speed = add_relative_speed_step(steps,object_to_solve,object_given,opposite,output['unit'])
                if output['unit'] == "m":
                    time = time.to_secs()
                    dis = dis.to_mtr()
                    length_given = length_given.to_mtr()
                elif output['unit'] == "k":
                    time = time.to_hours()
                    dis = dis.to_km()
                    length_given = length_given.to_km()
                else:
                    time = time.to_hours()
                    dis = dis.to_mi()
                    length_given = length_given.to_mi()
                total_dis = f.rd(rel_speed * time)
                length_solve = total_dis - dis - length_given
                steps.append("The distance between %s and %s (including their length) is %.2f%s" %(object_to_solve['name'],object_given['name'],total_dis,distance_unit))
                steps.append("So the length of %s is total distance - distance given - length of %s = %.2f %s" %(object_to_solve['name'],object_given['name'],length_solve,distance_unit))
                answer['result'] = "The length of %s is total distance - distance given - length of %s = %.2f %s" %(object_to_solve['name'],object_given['name'],length_solve,distance_unit)
    answer['steps'] = steps
    return answer

def add_relative_speed_step(steps,object1,object2,opposite,unit):
    s1 = s.Speed(object1['speed'],object1['s-unit'])
    s2 = s.Speed(object2['speed'],object2['s-unit'])
    rel_speed = f.rel_speed(s1,s2,opposite,unit)
    msg = "Formula to calculate relative speed is \n"
    speed_unit = s.units(unit)
    if opposite:
        steps.append(msg + f.get_formula("rs-2"))
    else:
        steps.append(msg + f.get_formula("rs-1"))
    steps.append("The relative speed is %.2f%s" %(rel_speed,speed_unit))
    return rel_speed
