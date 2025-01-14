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
