# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:25:14 2019

@author: ATUL SHARMA
"""

import pandas as pd
import numpy as np
ddf=pd.read_excel(open('k-nnalgo.xlsx','rb'))
x=ddf.iloc[:,0:-1]
y=ddf.iloc[:,-1]
x=np.array(x)
y=np.array(y)
i=int()
j=int()
result=[]
us=[]
z=[]
a=int(input("enter the quality of cottan-"))
b=int(input("enter the price of cottan-"))
#for getting list only for distance elements
for i in range(len(x)):
    d=np.sqrt((abs(x[i][0]-a)**2)+(abs(x[i][1]-b)**2))
    result.append(d)
    us.append(d)
result=np.sort(result)
for i in range(3):
    for j in range(len(us)):
                if(result[i]==us[j]):
                    z.append(j)
B=G=0
for i in range(len(z)):
    if(z[i]>=3):
      B=B+1
    else:
        G=G+1
if(G>B):
    print("samplde is good")
else:
 print("sample is bad")