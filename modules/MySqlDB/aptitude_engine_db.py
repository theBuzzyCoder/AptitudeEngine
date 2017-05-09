#!/usr/bin/python3
import mysql
interface = False
import json

def get_all_types():
    result =[]
    data = interface.select("SELECT * FROM type_table")
    for row in data:
        item = {}
        item['name'] = row[1]
        item['image'] = row[2]
        result.append(item)
    return result

def feedback(data):
    if data['id'] != 0:
        interface.uid("INSERT INTO feedback (qid,name,email,type,ftext) VALUES (%d,'%s','%s',%d,'%s')" %(int(data['id']),data['name'],data['email'],int(data['type']),data['ftext']))
    else:
        interface.uid("INSERT INTO feedback (name,email,type,ftext) VALUES ('%s','%s',%d,'%s')" %(data['name'],data['email'],int(data['type']),data['ftext']))


def get_type(typeid,stypeid):
    type_data = interface.select("SELECT type FROM type_table WHERE id = %d" %(typeid),False)
    sub_type = interface.select("SELECT stype FROM stype_table WHERE typeid = %d and stypeid = %d" %(typeid,stypeid))
    return (type_data[0],sub_type[0][0])

def insert_question(question,dictionary):
    typ = int(dictionary['type'])
    stype = int(dictionary['stype'])
    hits = 1
    interface.uid("INSERT INTO history (question,hits,type,stype) VALUES(\"%s\",%d,%d,%d)" %(question,hits,typ,stype))
    return interface.get_last_insert_id()

def check_question(question):
    data = interface.select("SELECT * FROM history WHERE LOWER(question) = \"%s\"" %(question))
    try:
        if len(data) != 0:
            row = data[0]
            interface.uid("UPDATE history SET hits = hits + 1 WHERE id = %d" %(row[0]))
            return row[0]
        else:
            return False
    except Exception as e:
        print(e)
        return False
def view_questions(typ):
    data = interface.select("SELECT id FROM type_table WHERE LOWER(type) = '%s'" %(typ.lower()))
    type_id = data[0][0]
    data = interface.select("SELECT question FROM history WHERE type = %d" %(type_id))
    questions = []
    for row in data:
        questions.append(row[0])
    return questions
def related_question(typ,stype):
    data = interface.select("SELECT id FROM type_table WHERE LOWER(type) = '%s'" %(typ.lower()))
    print(typ)
    type_id = data[0][0]
    data = interface.select("SELECT stypeid FROM stype_table WHERE LOWER(stype) = '%s'" %(stype.lower()))
    stype_id = data[0][0]
    data = interface.select("SELECT question FROM history WHERE type = %d and stype = %d ORDER BY hits DESC" %(type_id,stype_id))
    rel_questions = []
    for row in data:
        rel_questions.append(row[0])
    return rel_questions
def connect():
    global interface
    interface = mysql.MySQLInterface("root","root","aptitude_engine")
def disconnect():
    global interface
    interface.close()
