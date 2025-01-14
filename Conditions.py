# Below are logical operators use to make decision  

# < 
# >
# == Note : we must use == for equal comparision, we can't use = as its decalration operator
# !=

print (2 < 3)
print (2 > 3)
print("Python" == "Java")
print("Python" != "C#")
print("Python" == "PYTHON")

# IF-ELSE condition

if 2 > 3:
    print ("2 is greater")
else:
    print("3 is greater")
    
# IF-ELIF - ELSE condition
a= 2
b= 1
c = 0
if a > b:
    print(" a is bigger")
elif a < c:
    print("a is bigger")
else:
    print("a is lesser")
    
# Chained Conditions
x = 2
y = 3
z = 5

if x > y and x > z:
    print("X is Greater")
elif y > x and y > z:
    print("Y is greater")
else:
    print("Z is greater")


