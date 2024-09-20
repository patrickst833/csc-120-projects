#!/usr/bin/env python
# coding: utf-8

# In[91]:


# Question 1

Age = int(input("What is your age? "))
Citizen = (input("Are you a U.S. citizen? "))

# Solution

if Age>=18 and Citizen >= 'yes':
    print("You are eligible to vote")

else:
    print("You are not eligible to vote")


# In[92]:


# Question 2

Year = (int(input("Type in a year: ")))

# Solution

if Year % 4 == 0:
        print(f"{Year} is a leap year.")
else:
     print(f"{Year} is not a leap year.")


# In[93]:


# Question 3

correct_password = "Assumption"

enter_password = input("Enter your password: ")

# Solution

if enter_password == correct_password:
    print("Password is the same. ")
    print("Password is correct. ")

else:
    print("Password is different. ")
    print("Password is incorrect. ")



# In[94]:


# Question 4

month_name = input("Input the name of Month: ")

# Solution

if month_name == 'February':
	print('Number of days: 28/29 days')
elif month_name in ('April', 'June', 'September', 'November'):
	print('Number of days: 30 days')
elif month_name in ('January', 'March', 'May', 'July', 'August', 'October', 'December'):
	print('Number of days: 31 day')
else:
	print('Error month name') 


# In[95]:


# Question 5

# Solution

total = 0
print('Before', total)
for item in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
    total+=item
    print(total,item)
print('After', total)


# In[96]:


# Question 6

numbers = [3,9,1,6,2,8]
smallest_so_far = numbers[0]

# Solution

for item in numbers:
    if item < smallest_so_far:
        smallest_so_far = item
print('The smallest number in the list is: ', smallest_so_far)


# In[97]:


# Question 7

# Solution

for i in range(100, 501):
    if i % 11 == 0 and i % 2 != 0:
        print(i)


# In[98]:


# Question 8

numbers = {-2, 13, -4, -5, -6, 10, 20, 30, -12}

# Solution

positive_sum = sum(num for num in numbers if num > 0)

print("The sum of positive numbers is:", positive_sum)


# In[99]:


# Question 9

# Solution

for i in range(1, 31):
    if i % 5 != 0:
        print(i)


# In[100]:


# Question 10

length = int(input("Enter length in cm: "))

# Solution

if length < 0:
    print("Entry is Invalid")
else:
    inch = length / 2.54
    print(length, "cm =", inch, "inches")

