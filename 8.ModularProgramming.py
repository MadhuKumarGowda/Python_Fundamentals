# below are built in methods [ which are installed along with python] 
import  math

# Custom module 
import myModule

print(int(math.sqrt(16)))
print(math.pi)
print(math.radians(60))
print(math.degrees(math.pi))

# Custom module method
print(myModule.addNumber(3,4))

# Optional Parameter execution
print(myModule.optionParams())
# Here we can't change the 2nd parameter value alone
# we need to pass the arguments in their respective order
print(myModule.optionParams("Welcome"," Python learning"))
