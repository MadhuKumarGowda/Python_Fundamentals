# Python sets

# Mutability:
# Tuples: Immutable, meaning you cannot modify their elements once created.
# Sets: Mutable, meaning you can add or remove elements.

# Order:
# Tuples: Ordered, meaning the elements maintain their original insertion order.
# Sets: Unordered, meaning the elements do not have a specific order.

# Duplicates:
# Tuples: Allow duplicate elements.
# Sets: Do not allow duplicate elements.

# Use Cases:
# Tuples:
# Useful when you need a fixed collection of items that shouldn't be modified, such as coordinates or database records.
# Sets:
# Useful when you need a collection of unique items, such as a list of distinct words in a document or a set of user IDs.

# There are multiple ways to Defining set

nums = {1,2,3,4,5,6}
nums1 = set((1,2,3,4,5,6,7))

print(nums)
print(nums1)
print(type(nums1))
print(len(nums1))

# No duplicates allowed
# if we add duplicates to set, set will always return unique values
uniqueNums = {1,2,3,4,4,5,6,6,6,7,7,7,7,8} 
print(len(uniqueNums))
print("Unique Sets:",uniqueNums)

# True is a dupe of 1, False is dupe of 0
numsSet = {1,True,2,False,3,4,0}
print(numsSet)

# Check if a value is in a set
print(2 in numsSet)

# But you can not refer to an element in the set with an index position or key as we 
# did for list or dictionaries

# add new element to set
numsSet.add(8)
print(numsSet)

# Add elements form another set
# We can update the set by adding new list, tuple and dictionaries as well 
moreNums = {8,9,10}
numsSet.update(moreNums)
print(numsSet)

# Merge 2 sets to create new set

set1 = {1,2,3,4,6,7}
set2 = {4,5,6,7,3,2}
unionSet = set1.union(set2)
print("Union set :", unionSet)

# Keep only the duplicates / common values

setX = {1,2,3,4,6}
setY = {4,5,6,7,3,2}
# Below method will not create new set, it modify the setX set
setX.intersection_update(setY)
print("Common sets:", setX )

# Keep everything except the duplicates

set11 = {1,2,3,4}
set22 = {4,3,2,5}

set11.symmetric_difference_update(set22)
print("Keep Everything except duplicates",set11)
