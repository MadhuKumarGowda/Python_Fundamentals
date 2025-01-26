# name is global scope variable & can be accessed across the program
name = "madhu"

# firstName is local variable as its defined with in greeting function
# it can be accessed with in greeting function scope 
def greeting(firstName):
    print("Global Variable:", name)
    print("Local Variable:", firstName)
    color = "red"
    print("Locally defined variable:", color)
    
greeting("Kumar")

def newFunction():
    greeting("gowda")

newFunction()

# define global variable
count = 1
def another():
    color = "orange"
    
    # accessing global variable within the function, then we need to declare global keyword
    global count
    count += 1
    print("Global count value :",count)    
    
    # nested function is limited to another functions scope and 
    # can not be accessed from outside of the another function
    def nestedFun(name):
        # to access variable fo parent scope, we can use nonlocal keyword
        nonlocal color 
        color = "red"
        print("Closure variable color", color)
        print("nested fun variable", name)
    
    nestedFun("KumarKS")

another()