# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:04:04 2019

@author: ATUL SHARMA
"""

import pandas as pd
import numpy as np
ddf=pd.read_excel(open('irisdataset.xlsx','rb'))
x=ddf.iloc[:101,0:2]
y=ddf.iloc[:101,-1]
x=np.array(x)
y=np.array(y)
i=float()
j=float()
result=[]
us=[]
z=[]
a=float(input("enter the sepel's length-"))
b=float(input("enter the sepel's width-"))
for i in range(len(x)):
    d=np.sqrt((abs(x[i][0]-a)**2)+(abs(x[i][1]-b)**2))
    result.append(d)
    us.append(d)
result=np.sort(result)
for i in range(3):
    for j in range(len(us)):
                if(result[i]==us[j]):
                    z.append(j)
                    
irissatosa=irisversicolour=0
for i in range(len(z)):
    if(z[i]<=51):
     irissatosa=irissatosa+1 
    else:
      irisversicolour=irisversicolour+1      
if(irissatosa>irisversicolour):
    print("plant is  irissatosa")
else:
 print("plant is  irisversicolour") 
