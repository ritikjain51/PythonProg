# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 23:55:39 2019

@author: ATUL SHARMA
"""

num=int(input("enter a number for factorial"))
factorial=1
if (num<1):
    print("the factorial of negetive num is not possible")
elif(num==0):
    print("the factorial of zero is one")
else: 
 for i in range (1,num + 1):
 factorial=factorial*i
 print("the factorial of",num,"is", factorial) 
  