# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:13:04 2019

@author: ATUL SHARMA
"""

import pandas as pd
import numpy as np
ddf=pd.read_excel(open('adult_salary_dataset.xlsx','rb'))
x=ddf.iloc[:,0:-1]
y=ddf.iloc[:,-1]
x=np.array(x)
y=np.array(y)
from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
print (x[:, 1])
x[:,1]=lb.fit_transform(x[:,1])
x[:,3]=lb.fit_transform(x[:,3])
x[:,5]=lb.fit_transform(x[:,5])
x[:,6]=lb.fit_transform(x[:,6])
x[:,7]=lb.fit_transform(x[:,7])
x[:,8]=lb.fit_transform(x[:,8])
x[:,9]=lb.fit_transform(x[:,9])
x[:,13]=lb.fit_transform(x[:,13])
print (x[:, 1])
from sklearn.preprocessing import OneHotEncoder
i=OneHotEncoder(categorical_features=[3])
x=i.fit_transform(x).toarray()
from sklearn.preprocessing import StandardScaler
j=StandardScaler()
x=j.fit_transform(x)
from sklearn.cross_validation import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5)
from sklearn.preprocessing import StandardScaler
k=StandardScaler()
xtrain=k.fit_transform(xtrain)
xtest=k.fit_transform(xtest)
for i in range(len(y)):
    if(y[i]==' <=50K'):
        y[i]=0
    else: 
        y[i]=1
    





