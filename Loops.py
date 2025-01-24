# Demonstrate about loops and its syntax

# Below for loop will print the output from 0 to 9
# by default increment value is 1
print("--------------------")
for x in range(0,10):
    print(x)
print("--------------------")
    
# below is the example for for loop with one parameter
for x in range(5): # 5 is target number, it start from 0 and increase by 1
    print(x)
print("--------------------")

# If you want add increment operator by 2/3/4....
# Below loop will increase the number by 3 as i mentioned 3 as third parameter
for x in range(0,10,3): # 0 is the start, 10 is the target, and 3 is increment 
    print(x)
print("--------------------")


# While Loops
# loop = True

# while loop:
#     name = input("Enter something")
#     if name == "stop" or name == "Stop":
#         loop = False # or we can use break key word
# print("Program stopped")

# break with loop
value = 1
while value <= 10:
    print(value)
    if value ==5:
        break
    value += 1

print("---------------------------")
# continue with loop
value1 = 1
while value1 <= 10:    
    value1 += 1
    if value1 % 2 == 0:
        continue
    print(value1)
else:
    print(value1) 

# For Loops  
    