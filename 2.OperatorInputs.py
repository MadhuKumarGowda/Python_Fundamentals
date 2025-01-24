# Python operators and inputs

name= "Python"
print(name)

print('Hello, What is your name?')
# input() is to read the input from customer 
name = input()
print("your name is", name)

# Below are the basic Operators of python
# + addition
# - Subtraction
# / Divide
# * Multiplication

num1 = 45
num2 = 55
print("sum" , num1 + num2)
print("sub" , num1 - num2)
print("div" , num1 / num2)
print("mul" , num1 * num2)

# few more operators
# ** exponent 
# // integer division, return only inter and not reminder
# % return reminder
print(3**3) # output is 3 * 3 * 3
print (75 // 10 )
print(75%10)

print("Enter a number ?")
number = input();
print("Enter another number ?")
anothernumber = input()

# below method help to find what type of data is
print("anothernumber is a ", type(anothernumber))

# Note: all the input will be string ata type by default
# we need to convert before perform any mathematical operation
SUM = (int(number) + int(anothernumber))
print("Sum is", SUM)



