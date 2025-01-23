# Author Madhu Kumar K S

# Below are basic data types
int # numbers examples 0 1 3 5 6
str # with in 'Python' / "Python"
bool # True / False
float # 0.12 1.23 3.455

# Declaring variables 
name = "Python"
newName = 'Python'

# access the above variables
print(name)
print(newName) 

name = "Welcome to Python"
print(name)

# Rules for variables
# Only contains _ , characters and numbers
# shouldn't start with number, but can be ended with numbers

NAME = "Hello"
name = "Python"

# Above 2 variables are different as Python is case sensitive 
age = 17

#Literal assignment
#Checking the data type instances

name="madhu"
initial ="KS"

#There are different ways to check the type 
print(type(name))
print(type(name) == str)
print(isinstance(name, str))

#Constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

#Concatenation

fullname = name + " " + initial
print(fullname)
fullname += " Welcome."

#Casting a number to a string

decade = str(1986)
print(type(decade))
print(decade) 


statement = "i like the music from " + decade + "s."

# Multiple lines
multiline = '''
Hey, How are you?        
i was just checking from python!
                                all good.

'''
print(multiline)

#Escaping special characters
# \ helps tp add special character, \t helps to add tab, \n add new line
sentence = 'I\'m a Senior Software Engineer\t with 12 Years of Experience\nWorking on Cloud, React, Node and Python.'
print(sentence)

# String Methods

print(name)
# The Upper and Lower methods will return new string and it doesn't modify the current string
print(name.lower())
print(name.upper())
print(name)

# Title method will capitalize the given string
# Title and replace methods will return new string and it doesn't modify the current string
print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

# Strip, len methods
# Below methods will return new string and it doesn't modify the current string
print(multiline.title())
print(len(multiline))
print(len(multiline.strip())) # Remove complete white space from left and right ended
print(len(multiline.lstrip())) # Only remove the left side of the string
print(len(multiline.rstrip())) # Only remove the right side of the string

#Build a menu
title = "menu".upper();
# Center method will place the menu center with * sides
print(title.center(20, "*"))
# Ljust and Rjust are the method to adjust the left and right position
print("Coffee".ljust(16, " ") + "$1".rjust(4))
print("Tea".ljust(16, " ") + "$1.5".rjust(4))
print("Cake".ljust(16, " ") + "$2".rjust(4))

# String Index Values
print(name[1])
print(name[-1]) # we can use -1 to access last char of the string when we dont know the actual length

#String methods return boolean values
print(name.startswith("m"))
print(name.endswith("U".lower()))

#Boolean datatypes

myValue = True
x = bool(False)
print(type(x))
print(myValue) 

#Numeric Datatypes

#Integer Types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 3.28
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in functions for numbers

print(abs(gpa))
print(round(gpa)) # Rounded to nearest integer
print(round(gpa,1)) # Rounded to nearest decimal value, 3.28 o/p will be 3.3

# Math module
import math

print(math.pi)
print(math.sqrt(64)) # Return float value
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number

zipcode = "10001"
zip_code = int(zipcode)
print(type(zip_code))

