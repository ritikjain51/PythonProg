# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 09:32:43 2019

@author: ATUL SHARMA
"""

nterms=int(input("how many terms are requried?"))
n1=0
n2=1
count=0
if nterms<1:
     print("please enter a positive number")
elif nterms == 1:
     print("the fabonacci series upto",nterms,":")
     print(n1)
else:
     print("fabonacci series upto",nterms,":")
     while count<nterms:
     print(n1,end=',')       
     nth=n1+n2
     #for update the values
     n1=n2
     n2=nth
     count=count+1
     
     
     