# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:35:57 2019

@author: ATUL SHARMA
"""

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] = result[i][j]+ X[i][k] * Y[k][j]
for r in result:
   print(r)