# Demonstrate about loops and its syntax

# Below for loop will print the output from 0 to 9
# by default increment value is 1
print("--------------------")
for char in range(0,10):
    print(char)
print("--------------------")
    
# below is the example for for loop with one parameter
for char in range(5): # 5 is target number, it start from 0 and increase by 1
    print(char)
print("--------------------")

# If you want add increment operator by 2/3/4....
# Below loop will increase the number by 3 as i mentioned 3 as third parameter
for char in range(0,10,3): # 0 is the start, 10 is the target, and 3 is increment 
    print(char)
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
 
names = ['madhu','kumar','abhi','yukthi']
# for name in names:
#     print(name)
    
# for char in "madhukumarks":
#     print(char)

# for x in names:
#     if x == "kumar":
#         break
#     print(x)

for x in names:
    if x == "kumar":
        continue
    print(x)

for x in range(4):
    print(x)

print("-------Range between start and end---------")
for x in range(2,6):
    print(x)

print("-------Range between start and end with custom increment---------")
for x in range(0,50,5): # :: Start index 50: End Index and 5 is increment count
    print(x)
else:
    print("Loop is reached at its end")
 
 
    