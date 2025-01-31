import os
# r = Read
# a = Append
# w = Write 
# x = Create

# Read - Error if file does not exist

# we can mention rt to read and text file or rb to read binary file
f = open("names.txt", "r") 
# 
#print(f.read())
# to read first 4 characters of the file
# print(f.read(4))

# to read line by line manually
#print(f.readline())
#print(f.readline())

# read file line by line with loop
for line in f:
    print(line)

# we should close this file
f.close()

# Read operation with try and except block
try:
    f = open("names_list.txt", "r")
    print(f.read())
   
except FileNotFoundError:
    print("File not found")
finally:
     f.close()
    
# Approach 1 Write - Write into file if exist else throw an error [ overwrite existing file ]
f = open("context.txt","w")
print("I deleted all the content of the file")
f.write("Hello from python")
f.close()

f = open("context.txt", "r")
print(f.read())
f.close()

# Approach 2 Write - Create file if not exist [ overwrite existing file ]
# Opens a file for writing, creates the file if it does not exist
f = open("name_list.txt", "w")
f.close()


    
# Avoid an error if it doesn't exist
if os.path.exists("newFile.txt"):
    os.remove("newFile.txt")
else:
    print("The file does not exist")

# Append - Update file if not exist
f = open("names.txt", "a")
f.write("\nAbhi")
f.close()

f = open("names.txt", "r")
print(f.read())
f.close()

# Create - Error if file exist
# Create the specified file, but returns an error if the file exists
# if not os.path.exists("newFile.txt"):
#     f = open("newFile.txt", "x")
#     f.close()

with open("morename.txt") as f:
    content = f.read()

with open("names.txt", "w")as f:
    f.write(content)