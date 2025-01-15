# Demonstrate about Function and its syntax

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
