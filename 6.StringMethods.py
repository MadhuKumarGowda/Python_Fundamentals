# Followings are the string methods 
# .strip() .len()  .lower() .upper()  .spilt()

# strip() : removing all leading and trailing white space from string
text = input("Input something")
print("Without strip",text)  # without strip method          
print("with strip",text.strip())  # with strip method    

# len() : Find the length of the string, this is not a method, but its a function
print("Length of the text without strip", len(text))     
print("Length of the text with strip",len(text.strip()))  

# Lower() : Use to convert to lower case of the string  
print("Lower case with strip",text.lower().strip())   
   
# Upper() : Use to convert to Upper case of the string     
print("Upper case with strip",text.upper())   

# Spilt() : Create a list of given string by delimiter
# by default it delimit by space if we not provide
print("Delimit the string using spilt",text.strip().split('-'))

# there are other string methods available in python
# please refer below link to know about them
# https://www.tutorialspoint.com/python/python_strings.htm

# Slice : We can use this for list and string
# [start:stop:step]
print("Slice the string",text[0:len(text)-3])
print("slice with single parameter", text[0:])
print("Slice with step parameter", text[::2])

fruits = ["Apple", "Banana", "Grapes", "Orange", "Pear"]
print("slice for list", fruits[1::2])

# if we want to add item to specific position of the list, we can use slice
fruits[1:1] = ["BlueBerry"]
print(fruits)