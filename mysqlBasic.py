"""
mysql: database is use to store the content. store of content in database will be non-volatile

library to use:
    import mysql.connector    #for download write pip install mysql_connector

functions to use:
    connect: settings for mysql
    cursor: makes the accessing of database line by line
    execute: runs the querry of database
    
querries:
    create database nameDATABASE
    show databases
    create table tableName(coulmns)
    delete table
    commit;
    alter table
    insert into table
    select * from table

import mysql.connector
obj=mysql.connector.connect(
        user='root',
        password='',
        host='localhost'
        )
mycursor=obj.cursor()
mycursor.execute('show databases')
for i in mycursor:
    print(i)
    
"""

import mysql.connector
obj=mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='test'
        )
a='raju ji'
b=3
mycursor=obj.cursor()
#mycursor.execute('create database samyak')
mycursor.execute('create table student(id int,name VARCHAR(255),address VARCHAR(255))')
mycursor.execute('insert into student values({0},"{1}","newai")'.format(b,a))
mycursor.execute('commit;')
mycursor.execute('select * from student')
for i in mycursor:
    print(i)