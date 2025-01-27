# below are built in methods [ which are installed along with python] 
import  math

#alias module
import random as rdm
# Custom module 
import myModule

print(int(math.sqrt(16)))
print(math.pi)
print(math.radians(60))
print(math.degrees(math.pi))

# accessing alias module
print(rdm.choice("1234"))

# Custom module method
print(myModule.addNumber(3,4))

# Optional Parameter execution
print(myModule.optionParams())
# Here we can't change the 2nd parameter value alone
# we need to pass the arguments in their respective order
print(myModule.optionParams("Welcome"," Python learning"))


# to know what are all methods available for particular module
# we can use dir method / other approach is with help of .operator
for item in dir(rdm):
    print(item)
    
# To print module name we can use __name__
print(myModule.__name__)
