

"""
pandas: this library is use to import or export content from different files
having different formats.

librry to use:
pandas
xlrd(this library is run in background)
xlsxwriter

functions to use:
1)to write something in excel or csv files:
open: to open a file by giving the permissions: w,r,rb,x
ExcelWriter: this function further creates an object which helps in writing content
DataFrame: this convert the data into data frame format.
to_excel/to_csv:-these are use to select the type of file and also write the content
save: when things get write we can only see the content in a file when we save
the changes.


2)to read the content of a file:
open: to open a file by giving the permissions.
read_excel/read_csv: this function actually reads the content of a file in
data frame format.
now convert the data in required format.




write

import pandas as pd
import xlsxwriter
df=pd.DataFrame({'x':[3,4,5,6,3,2,5,6,4,3],'y':[6,5,3,4,6,6,4,3,5,6],'z':[1,1,1,1,1,0,0,0,0,0]})
writer=pd.ExcelWriter('pandas.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1')
writer.save()

read
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ddf=pd.read_csv(open('Churn_Modelling.csv','rb'))
"""
#reading content attribute wise method1
surename=ddf['x']
balance=ddf['y']
surename=np.array(surename)
balance=np.array(balance)
"""
surename=ddf.iloc[0:10,[0,3]]
balance=ddf.iloc[0:10,-1]
surename=np.array(surename)
balance=np.array(balance)

plt.title('churn_modelling')
plt.xlabel("surename")
plt.ylabel("balance")

plt.scatter(surename[:,0],surename[:,1],c=balance)
#plt.xlim(0,20)
plt.show()









