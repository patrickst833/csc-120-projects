#!/usr/bin/env python
# coding: utf-8

# # Lab Assignment Seven 
# ### INFERENTIAL STATISTICS
# 
# <h4>Submission Instructions</h4>
# <ol>
# <li><h5>Save the file as <b>labAssignment7+lastname</b>. Kindly submit in the <b>.ipynb</b> format</h5></li>
# <li><h5>Upload to Brightspace</h5></li>
# </ol>
# <h4>Dataset: Tips</h4>
# <h4>Source: Seaborn library</h4>
# <h4>example:</h4>
# <blockquote>
#     <code>tips = sns.load_dataset('tips')</code>
# </blockquote>
# <h4>Step One: Data Preparation (20 points)</h4>
# <ol>
#     <li>Import the libraries</li>
#     <li>load the data into a dataframe as show above</li>
# </ol>

# In[1]:


#import the libraries
import pandas as pd
import numpy as np
import seaborn as sns

tips = sns.load_dataset('tips')
tips.head()


# <h4>Step Two: Descriptive statistics (20 points) </h4>
# <ol>
#     <li>Use appropriate functions to compute the following:</li>
#     <ul>
#         <li>Mean</li>
#         <li>Median</li>
#         <li>Standard deviation</li>
#     </ul>
#     <li>Perform any other additional descriptive stats tasks</li>
# </ol>

# In[2]:


#Descriptive statistics
#1 (Mean, Median, and Standard deviation)
#finding the mean
mean_tip = round(tips['tip'].mean(),3)
print(f'The average tip is: {mean_tip}')

#finding the median
median_tip = tips['tip'].median()
print(f'The median of tips is: {median_tip}')

#Standard deviation
std_dev_tip = round(tips['tip'].std(),3)
print(f'The standard deviation from the mean is: {std_dev_tip}')

#2 (Any other additional descriptive stats tasks)
#mode
mode_day = tips['tip'].mode()
print(f'The most frequent day of tipping is: {mode_day}')

#range
range_tip = tips['tip'].max() - tips['tip'].min()
print(f'The range for tips is: {range_tip}')

#variance
variance_tip = round(tips['tip'].var(),3)
print(f'The variance of the tips is: {variance_tip}')


# <h4>Step Three: Hypothesis testing (20 points)</h4>
# <ol>
#     <li>Perform a <b> two-sample t-test</b> to determine if the <b>average total_bill</b> differs for</li>
#     <ul>
#         <li>smokers</li>
#         <li>non-smokers</li>
#     </ul>
#     <li>If we assume the mean of the tips to be 3.0, peform a <b>One-sample t-test </b> to decide whether it is accurate</li>
#     <ul>
#         <li><b>Null Hypothesis (H0): The mean tip is 3.0 </b></li>
#         <li><b>Alternate Hypothesis (H1): The mean tip is not equal to 3.0 </b></li>
#     </ul>
#     <li>Follow the example we did in class to understand</li>
#     <li>Kindly indicate what you infer from the t-statistic and p-values for:</li>
#     <ul>
#         <li><b>One-sample t-test</b></li>
#         <li><b>Two-sample t-test</b></li>
#     </ul>
# </ol>

# In[19]:


#load data
from scipy import stats as st

#1 two-sample t-test
smokers_tips = tips[tips['smoker']=='Yes']['total_bill']
non_smokers_tips = tips[tips['smoker']=='No']['total_bill']

t_test_results = st.ttest_ind(non_smokers_tips, smokers_tips)
print(t_test_results)

#2 one-sample t-test
t_test_result = st.ttest_1samp(tips['tip'],3.0)
print(t_test_result)

#4 Interpretation
#One-sample t-test: The t-statistic is -1.3388 which means that the sample mean is lower than the hypothesized mean
#One-sample t-test: The P-value is 0.1820 which is greater than the level of significance of 0.05 and we fail to reject the null hypothesis and that there is no significant difference between the sample mean and the hypothesized value.
#Two-sample t-test: The t-statistic is -0.0194 and that means there is a small difference between the average total bills for smokers and non-smokers and that there is no difference between the groups being tested.
#Two-sample t-test: The P-value is 0.0922 is way bigger than the 0.05 signficance level so we fail to reject the null hypothesis which means that there is no significant difference between the average total bills of smokers vs. non-smokers


# <h4>Step Four: Confidence Interval (20 points)</h4>
# <ol>
#     <li>Write the code to find the standard_error</li>
#     <li>Use the appropriate <b>scipy</b> function to determine the confidence interval</li>
#     <li>Indicate what the confidence interval mean</li>
# </ol>
# 

# In[14]:


#Import data
from scipy.stats import sem

#standard error
mean_tip = round(tips['tip'].mean(),3)
std_error_mean = round(sem(tips['tip']),3)
print(f'The standard error is: {std_error_mean}')

#confidence interval
confidence_interval = st.norm.interval(confidence=0.95,loc=mean_tip,
                                       scale = std_error_mean)
print(f'The confidence interval is: {confidence_interval}')
#This means that the true population mean will lie in this interval 95% of the time


# <h4>Step Five: Visualization (20 points)</h4>
# <ol>
#     <li>Perform the following visualizations</li>
#     <ul>
#         <li>The distribution of total_bill for smokers and non-smokers</li>
#         <li>A histogram of tips</li>
#         <li>A distribution of tips across the time of the meal</li>
#     </ul>
# </ol>

# In[25]:


#The distribution of total_bill for smokers and non-smokers
import matplotlib.pyplot as plt
sns.boxplot(x ='smoker', y = 'total_bill', data=tips)
plt.title('Smoker vs. Non-Smokers bill')
plt.xlabel('Smoker')
plt.ylabel('Total Bill')
plt.show()

#A histogram of tips
sns.histplot(tips['tip'], bins=20, kde=True)
plt.title('Distribution of Tips')
plt.show()

#A distribution of tips across the time of the meal
sns.boxplot(x ='time', y = 'tip', data=tips)
plt.title('A Distribution of tips across the time of the meal')
plt.xlabel('Time')
plt.ylabel('Tip')
plt.show()


# In[ ]:




