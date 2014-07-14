#!/usr/bin/python
#-*- coding: utf-8 -*-
import mysql.connector
import config

connect = mysql.connector.connect(
    database=config.db,
    user=config.user,
    password=config.passwd,
    host=config.host
)

cursor = connect.cursor()
cursor.execute('select * from chefmozcuisine limit 10', ())
rows = cursor.fetchall()
print(rows)
cursor.close()
connect.close()