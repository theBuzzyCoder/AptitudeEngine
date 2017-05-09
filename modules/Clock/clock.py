#!/usr/bin/python3

#expected type of questions in this category
#1 angle between two hands
#2 angle made by one hand
#3 at what time both hands
#  1 together
#  2 opposite
# ques parameter is a dictionary of following format
# for format 1 and 2 {"hour":10,"min" :30,"type" :1}
# type -1 angle b/w 2 hands
# type-2 angle by hour hand
# type-3 angle by min hand
# for format 3 {"from":10,type":"1"}
# type-1 together
# type-2 opposite
def calculate_angle(ques):
    solution = {"type":3}
    steps = []
    hour_angle = False
    minute_angle = False
    result = False
    if "hour" in ques:
        #type 1 or 2
        if ques['type'] == 1 or ques['type'] == 2:
            solution['stype'] = 2
            steps.append("From the clock we can observe that for every hour ,hour hand moves by 30deg (How 30deg ? 12hours - 360deg,1hour - ? its 30deg)")
            steps.append("Now notice that for every 60min hour hand moves 30deg i.e for every 2min 1deg")
            hour_angle = 30 * ques['hour'] + ques['min'] / 2
            result = hour_angle
            steps.append("So the formula would be hour_angle = 30*hour_hand+min_hand/2 i.e hour_angle = 30 * "+str(ques['hour'])+" + "+str(ques['min'])+" / 2 = "+str(hour_angle)+" deg")
            solution['result'] = "Angle made by hour hand is %d deg" %(result)

        if ques['type'] == 1 or ques['type'] == 3:
            solution['stype'] = 3
            steps.append("From the clock we observe that for every min ,minute hand moves 6 deg (How 6deg ? 60min -360deg,1min -? its 6deg)")
            minute_angle = 6 * ques['min']
            result = minute_angle
            steps.append("So the formula would be minute_angle = min_hand * 60 i.e minute_angle = 60 * "+str(ques['min'])+" = "+str(minute_angle)+" deg")
            solution['result'] = "Angle made by minute hand is %d deg" %(result)

        if ques['type'] == 1:
            solution['stype'] = 1
            result = abs(hour_angle - minute_angle)
            steps.append("Angle between two hands is | hour_angle - minute_angle | i.e | "+str(hour_angle)+" - "+str(minute_angle)+" | = "+str(result))
            steps.append("Note : if angle between two hands greater than 180 subtract the angle from 360")
            if result > 180:
                steps.append("Since angle between two hands is greater than 180 then angle = 360 - "+str(result)+" = "+( 360 - result ))
                result = 360 - result
            solution['result'] = "Angle is "+str(result)+" deg"
    else:
        if ques['type'] == 1 :
            solution['stype'] = 4
            #two hands are together when the hour_angle = minute_angle
            #i.e 30*h+m/2 = 6*m
            # let 30*h be a constant c
            #then c+m/2 = 6m
            # c = 11m/2
            # ie 30h = 11m/2
            # ie m = 60/11h
            m = round(60 / 11 * ques['from'],2)
            steps.append("Both hands will be together when hour_angle = minute_angle")
            steps.append("Angle made by hour hand is given by 30 * hour_hand + minute_hand / 2")
            steps.append("Angle made by minute hand is given by 6 * minute_hand")
            steps.append("We relate the above two we get a equation minute_hand = hour_hand * 60 / 11")
            result = m
            if m < 60:
                steps.append("So hour hand and minute hand will coincide at "+str(ques['from'])+" hour and "+str(m)+" minutes")
                solution['result'] = "Hour hand and minute hand will  coincide at "+str(ques['from'])+" hour and "+str(m)+" minutes"
            else:
                steps.append("As we get minute_hand = "+str(m)+" which is greater or equal to be 60 which is impossible")
                steps.append("Hour hand and minute hand will never coincide between "+str(ques['from']) + " - " +str((ques['from']+1) % 12) + " hours")
                solution['result'] = "Hour hand and minute hand will never coincide between "+str(ques['from']) + " - " +str((ques['from']+1) % 12) + " hours"
        else:
                #two hands are opposite when the |hour_angle - minute_angle| = 180
                #i.e |30*h+m/2 - 6*m| = 180
                # let 30*h be a constant c
                #then |c+m/2 - 6m| = 180
                # |c - 11m/2| = 180
                # ie 30h +- 180 = 11m/2
                # ie m = 60(h -6)/11
                # ie if h >= 6
                #    m = 60(h-6)/11
                # else m = 60(h+6)/11
                solution['stype'] = 5
                if ques['from'] >= 6:
                    m = round(60/11*(ques['from'] - 6),2)
                else:
                    m = round(60/11*(ques['from'] + 6),2)
                steps.append("Both hands will be opposite when | hour_angle - minute_angle | = 180deg")
                steps.append("Angle made by hour hand is given by 30 * hour_hand + minute_hand / 2")
                steps.append("Angle made by minute hand is given by 6 * minute_hand")
                steps.append("We relate the above two we get two equation")
                steps.append("if hour_hand >= 6 then minute_hand = 60/11 * ( hour_hand - 6 )")
                steps.append("else  minute_hand = 60/11 * ( hour_hand + 6 )")
                result = m
                if m < 60:
                    steps.append("So hour hand and minute hand will be opposite between "+str(ques['from'])+" hour and "+str(m)+" minutes")
                    solution['result'] = "Hour hand and minute hand will be opposite between "+str(ques['from'])+" hour and "+str(m)+" minutes"
                else:
                    steps.append("As we get minute_hand = "+str(m)+" which is greater or equal to be 60 which is impossible")
                    steps.append("Hour hand and minute hand will never be opposite between "+str(ques['from']) + " - " +str((ques['from']+1) % 12) + " hours")
                    solution['result'] = "Hour hand and minute hand will never be opposite between "+str(ques['from']) + " - " +str((ques['from']+1) % 12) + " hours"
    solution['steps'] = steps
    return solution
