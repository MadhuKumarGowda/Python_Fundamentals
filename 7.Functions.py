# Demonstrate about Function and its syntax
# Functions are reusable block 

def sum(x,y):    
    return x+y

def printString(string):
    print(string)

print(sum(10,5))
printString("Hello Python")

# Function to read Text file

f = open('File.txt', 'r') # name of the file , mode of action r: Read w: Write
fileContent = f.readlines()

print(fileContent) # This will display file content with \n

newContent = []
for data in fileContent:
    if data[-1] == '\n':
        newContent.append(data[:-1]) # method to remove \n at the end
    else:
        newContent.append(data)
    
print(newContent) 

# Another simple way to remove space from word
newList = []
for line in fileContent:
    newList.append(line.strip())

print(newList)

# Function to Write into file

# Below code is clear the existing content of file, then write the new content
f = open('file.txt', 'w')
f.write('Now the file has one more line!\n')
f.write('learning write into file')
f.close() # this is mandatory to close when we open file for write

nf = open('file.txt', 'r')
newContent = nf.readline()
writeList = []

for line in newContent:
    writeList.append(line.strip())

print(writeList)

# find() and count() methods implementation

string = "hello from python"
print(string.find("h")) # return the index of given char else return -1

print(string.count('o')) # return the count of occurrence of given char or return 0

def hello():
    print("This message form python hello")

hello()

def sum(num1,num2):
    if(type(num1) is not int or type(num2) is not int):
        return
    else:
        print("sum function:" , num1 + num2)
        return num1+num2

total = sum("6",3) # function return None which is special type in python 
print(total)

# we can set default values for parameters 
# it will avoid exception
# if we fail to pass the argument with functions, then it consider 0 0 as default for both
def sumNumbers(num1=0,num2=0):
    if(type(num1) is not int or type(num2) is not int):
        return
    else:
        print("sum function:" , num1 + num2)
        return num1+num2

totalNumber = sumNumbers(3)
print(totalNumber)


# When we dont know about how many parameters are being passed to function
# then we can use *args / * with whatever text
# * return arguments as tuples
def multipleArguments(*args):
    print(len(args))
    print(type(args))

multipleArguments("madhu", 38, "KS", True)

# When we dont know about how many parameters are being passed to function
# But arguments are names arguments
# then we can use *kwargs [key word arguments] / * with whatever text
# ** return as dictionary 
def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_named_items(first="madhu", last="kumar", Surname="Gowda")


