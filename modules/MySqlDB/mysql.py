#!/usr/bin/python3
import MySQLdb
class MySQLInterface:

    #constructor for class
    def __init__(self,un,pw,db,host="localhost"):
        self.__dbname = db;
        self.__db = MySQLdb.connect(host,un,pw,db)
        self.__cursor = self.__db.cursor()

    # database commit
    def commit(self):
        self.__db.commit()

    # database rollback
    def rollback(self):
        self.__db.rollback()

    # used to fetch data one at a time
    def next_data(self):
        return self.__cursor.fetchone()

    # fetch all data
    def all_data(self):
        return self.__cursor.fetchall()

    #used to get the row count of cursor
    def row_count(self):
        return self.__cursor.rowcount()

    #select query function with option for all data or one
    def select(self,query,all=True):
        try:
            self.__cursor.execute(query)
            if all:
                return self.all_data()
            else:
                return self.next_data()
        except Exception as e:
            raise

    #update insert delete command with transaction support
    def uid(self,query,trans = False):
        try:
            self.__cursor.execute(query)
            if not trans:
                self.commit()
        except Exception as e:
            raise

    #multiple update insert delete command with transaction support
    def uids(self,querys,trans = False):
        try:
            for query in querys:
                self.__cursor.execute(query)
            if not trans:
                self.commit()
        except Exception as e:
            raise

    # used to close the connection with database typically called when all
    # operations are completed with the database
    def get_last_insert_id():
        return self.__cursor.lastrowid

    def close(self):
        self.__db.close()
