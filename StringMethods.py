# Followings are the string methods 
# .strip() .len()  .lower() .upper()  .spilt()

# strip() : removing all leading and trailing white space from string
text = input("Input something")
print(text)  # without strip method          
print(text.strip())  # with strip method    

# len() : Find the length of the string, this is not a method, but its a function
print(len(text))     
print(len(text.strip()))  

# Lower() : Use to convert to lower case of the string  
print(text.lower().strip())   
   
# Upper() : Use to convert to Upper case of the string     
print(text.upper())   

# Spilt() : Create a list of given string by delimiter
# by default it delimit by space if we not provide
print(text.strip().split('-'))

# there are other string methods available in python
# please refer below link to know about them
# https://www.tutorialspoint.com/python/python_strings.htm