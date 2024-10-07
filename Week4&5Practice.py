# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#creating a function to greet.
def greet(name):
          print('Hello,',name,'! Welcome to Python Programming')

greet('George')


# +
def add_two_numbers(a,b):
    return a+b

#using the function

result = add_two_numbers(4,5)

print('The sum of the numbers are:',result)
print('The sum of the numbers are:',add_two_numbers(8,9))
# +
#function to calculate the area of a circle
#first one basic

import math
def calculate_area(radius):
    return math.pi*radius**2

print("Area of circle", calculate_area(10))


# +
#function to calculate the area of a circle
#second one

import math

def calculate_area():
    radius = input('Enter the radius of a circle')
    return math.pi * float(radius)**2

area_of_circle = calculate_area()

print('The area of the circle is:',area_of_circle)

# +
#function to calculate the area of a circle
#third one more matured

import math

def calculate_area():
    radius = input('Enter the radius of a circle')
    area = math.pi * float(radius)**2
    return area,radius

circle_area, circle_radius = calculate_area()

print(f'The area of a circle with radius:{circle_radius} is {circle_area}')

# +
##Inventory System

#defining the database
#key = item names
#values = quantities
inventory = {
    "Apple":90,
    "Banana":80,
    "Orange":40,
    "Pear":90
}

#print state of the inventory
print(inventory)

#function to add product to the inventory
def add_product(inventory, product, quantity):
    inventory[product] = quantity

#dunction to update quantity in the inventory
def update_quantity(inventory,product,newquantity):
    inventory[product] = inventory[product] + newquantity

#function to calculate total qauntity of products
def total_inventory_quantity(inventory):
    total_quantity = 0
    for product in inventory:
        total_quantity = total_quantity + inventory[product]
    return total_quantity


# +
#Example of how to use the basic inventory application

#add a new product to the inventory
add_product(inventory, "Watermelon",100)
print('Adding new product: ',inventory)

#increasing the quantity of apples
update_quantity(inventory,"Apple",30)
print('Increasing quantity of Apples:',inventory)

#finding the total quantity of products in the inventory
total_inventory_items = total_inventory_quantity(inventory)
print('Total quantity of products: ',total_inventory_items)
# -

#clearing the inventory
inventory.clear()
print(inventory)


