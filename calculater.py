# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:28:59 2019

@author: ATUL SHARMA
"""

#simple calculater
# This function adds two numbers 
def add(x, y):
    c=x+y
    return c

# This function subtracts two numbers 
def subtract(x, y):
    c=x-y
    return c

# This function multiplies two numbers
def multiply(x, y):
    c=x*y
    return c

# This function divides two numbers
def divide(x, y):
    try:
        c=x/y
        return c
    except ZeroDivisionError:         
        print(" please enter an another number")
    
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter your choice:")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    c=add(num1,num2)
    print("the ans is",c)

elif choice == '2':
    c=subtract(num1,num2)
    print("the ans is",c)

elif choice == '3':
    c=multiply(num1,num2)
    print("the ans is", c)

elif choice == '4':
    c=divide(num1,num2)
    print("the ans is", c)
else:
   print("Invalid input")
   
import mysql.connector
obj=mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='calculater'
        )
mycursor=obj.cursor()
#mycursor.execute('create database calculater')
#mycursor.execute('create table data(num1 int,num2 int,c int)')
mycursor.execute('insert into data values({0},{1},{2})'.format(num1,num2,c))
mycursor.execute('commit;')
mycursor.execute('select * from data')
for i in mycursor:
    print(i)
    



