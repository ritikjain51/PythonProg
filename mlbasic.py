

import pandas as pd
import numpy as np
ddf=pd.read_csv(open('Churn_Modelling.csv','rb'))
x=ddf.iloc[:,3:-1]
y=ddf.iloc[:,-1]
x=np.array(x)
y=np.array(y)

from sklearn.preprocessing import LabelEncoder
lbl=LabelEncoder()
x[:,1]=lbl.fit_transform(x[:,1])
x[:,2]=lbl.fit_transform(x[:,2])
print (x)
from sklearn.preprocessing import OneHotEncoder
oe=OneHotEncoder(categorical_features=[1])
x=oe.fit_transform(x).toarray()
print (x)
from sklearn.preprocessing import Imputer
i=Imputer()
x=i.fit_transform(x)
print (x)
from sklearn.preprocessing import StandardScaler
j=StandardScaler()
x=j.fit_transform(x)
print (x)
from sklearn.cross_validation import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5)