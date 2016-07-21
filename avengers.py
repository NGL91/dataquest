
# coding: utf-8

# In[5]:

import os
os.getcwd()
os.chdir('/home/abc/workspace/machinelearning/data/avengers')
os.getcwd()
os.listdir()


# In[12]:

import pandas as pd
avengers = pd.read_csv('avengers.csv', encoding='latin1')

#Print shape: number of columns, number of rows
avengers.shape
#Print all labels
avengers.columns.values

#Plot year columns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
avengers['Year'].hist()


# In[76]:

#Because avenger heroes only appear since 1960, so we will remove rows have Year < 1960
true_avengers = avengers[avengers['Year']>=1960]
true_avengers['Year'].hist()


# In[79]:

def count_death(row):
    death1 = 1 if row['Death1'] == 'YES' else 0
    death2 = 1 if row['Death2'] == 'YES' else 0
    death3 = 1 if row['Death3'] == 'YES' else 0 
    death4 = 1 if row['Death4'] == 'YES' else 0
    death5 = 1 if row['Death5'] == 'YES' else 0 
    
    deaths= death1 +death2 + death3 + death4 + death5
    return deaths

# pd.options.mode.chained_assignment = None  # default='warn'
# true_avengers['Deaths'] = true_avengers.apply(lambda row: count_death(row), axis=1)
true_avengers.loc[:,'Deaths'] = true_avengers.apply(count_death, axis=1)
true_avengers.loc[:,'Deaths'].hist()



# In[88]:

joined_accuracy_count = (2015- true_avengers['Year'] == true_avengers['Years since joining'])

joined_accuracy_count = [1 for item in joined_accuracy_count if item ]
joined_accuracy_count = sum(joined_accuracy_count)
joined_accuracy_count


# In[ ]:



