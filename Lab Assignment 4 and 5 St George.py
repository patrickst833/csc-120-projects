#!/usr/bin/env python
# coding: utf-8

# In[1]:


##lAB ASSIGNMENT 4 AND 5
# AUTHOR: [Patrick St George]
# DATE: [10/8/2024]

#instructions:
# rename this file LabAssignmentFour+your lastname for eg. LabAssignmentFourDebrah

#submission:
# 1. Submit to brightspace
# 2. upload to your git account. 


# In[2]:


##Assignment Four (4) Functions

#Question One

# Write a function add_numbers(a,b) which takes two parameters adds them and returns the result.
# Don't forget to test your function

def add_numbers(a,b):
    return a + b
number1 = float(input("Enter the first number"))
number2 = float(input("Enter the second number"))

result = add_numbers(number1, number2)
print("Sum:", result)


# In[4]:


#Question two

# Write a function get_min_max(list_numbers) which returns the mininum and maximum of values from the list
# Don't forget to test your function

new_list = [10,45,2,11,17,23,1,50,7,14]

largest_number = max(new_list)
minimum_number = min(new_list)
print('The maximum number in the list is:',largest_number)
print('The minimum number in the list is:',minimum_number)


# In[11]:


#Question three

# Given two integers, return 'The sum of the integers equals 40' if the sum is equal to 40. If not return 'The sum is not equal to 40'
# Don't forget to test your function

number1 = float(input("Enter the first number"))
number2 = float(input("Enter the second number"))

num = (number1 + number2)
if num == 40:
    print("The sum of the integers equals 40")

else:
    print("The sum is not equal to 40")


# In[92]:


#Question four

# Write a function the prints the even numbers from a given list. 
# Don't forget to test your function.

list1 = [2,48,5,53,82,24]

for num in list1:

    if num % 2 == 0:
        print(num, end=" ")


# In[39]:


#Question five

# Write a function such that when there are two numbers passed to it only the product is return if the product 
# is equal to or lower than 500, else return their sum.
#Don't forget to test your function. 

def multiply(num1, num2):
    product = num1*num2
    if product <= 500:
        return product
    else:
        return num1 + num2

# Testing with an example

result1 = multiply(5,20)
result2 = multiply(40,20)
print(result1)
print(result2)


# In[44]:


#Question six

# Write a function to check if the first and the last number of a given list is the same. 
# If they are the same then return true else return false. 

def list(my_list):

    if(my_list):
        return my_list[0] == my_list[-1]
        return false

# Testing with an example

print(list([1,2,3,4,5,1]))
print(list([1,2,3,4,5,3]))


# In[62]:


#Question seven

# Write a function which calculates the income tax when a given income take is supplied as an argument. 
# use the information below to calculate the tax required. 
# Taxable Income                     Rate(in %)
#  First $5000                        0
#  Next  $5000                        15
#  Remaining                          25

# Kindly read on how income tax is calculated. 
# Don't forget to test your function. 

def income_tax(income):
    if income <= 5000:
        return 0
    elif income <= 10000:
        return (income - 5000) * .15
    else:
        tax = (5000 * 0) + (5000 * .15)
        tax += (income - 10000) *.25
        return tax

income = float(input("Enter your income"))
tax = int(income_tax(income))
print("Your income tax is:", tax)
    


# In[81]:


##Assignment Four (5) Data structures

#Question eight

# A. Create a dictionary called fruit_store it should be empty. 
# B. Add the following fruit-unit_price pair to the dictionary you created. 
#  "Banana":4
#  "Pear": 2
#  "Apple":3
# C. Add a new fruit-unit_price to the dictionary above 
#    "Watermelon": 6
# D. Assuming the quantity of Banana is 30, Pear is 40, Apple is 70 and finally watermelon is 60
#  i. How much is the total value of our inventory. 
# E. Print out the list of fruits and their unit_price in our store. 

# A.

fruit_store = {
    "Banana":4,
    "Pear":2,
    "Apple":3,
}

def add_product(store, fruit, price):
    store[fruit] = price 
add_product(fruit_store,'Watermelon', 6)

quantities = {
    "Banana": 30,
    "Pear": 40,
    "Apple": 70,
    "Watermelon": 60
}

total_value = sum(fruit_store[fruit] * quantities[fruit] for fruit in fruit_store)
print(f"Total value of inventory: ${total_value}")

print("Fruit store fruit prices:")
for fruit, price in fruit_store.items():
    print(f"{fruit}: ${price}")

    


# In[86]:


#Question nine

# Given a list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] extract sublist [2, 3, 4] using slicing

mynew_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(mynew_list)

sub_list = mynew_list[2:5]
print(sub_list)


# In[89]:


#Question ten

# Given a list animals = ['cat', 'dog', 'rabbit', 'mouse', 'elephant', 'tiger'] replace the middle two elements with
# ['lion','skunk'] using slicing and replacing.

animals = ['cat', 'dog', 'rabbit', 'mouse', 'elephant', 'tiger']
print("Originals:",(animals))

animals[2:4] = ['lion','skunk']
print("Replacements:",(animals))


# In[ ]:




