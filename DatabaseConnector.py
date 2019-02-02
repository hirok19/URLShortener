#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 12:58:07 2019

@author: supaul
"""
import pysqlite3
import hashlib
class DatabaseConnector:
    cursor=None
    conn=None
    def __init__(self,path):
        try:
            self.conn = pysqlite3.connect(path)
            self.cursor=self.conn.cursor()
        except:
            print("Unable to initialize database")
      
    def createTable(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS urlTable (id,url)""")
        except Exception as e:
            print("Unable to create table")
            print(e)
        
    def insertURL(self,URL):
        key=self.getKey(URL)
        #print(type(key))
        insert_stmt = ("INSERT INTO urlTable (id,url) VALUES ('{0}','{1}');")
        statement=insert_stmt.format(key,URL)
        #print(statement)
        try:
            if(self.getURLFromKey(key) is None):
                self.cursor.execute(statement)
                self.conn.commit()
                print("Data inserted!")
            else:
                print("Data already present")
        except Exception as e:
            print("Unable to insert data")
            print(e)
            return None
        return key
    def getKey(self,URL):
        hashedKey=hashlib.md5(URL.encode()) 
        return hashedKey.hexdigest() 
        
    
    def getURLFromKey(self,key):
        insert_stmt=("SELECT url from urlTable where id='{0}';")
        statement=insert_stmt.format(key)
        #print(statement)
        try:
            self.cursor.execute(statement)
            rows = self.cursor.fetchall()
            if(len(rows)>0):
                return rows[0][0]
            else:
                return None
                

        except Exception as e:
            print("Unable to fetch URL")
            print(e)
            return None