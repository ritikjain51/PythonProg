# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:23:14 2019

@author: ATUL SHARMA
"""


X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
      for j in range(len(X[0])):
          result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)