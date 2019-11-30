# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:25:59 2019

@author: ATUL SHARMA
"""
try:
    a=chr(input("enter the number"))
except ValueError:
    print("please enter only an integer value")
except NameError:
    print("please enter only alphabates" )
except TypeError:
    print("please enter a integer")
    
    
        