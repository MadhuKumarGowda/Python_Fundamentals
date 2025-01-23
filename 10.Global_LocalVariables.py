# Global vs Local Variables

age = 18 # Global Variable and able to access across the this file
loop = True
newAge = 30

def func(x):
    newAge = 21 # local variable to the func
    if x == 5:
        return x
    else:
        return newAge


def otherfunc(x):
    newAge = 25 # local variable to the otherfunc
    if x == 5:
        return x
    else:
        return newAge

print(func(10))
print(otherfunc(25))
print("GV", newAge)