# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:15:28 2019

@author: ATUL SHARMA
"""

a=0
def hello():
    global a
    print("hello world")
    if(a<5):
        a=a+1
        hello()
hello()   