# List and Tuples demonstration
# List is a collection of same/ different datatypes
fruits = ["Apple", "Banana", "Grapes"] # List with same data types
collections = [1, "Hello", "car", 0.5] # List with different data types

# Accessing collection
print(fruits[2])
print(collections[0]) 

# Add new items to list
fruits.append("Kiwi") # New item will append to end of the list
print(fruits)

# Modify the existing list item
fruits[1] = "BlueBerry" # Replace the item of index 1 of Fruit list
print(fruits)

#Tuples

position = (1,2)
color = (255,255,255)

print(type(color))

# Iteration to access the list
# There are 2 ways to accessing list, 1. Iterate by index and 2. iterate by item
# Below is example for iterate by item: this is not recommended as its slower than iterating by items
for index in range(0,len(fruits)):
    print(fruits[index])
    
# Below is example for iterate by item
for fruit in fruits:
    print(fruit)
    
    
users = ["Madhu","Gowda","KS"]
data = ["Madhu", 38]

print("Madhu" in users)
print(users[-1])
print(users.index("KS"))

print(users[0:2]) # it return the items which are present at 0 till next 2
print(users[0:]) # if we leave empty after : then it reads all the items of list

print(len(users)) # Return length of the list
users.append('Maddy') # Add new item to the list
print(users)

# Note: below list item should have [] else below item will save into list as individual char
users += ['Yukthishree'] # we can new list to the existing list
print(users)

# Another way to add list to existing list is by extend method
users.extend(['Abhi','Chotu'])
print(users)

# Insert method will allow us to insert an item into specific position
users.insert(0,'Raghav')
print(users)

# below approach will allow us to insert list items into from position 2
# if we mention start and end position same then items will be added
users[2:2] = ['Rock',"John"]
print(users)

# if start and end positions are different then new items will be replaced
# below range act as slice
users[1:3] = ['Pinky','Raamu']
print(users)

users.remove('KS')
print(users)

# if we want to remove last item from the list
print(users.pop()) # it returns the last item
print(users)

# if we want to delete at specific position 
del users[3]
print(users)

# we can use del to empty complete list
# del data # this approach will delete the data list from memory, not abel to access data list anymore
print(data)
data.clear() # this method will empty the list, able to access the list
print(data)

# Sort method
users[1:2] = ["madhu","mala"]
# Sort method will sort Uppercase first then sort the lower cases
users.sort() # modify the current list
print(users)

# if we want to sort irrespective of upper or lower case then we can use below approach
users.sort(key=str.lower)
print(users)

numList = [45,32,12,11,7,23]
numList.reverse() # The reverse method will flip the given list
print(numList)

numList.sort(reverse=True) # get the descending order sort
print(numList)
numList.sort(reverse=False) # get the ascending order list
print(numList)

# Above all sort methods will overwrite the current list and returns the new list
# There are ways to retain the original list using
# Global sort approach
newNumList = [22,77,54,12,1,9,45]
print("descending".title(),sorted(newNumList, reverse=True)) # Global sort with descending order 
print("ascending".title(),sorted(newNumList, reverse=False)) # Global sort with ascending order 
print(newNumList)

# There are multiple ways to copy the list
numListCopy_1 = newNumList.copy()
numListCopy_2 = list(newNumList)
numListCopy_3 = newNumList[:]

print(numListCopy_1)
print(numListCopy_2)
print(numListCopy_3)
print("----")
print(newNumList)

# Constructor method to create a list

myList = list([1,"Madhu","Kumar"])
print(myList)


#Tuples
# Tuples are same as list except that we can't change the item in it and order of the item in it.add()
# We can only modify by cloning to new list and modify the list by using append / insert / del

myTuple = tuple((1,"madhu", True))
newTuple = (2, "Kumar",False,38,'USA')

print(myTuple)
print(newTuple)

newTupleList = list(myTuple)
newTupleList.append('Maddy')
modifiedTuple = tuple(newTupleList)
print(modifiedTuple)

# we can de-structure the tuple 

(one,two,*remaining) = newTuple
print(one)
print(two)
print(remaining)

# the * symbol will de-structure the remaining together which are not considered by other index
# The *one will have first 3 values as we de-structure last 2 items
(*one,two,remaining) = newTuple
print(one)
print(two)
print(remaining)

# we can easily find how many occurrence in the give tuple

numberTuple = (2,3,4,5,3,3,7,8,9,3,3,3,)
print(numberTuple.count(3))
