# Python Dictionaries
# Dictionaries in python are used to store the value in key pair values 
# There are multiple ways to define / declare dictionaries
band = {
    "vocals":"plant",
    "guitar": "Page"
}
# Construction method
band1 = dict(vocals="Plant", guitar="Page");
print(band)
print(band1)
print(type(band))
print(len(band1))

# Access dictionaries items
print(band["vocals"])
print(band.get("guitar"))

# Access all the keys of dictionaries
print(band.keys())

# Access all the values of dictionaries
print(band.values())

# Access key value pair as tuple
print(band.items())

# Verify a key exists
print("guitar" in band)
print("keyboard" in band)

# Change values

# Insert / Update the existing values
band["vocals"] = "Coverdale"
# We can add new key value pair / modify the existing one
band.update({"bass": "JPJ"})
print(band)

# Remove an item from Dictionaries
print(band.pop("bass")) # should mention the key name 
print(band)

band["drums"] ="Bonham"
print(band)

print(band.popitem()) # it remove last item of dictionary, this will return item in tuple
print(band)

# Delete and Clear a dictionaries 
band["drums"] = "Bonham"
print("B4 Del",band)
del band["drums"]
print(band)

band1.clear()
print(band1)

del band1 # this will delete the complete dictionary

# Copy dictionary

# this will not create a copy, this will create a reference
# Any changes in band or band1 changes will be reflecting in both band and band1
# band1 = band 
# print("Bad copy")

# print(band1)
# print(band)

# band1["drums"] ="maddy"
# print("A4 adding new item to other dict",band)

# Better way to copy dict 
band2 = band.copy()
band2["drums"] = "ks"
print("new band2", band2)
print("copied band", band)

# Copy the dict using dict construction function
band3 = dict(band)
band3["keyboard"]="QWERTY"
print("new band2", band3)
print("copied band", band)

# Nested Dictionaries

member1 = {
    "name": "Plant",
    "instrument" : "vocals"
}
member2 = {
    "name": "Page",
    "instrument" : "Guitar"
}

nestedBand = {
    "member1": member1,
    "member2": member2
}

print("Nested Band", nestedBand)
print("Access nested band item", nestedBand["member1"]["name"])