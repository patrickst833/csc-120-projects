#!/usr/bin/env python
# coding: utf-8

# In[85]:


# Question 1

celsiustemp = float(input("Enter the temperature in Celsius: "))

fahrenheittemp = (celsiustemp*9/5)+32

print("The temperature in Fahrenheit is:",fahrenheittemp)


# In[86]:


# Question 2

num1 = 2
num2 = 4
num3 = 6
num4 = 8
num5 = 10

sum = (num1 + num2 +num3 +num4 +num5)
mean = (num1 + num2 +num3 +num4 +num5)/5

print("The sum of numbers is:", sum)
print("The mean of numbers is:", mean)


# In[87]:


# Question 3

value1 = input("Enter first number: ")
value2 = input("Enter second number: ")

total = int(value1)**3 + int(value2)**3

print(total)


# In[88]:


# Question 4

p=float(input("Enter the principle amount:"))
t=int(input("Enter the time(years):"))
r=float(input("Enter the rate:"))
simpleinterest=(p*r*t)/100
print("The simple interest is:", simpleinterest)


# In[89]:


# Question 5

r=float(input("Input the radius of the circle:"))

import math

area=(math.pi)*r**2

print("The area of the circle is:",area)


# In[91]:


# Question 6

day=int(input("Enter number of days"))
hours=24*day
minutes=60*hours
seconds=60*minutes
print("hours=",hours)
print("minutes=",minutes)
print("seconds=", seconds)


# In[92]:


# Question 7

hourly_wage = input("Please enter your hourly wage: ")

print("Hourly wage: ")
print(hourly_wage)
print("Hours worked: ")
print(hours_worked)

hours_worked = input("How many hours did you work this week? ")


# In[98]:


# Question 8

width=float(input("Enter the Width: "))
height=float(input("Enter the Height: "))

print("Value is: " ,width // 2, "and type is:" ,type(width//2))
print("Value is :" ,width / 2.0 ,"and type is:" ,type(width / 2.0))
print("Value is :" ,height / 3 ,"and type is:" ,type(width / 3))
print("Value is :" ,1 + 2 * 5,"and type is:" ,type(1 + 2 * 5))


# In[97]:


# Question 9

weight=float(input("Enter your weight(lbs): "))
height=float(input("Enter your height(inches): "))
BMI=(weight/(height**2))*703

print("BMI =",BMI)


# In[96]:


# Question 10

name = input("Your name")
print("Welcome to Python programming",name)

