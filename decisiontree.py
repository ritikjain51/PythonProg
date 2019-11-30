# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:06:15 2019

@author: ATUL SHARMA
"""

import pandas as pd
import numpy as np
ddf=pd.read_excel(open('record.xlsx','rb'))
x=ddf.iloc[:,1:-1]
y=ddf.iloc[:,-1]
x=np.array(x)
y=np.array(y)
l=x[:,0]
a=np.unique(l)
l=list(l)
l.count(a[0])
l.count(a[1])
m=y
b=np.unique(m)
m=list(m)
m.count(b[0])
m.count(b[1])
c1=0
c2=0
c3=0
c4=0
c=float()
for i in range(len(l)):
        if(a[1]==l[i]):
            if(b[0]==m[i]):
               c1=c1+1
            else:
               c2=c2+1
for i in range(len(l)):
        if(a[0]==l[i]):
            if(b[0]==m[i]):
               c3=c3+1
            else:
               c4=c4+1
              
p1=float()
p2=float()               
gini1=float()
d1=float()
p1=c1/(c1+c2);
p2=c2/(c1+c2);
d1=1-((p1)**2+(p2)**2)
gini1=d1
p3=float()
p4=float()               
gini2=float()
d2=float()
p3=c3/(c3+c4);
p4=c3/(c3+c4);
d2=1-((p3)**2+(p4)**2)
gini2=d2
ginip=float()
d3=(d1*(c1+c2)/10+d2*(c3+c4)/10)
ginip=d3



    
               
              
                
            
            
            

    
    
    
    
    
    


