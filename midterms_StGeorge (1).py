#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#MIDTERM EXAMINATION
#DUE DATE SUNDAY 27TH OCTOBER 11:59
#SAVE THE FILE AS midterms_LASTNAME
#NAME: Patrick St George


# In[11]:


##GENERAL PROGRAMMING
#QUESTION ONE
#Write a function called list_stats that, given a list of numbers, prints the minimum,
#maximum, and average of the numbers in the list. 

def list_stats(list):
    return min(list), max(list)

list = [40,54,27,4,34,9,23]
           
the_minimum, the_maximum = list_stats(list)

print(f'The minimum of the list is: {the_minimum}')
print(f'The maximum of the list is: {the_maximum}')
import statistics

average = statistics.mean(list)


print('The average of the list is:',average)


# In[99]:


#QUESTION TWO:
#write a program that prompts the user to enter two positive
#integers w and z ensure that w < b and the prints the list of all 
#perfect squares that are between a and b inclusive

def practice():
    while True:
        try:
            w = int(input("Enter the first positive integer (w): "))
            z = int(input("Enter the second positive integer (z): "))
            if w < z and w > 0 and z > 0:
                break
            else:
                print("Please ensure that w < z and both are positive integers.")
        except ValueError:
            print("Invalid input. Please enter positive integers.")

    print(f"Perfect squares between {w} and {z} (inclusive):")
    for i in range(int(w**0.5), int(z**0.5) + 1):
        square = i * i
        if square >= w and square <= z:
            print(square)

practice()


# In[95]:


#QUESTION THREE:
#Consider the code below and complete it.
#define your own list to test it. 

def doubleList(numberList):
    for number in numberList:
        print(number * 2)  

numberList = [3, 1, 5]

doubleList(numberList)


# In[90]:


#QUESTION FOUR:
#Write a python function to find common elements in two lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# ouput shold be 4

def common_list_elements(list1, list2):
    for element in list1:
        if element in list2:
            return element  
    return None  


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = common_list_elements(list1, list2)


if common is not None:
    print(common)  
else:
    print("No common elements")



# In[37]:


#QUESTION FIVE:
#Write a function in python which takes three arguments
#and returns the maximum of the three numbers. 
#do not use max() function

def maximum_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

#Testing
a = 10
b = 14
c = 12
print(maximum_of_three(a, b, c)) 
    


# In[45]:


#QUESTION SIX (indexing and slicing):
#Given the list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#write the code that does the following
#1. Print the first three numbers
#2. Print the last three numbers
#3. Reverse the list using slicing

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[0:3])

print(numbers[7:10])

numbers.reverse()
print(numbers)


# In[51]:


#QUESTION SEVEN:
#Given a dictionary as follows
#write the code to find the student with the highest grade
student_grade = {
    "Jane Doe":75,
    "John Smith":80,
    "George Owell":60,
    "Prince Jeffery":70,
    "Siri Alexa":67
}

for student, grade in student_grade.items():
    if grade > highest_grade:
        highest_grade = grade
        highest_student = student

print(f"The student with the highest grade is {highest_student} with a grade of {highest_grade}.")


# In[54]:


##EXPLORATORY DATA ANALYSIS
#QUESTION EIGHT:
#Complete the following code

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#1.defining the data
housing_data = pd.DataFrame({
    "income":[200.0, 150.0, 80.0, 120.0, 450.0, 100.0, 500.0, 75.0, 300.0, 350.0],
    "hse_price": [140.0, 90.0, 50.0, 100.0, 450.0, 100 , 200, 180, 150, 200],
    "hse_type": ['sf','th','co','cs', 'rh','sf', 'rh', 'co', 'th','th']
})

df=housing_data
#2.performing the basic eda
print(housing_data.info()) #displaying info about the dataframe

print(housing_data.head()) #displaying the first five rows.

#3.descriptive statistics
print('statistical summary of the data')
print(df.describe())

#4.check if there are missing values
print('check to see missing values in the data')
print(df.isnull().sum())

#5.five-number statistics summary. 
#use boxplot to do this.
#house price distribution by house type. 
sns.boxplot(x='hse_type', y='hse_price', data=df)
plt.title('House price distribution by house type')
plt.show()

#6.Is there any correlation between income and hse_price
#how will you determine that.
correlation = df['income'].corr(df['hse_price'])
print(f'Correlation between income and hse_price is:{correlation}')
                        



# In[55]:


#QUESTION NINE
#Using the attached data file for cars
#perform an EDA on the data. 
#follow the example during the lecture and the practice sessions

#1.Load libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[56]:


#2.Import the data
df = pd.read_csv('data.csv')


# In[65]:


#3. rename the columns
#uncomment the code below and replace...
#the car_data with the variable for your dataframe.
df = df.rename(columns={"Engine Fuel Type": "Fuel", "Number of Doors":"Doors", "Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })
df.head(5)


# In[66]:


#4.Inspect the data
print('check first five sample of data')
print(df.head())


# In[67]:


#5.Clean the data
#check if there are missing values
print('check to see missing values in the data')
print(df.isnull().sum())


# In[104]:


#6.Perform a univariate analysis 
#choose one(numeric) variable
#use histogram to check the distribution
#use box plots to identify outliers
sns.histplot(df['Price'], bins=30, kde=True)
plt.title('Distribution of Price')
plt.show()

sns.boxplot(x='Price', data=df)
plt.title('Price Distribution')
plt.show()


# In[77]:


#7.Perform a bivariate analysis
#using Vehicle size and Price
#plot a bar chart 
sizes = df['Vehicle Size'].unique()
avg_prices = []

for size in sizes:
    avg_price = df[df['Vehicle Size'] == size]['Price'].mean()
    avg_prices.append(avg_price)

# Plotting the bar chart
plt.bar(sizes, avg_prices, color=['blue', 'orange', 'green'])
plt.xlabel('Vehicle Size')
plt.ylabel('Average Price')
plt.title('Average Vehicle Price by Size')
plt.show()


# In[80]:


#QUESTION TEN
#determine if there is any correlation between price and popularity
#Can you explain the value 
correlation = df['Price'].corr(df['Popularity'])
print(f'Correlation between Price and Popularity is:{correlation}')

#This is a very weak negative correlation relationship between price and popularity so as prices increases the popularity might slighty decrease


# In[ ]:




