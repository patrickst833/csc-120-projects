#!/usr/bin/env python
# coding: utf-8

# In[19]:


#B.i
#Finding the variance and standard deviation of a list

import pandas as pd
import statistics as st

def find_var_std_dev(list):
    variance = st.variance(list)
    std_dev = st.stdev(list)

    return variance, std_dev

data = [25, 21, 32, 94, 35]
variance, std_dev = find_var_std_dev(data)

print('Variance:',variance)
print('std_dev:',std_dev)


# In[14]:


#B.ii
#Finding the covariance of 2 lists

import pandas as pd
import statistics as st

def find_covariance(list1, list2):
    
    df = pd.DataFrame({'list1': list1, 'list2': list2})
  
    cov_matrix = df.cov()
    
   
    covariance = cov_matrix['list1']['list2']
    
    return covariance


list1 = [2, 54, 23, 56, 3]
list2 = [45, 6, 75, 4, 89]


list_cov = find_covariance(list1, list2)

print(f"Covariance: {list_cov}")


# In[24]:


#C
#Finding the variance and standard deviation of a list

import pandas as pd
import statistics as st

def find_var_std_dev(list):
    variance = st.variance(list)
    std_dev = st.stdev(list)

    return variance, std_dev

Age = [61,60,60,60,60,59,59,59,59,59]
Height = [1.85,1.71,1.55,1.46,1.58,1.71,1.70,1.72,1.46,1.83]

age_var, age_std_dev = find_var_std_dev(Age)

height_var, height_std_dev = find_var_std_dev(Height)


print('Age Variance:', age_var)
print('Age Standard Deviation:', age_std_dev)
print('Height Variance:', height_var)
print('Height Standard Deviation:', height_std_dev)

def find_covariance(list1, list2):
    
    df = pd.DataFrame({'Age': Age, 'Height': Height})
  
    cov_matrix = df.cov()
    
   
    covariance = cov_matrix['Age']['Height']
    
    return covariance


list_cov = find_covariance(Age, Height)

print(f"Covariance: {list_cov}")

#The manual answers and the ones on python are the same


# In[ ]:




