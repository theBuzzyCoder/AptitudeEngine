#!/usr/bin/python3

# formula's or conversion in textual format
note ="Note : All values should be converted to proper units"
conversion = []
conversion.append("""Speed :
From meters per second to kilometers per hour -> speed * 5 / 18
From meters per second to miles per hour -> speed * 5 / 18 * 0.62
From kilometers per hour to meters per second -> speed * 18 / 5
From kilometers per hour to miles per hour -> speed * 0.62
From miles per hour to meters per second -> speed * 1.61 * 5 /18
From miles per hour to kilometers per hour -> speed * 1.61 """)
conversion.append("""Distance :
From meters to kilometers -> distance / 1000
From meters to miles -> distance / 1000 * 0.62
From kilometers to meters -> distance * 1000
From kilometers to miles -> distance * 0.62
From miles to meters -> distance * 1610
From miles to kilometers -> distance * 1.61""")
conversion.append("""Time :
From seconds to minutes -> time / 60
From seconds to hours -> time / 3600
From minutes to seconds -> time * 60
From minutes to hours -> time / 60
From hours to seconds -> time * 3600
From hours to minutes -> time * 60""")

#returns conversion based on requirement
def get_conversion(unit):
    if unit =="s":
        return conversion[0]
    elif unit == "d":
        return conversion[1]
    else:
        return conversion[2]

#returns formula string
# parameter f can be
# s -> for speed formula
# d -> for distance formula
# t -> for time formula
# rs-1 -> for relative speed same direction
# rs-2 -> for relative speed opposite direction
# rat-distance-? -> ratio of distance based on their speed and time
# rat-speed-? -> ratio of speed based on their distance and time
# rat-time-1 -> ratio of time based on their speed
# rat-time-2 -> ratio of time based on their distance
# avg-speed-1 : average speed based on their two different speed
# avg-speed-2 : average speed based on  distance and time
formulas = []
formulas.append(" Speed = Distance / Time ")
formulas.append(" Distance = Speed * Time ")
formulas.append(" Time = Distance / Speed ")
formulas.append(" If two objects are moving in same direction then their relative speed is \n Speed = | speed_of_object1 - speed_of_object2 | ")
formulas.append(" If two objects are moving in opposite direction then their relative speed is \n Speed = speed_of_object1 + speed_of_object2 ")
formulas.append(" If two objects have their speed in ratio A:B then their distance is also in A : B ratio ")
formulas.append(" If two objects have their time in ratio A:B then their distance is also in A : B ratio ")
formulas.append(" If two objects have their distance in ratio A:B then their speed is also in A : B ratio ")
formulas.append(" If two objects have their speed in ratio A:B then their time is in B : A ratio ")
formulas.append(" If two objects have their distance in ratio A:B then their speed is also in A : B ratio ")
formulas.append(" Suppose an object covers a certain distance at x speed and an equal distance at y speed. Then,the average speed during the whole journey is ( 2 * x * y )/( x + y ) ")
formulas.append(" Average speed is given by Total distance travelled / Total time ")


def get_formula(f):
    params = [
    "s","d","t","rs-1","rs-2","rat-distance-1","rat-distance-2","rat-speed-1","rat-speed-2",
    "rat-time-1","rat-time-2","avg-speed-1","avg-speed-2"]

    try:
        return formulas[ params.index(f) ]
    except Exception as e:
        return False

#modified round function to round off upto 2 decimal point
def rd(num):
    if isinstance(num,int):
        return num
    return round(num,2)

#formula for relative speed
def rel_speed(s1,s2,opposite,unit):
    if opposite:
            if unit == "m" :
                return rd( s1.to_mtrps() + s2 .to_mtrps())
            elif unit == "k" :
                return rd( s1.to_kmph() + s2 .to_kmph())
            else :
                return rd( s1.to_miph() + s2 .to_miph())
    else:
        if unit == "m" :
            return rd( abs(s1.to_mtrps() - s2 .to_mtrps()))
        elif unit == "k" :
            return rd( abs(s1.to_kmph() - s2 .to_kmph()))
        else :
            return rd( abs(s1.to_miph() - s2 .to_miph()) )

#formula to calculate speed
def speed(dis,time,unit):
    if unit == "m" :
        return rd(dis.to_mtr() / time.to_secs())
    elif unit == "k" :
        return rd(dis.to_km() / time.to_hours())
    else :
        return rd(dis.to_mi() /time.to_hours())

#formula to calculate time
def time(dis,speed,unit):
        if unit == "m" :
            return rd(dis.to_mtr() / speed.to_mtrps())
        elif unit == "k" :
            return rd(dis.to_km() / speed.to_kmph())
        else :
            return rd(dis.to_mi() / speed.to_miph())

#formula to calculate distance
def distance(speed,time):
    if unit == "m" :
        return rd(time.to_secs() * speed.to_mtrps())
    elif unit == "k" :
        return rd(time.to_hours() * speed.to_kmph())
    else :
        return rd(time.to_hours() * speed.to_miph())

#function to find average speed
def average_speed(array_dis,array_time,unit):
    total_dis = 0
    total_time = 0
    if unit == "m":
        for index in len(array_dis):
            total_dis += array_dis[index].to_mtr()
            total_time += array_time[index].to_secs()
    elif unit == "k":
        for index in len(array_dis):
            total_dis += array_dis[index].to_km()
            total_time += array_time[index].to_hours()
    else:
        for index in len(array_dis):
            total_dis += array_dis[index].to_mi()
            total_time += array_time[index].to_hours()
    return rd(total_dis / total_time)
