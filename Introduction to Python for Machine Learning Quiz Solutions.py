#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Importing Libraries
import pandas as pd
import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew


# In[3]:


# Loading fuel data  
url='https://github.com/WalePhenomenon/climate_change/blob/master/fuel_ferc1.csv?raw=true'
fuel_data = pd.read_csv(url, error_bad_lines=False)


# # Question 1

# In[5]:


np.array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])


# In[74]:


from numpy import eye
eye(3)


# In[9]:


np.identity(3)


# # Question 2

# In[75]:


coal_1998 = fuel_data['fuel_cost_per_unit_burned'][(fuel_data['fuel_type_code_pudl'] == 'coal') & (fuel_data['report_year']==1998)]
coal_1994 = fuel_data['fuel_cost_per_unit_burned'][(fuel_data['fuel_type_code_pudl'] == 'coal') & (fuel_data['report_year']==1994)]

percentage_change = (sum(coal_1994)-sum(coal_1998))/100
print(percentage_change)


# # Question 3

# In[ ]:


# Could not answer this question but will search for the answer.


# # Question 4

# In[ ]:


'''
from question 6 the feature with missing values is the fuel_unit feature and it is a categorical type 
because its made up of categories of measurements.
The type of imputation I will use is Mode imputation which replaces missing values of 
a categorical variable by the mode of non-missing cases of that variable.
'''


# # Question 5

# In[85]:


years = range(1994,2019)
accum = 0
for year in years:
    get_data = fuel_data['fuel_cost_per_unit_delivered'][(fuel_data['report_year']==year)]
    average = sum(get_data)/len(get_data)
    if average > accum:
        accum = average
        new_year =year
        
print('Year-{}, Average-{}'.format(new_year,accum))


# # Question 6

# In[87]:


features = ['record_id','utility_id_ferc1','report_year','plant_name_ferc1','fuel_type_code_pudl','fuel_unit','fuel_qty_burned','fuel_mmbtu_per_unit','fuel_cost_per_unit_burned','fuel_cost_per_unit_delivered','fuel_cost_per_mmbtu']
for feature in features:
    p = fuel_data[feature].isnull()
    total = len(fuel_data[p == True])
    percent = (total/len(fuel_data))*100
    if total> 0:
        print('Feature: {}, Total: {}, Percent: {:.3f}'.format(feature,total,percent))


# # Question 7

# In[81]:


# skew_fqb is the skewness for the feature fuel quantity burned
skew_fqb = skew(fuel_data['fuel_qty_burned'])
print(skew_fqb)

# kurt_fqb is the kurtosis for the feature fuel quantity burned
kurt_fqb = kurtosis(fuel_data['fuel_qty_burned'])
print(kurt_fqb)


# # Question 8

# In[88]:


fuel_data.describe(include='all')


# # Question 9

# In[92]:


fuel_types = ['coal','waste','oil','gas']
accum = 100000
new_fuel_type = ''
for fuel_type in fuel_types:
    get_data = fuel_data['fuel_cost_per_unit_burned'][(fuel_data['fuel_type_code_pudl']==fuel_type)]
    average = sum(get_data)/len(get_data)
    if average<accum:
        accum=average
        new_fuel_type = fuel_type
    
print('Fuel Type-{}, Average-{}'.format(new_fuel_type,accum))


# # Question 10

# In[98]:


A = [1,2,3,4,5,6]
B = [13, 21, 34]
A.extend(B)
print(A)

