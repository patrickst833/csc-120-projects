#!/usr/bin/env python
# coding: utf-8

# 

# In[ ]:





# <h4>FINAL PROJECT STATS PROGRAMMING FALL 2024 </h4>
# <h5>Follow the instructions carefully to complete the project.</h5>
# <blockquote>
#     <ol>
#         <li>Make any reasonable assumptions in coding</li>
#         <li>The dataset is attached to the brightspace assignment</li>
#         <li>As much as possible use familiar code</li>
#         <li>Save file as final_project + lastname </li>
#     </ol>
# </blockquote>
# <p><h5>PREAMBLE</h5>
#     The dataset contains data about salaries and years of experience. We want to do a full statistical analysis on this dataset. 
# </p>

# <h5><b>STEP ONE: loading libraries and the data</b></h5>

# In[108]:


#Loading the important libraries to use

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yfin
import statistics as st
import math
from scipy.stats import sem
import datetime as dt
#Loading Dataset
df = pd.read_csv('Salary_dataset.csv')


# <h5><b>STEP TWO: Perform a full Exploratory Data Analysis (EDA)</b></h5>

# In[140]:


#Inspect Data
#Basic data exploration
print('check first five sample of data')
print(df.head())
#general information about the data
print('general information about the data')
print(df.info())
#descriptive statistics
print('statistical summary of the data')
print(df.describe())
#Understand the number of rows and columns
print('number of rows and columns')
print(df.shape)


#Data cleaning
#checking for missing values
print('check to see missing values in the data')
print(df.isnull().sum())

#Univariate Analysis
#histogram of years of experience
sns.histplot(df['YearsExperience'], bins=20, kde=True)
plt.title('Distribution of years of experience')
plt.show()
#boxplot of salary
sns.boxplot(x=df['Salary'])
plt.title('Box Plot of Salary')
plt.show()
#use a countplot to count each year of experience 
sns.countplot(x='Salary', data=df)
plt.title('count of each salary')
plt.show()
#Scatterplot between Salary and Years of experience
sns.scatterplot(x='YearsExperience', y='Salary', data=df)
plt.show()
#heatmap
df = df[['YearsExperience', 'Salary']]
df_corr =df.corr()
print(df_corr)
sns.heatmap(df_corr, annot=True)
plt.show()

correlation = df['YearsExperience'].corr(df['Salary'])
print(f'Correlation: {correlation}')

#Bivariate Analysis
sns.boxplot(x='YearsExperience', y='Salary', data=df)
plt.show()
#Boxplot one variable
sns.boxplot(x=df['YearsExperience'])
plt.title('Box Plot of Years of Experience')
plt.show()


# <h5><b>STEP THREE: Perform a full Descriptive statistical analysis on the dataset</b></h5>

# In[89]:


#standard deviation
import statistics as st

import math


def find_var_std_dev(data_list):
    # Finding the mean of the list
    sum_list = 0
    for w in data_list:
        sum_list += w  

    mean_list = sum_list / len(data_list)  

    # Finding variance
    sum_var = 0
    for x in data_list:
        sum_var += (x - mean_list) ** 2 

    variance = sum_var / (len(data_list) - 1)  
    
    std_dev = math.sqrt(variance)
    
    return variance, std_dev

Salary_list = df['Salary']
YearsExperience_list = df['YearsExperience']

salary_var, salary_std = find_var_std_dev(Salary_list)
years_var, years_std = find_var_std_dev(YearsExperience_list)

print(f'The variance and standard deviation of Salary are: {round(salary_var, 3)} and {round(salary_std, 3)}')
print(f'The variance and standard deviation of Years of experience are: {round(years_var, 3)} and {round(years_std, 3)}')

#covariance matrix
def find_covariance(Salary_list, YearsExperience_list):
    meanx = st.mean(Salary_list)
    meany = st.mean(YearsExperience_list)

    sumxy = 0

    for i in range(len(Salary_list)):
        sumxy += (Salary_list[i] - meanx) * (YearsExperience_list[i] - meany)

    covxy = sumxy / (len(Salary_list) - 1)
    
    return covxy

Salary_list = df['Salary']
YearsExperience_list = df['YearsExperience']

covariance = find_covariance(Salary_list, YearsExperience_list)

print(f'The covariance between Salary and Years of Experience is: {round(covariance, 3)}')

#correlation matrix
corr_matrix = df.corr()
print(corr_matrix)

#heatmap
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation matrix for housing dataset")
plt.show()

#range
YearsExperience_range = df['Salary'].max() - df['Salary'].min()
print(f'The range for salary is: {salary_range}')
salary_range = df['YearsExperience'].max() - df['YearsExperience'].min()
print(f'The range for years of experience is: {YearsExperience_range}')

#Variance
var_salary = round(df['Salary'].std(),3)
print(f'The vairance of salary is: {var_salary}')
var_YearsExperience = round(df['YearsExperience'].std(),3)
print(f'The vairance of years of experience is: {var_YearsExperience}')

sns.boxplot(df['Salary'])
plt.title("Boxplot of Salary")
plt.show()
sns.boxplot(df['YearsExperience'])
plt.title("Boxplot of Years of Experience")
plt.show()


# <h5><b>STEP FOUR: Perform a full Inferential statistical analysis on the dataset</b></h5>

# In[101]:


#find the mean salary
#determine the standard error for the mean
#determine the confidence interval for the mean with a 95% confidence
#explain what the confidence interval means.
#mean
Salary = df['Salary']

mean_salary = np.mean(Salary)  
   
print(f'Descriptive stats for Salary: mean: {mean_salary}')
#standard error
std_error_mean = round(sem(df['Salary']),3)
print(f'The standard error of the mean is: {std_error_mean}')

#range for mean
range_mean_salary = round(df['Salary'].mean(),3)
upperbound_mean = range_mean_salary + std_error_mean
lowerbound_mean = range_mean_salary - std_error_mean
print(f'The true population mean is between {upperbound_mean} and {lowerbound_mean}')

#confidence interval
from scipy import stats as st

confidence_interval = st.norm.interval(confidence=0.95,loc=range_mean_salary,
                                       scale = std_error_mean)
print(f'The confidence interval is: {confidence_interval}')
#What this means is that the true population mean for salary is expected to lie between 66,194.05 and 85,813.95 and based on the sample data I am 95% confident that the true population mean salary is within this range


# In[107]:


#Hypothesis testing
#Alternative Hypothesis: Those with year of experience over 5 earn more in the population
#Null Hypothesis: The status quo remains the same. 
#Use the two sample t-test 
#explain the t-statistics and the p-value
group_1 = df[df['YearsExperience']<=5]['Salary']
group_2 = df[df['YearsExperience'] > 5]['Salary']

t_test_results = st.ttest_ind(group_1, group_2)
print(t_test_results)

#The t-statistic is -9.73 which is a large value and means that the sample mean of salaires for the group with less than 5 years is a lot lower than the sample mean of the group with over 5 years experience. The negative also means the direction of the difference means the group with mroe experiences earsn more than the gorup with less
#The p-value is 1.76 x 10^-10 is veru small and less than 0.05 so we can reject the null hypothesis that the status quo would remain the same


# <h5><b>STEP FIVE: Perform full linear regression</b></h5>

# In[139]:


#code goes here
#How much will someone with a work experience of 10years earn.

linear_reg = np.polyfit(df['YearsExperience'], df['Salary'], deg=1)
linear_reg

trend = np.polyval(linear_reg, df['YearsExperience'])

plt.figure(figsize=(10,6))
plt.scatter(df['YearsExperience'], df['Salary'])
plt.plot(df['YearsExperience'], trend, 'r')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

slope, intercept = linear_reg

years_of_experience = 10
predicted_salary_10_years = slope * years_of_experience + intercept

print(f"Predicted Salary for someone with 10 years of experience: ${predicted_salary_10_years:,.2f}")

plt.figure(figsize=(10, 6))
plt.plot(df['YearsExperience'], df['Salary'], label="Salary vs Experience")
plt.title('Salary vs Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

import statsmodels.api as sm
x_years = df["YearsExperience"]
y_salary = df["Salary"]
salary_years = pd.DataFrame({
    "YearsExperience":x_years,
    "Salary":y_salary})
corrMatrix = salary_years.corr()
corrMatrix

X = salary_years['YearsExperience']
y = salary_years['Salary']

X = sm.add_constant(X)
reg_model = sm.OLS(y,X).fit()
print(reg_model.summary())

y_hat = reg_model.predict(X)
plt.figure(figsize=(10,6))
plt.scatter(X['YearsExperience'], y , label = 'Data Points')
plt.plot(X['YearsExperience'], y_hat, color = 'red', label = 'Fitted Line')

time_value = float(input("Enter a value for time to predict: "))
y_hat = 2.485e+04 + 9449.9623 * time_value
print(f'The salary with {round(time_value,3)} years of experience is ${y_hat:,.2f}')


# In[ ]:




