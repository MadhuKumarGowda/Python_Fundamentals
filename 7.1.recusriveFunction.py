# Function is being called iteratively is called recursive function
def add_one(num):
    if(num >= 9):
        return num + 1
    
    total = num + 1
    print(total)
    
    return add_one(total)

newTotal = add_one(5)
print(newTotal)

# Factorial Numbers with loop
def factorialLoop(n):
    result = 1
    for x in range(1,n+1):
        result *= x
    return result
     
# Factorial Numbers with recursive method
print("Factorial".center(50,"*"))
def factorial(n):
    if n == 0:
        return 1
    else:        
        print(n)
        return n * factorial(n - 1)

number = 4
print(f"The factorial with Recursive of {number} is {factorial(number)}")
print(f"The factorial with loop of {number} is {factorialLoop(number)}")

# Fibonacci Method with Loop

def fibonacciLoop(n):
    a,b=0,1
    for i in range(n):
        a, b = b, a + b
    return a

for i in range(10):
    print(fibonacciLoop(i))
