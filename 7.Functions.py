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

