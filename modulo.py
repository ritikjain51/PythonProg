# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:58:03 2019

@author: ATUL SHARMA
"""

a=int(input("enter a number to find mod"))
b=int(input("enter a num for mod "))
if(a>b):
        print(a,'%',b,'=',a % b)
elif(b>a):        
          print(b,'%',a,'=',b % a)
elif(b==0):                   
           try:
               print(a,'%',b,'=',a % b)
           except ZeroDivisionError:         
                   print(" please enter an another number")
    