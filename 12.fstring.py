person = "madhu"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

# implementing of S string : its represent by %
s_message = "\n%s has %s coins left.\n" %(person,coins)
print("S method",s_message)

# implementing of Format string with {} : its represent by {} with format method
format_message = "\n{} has {} coins left.\n".format(person,coins)
print("{} method",format_message)

# implementing of Format string with index : its represent by {} with index
index_message = "\n{1} has {0} coins left.\n".format(coins,person)
print("index method",index_message)

# implementing of Format string with assigning : its represent by {} with index
assigning_message = "\n{p} has {c} coins left.\n".format(c=coins,p=person)
print("Assigning method",assigning_message)

player = {"person": "maddy","coins":3}
# implementing of Format string with dictionary : its represent by ** with index
dictionary_message = "\n{person} has {coins} coins left.\n".format(**player)
print("Dictionary method",dictionary_message)

# above all format methods are ok to use when we small less number of arguments
# it become more complex when we want to display the more number of arguments
# to resolve all this complexity we can use f string approach

f_message = f"\n{person} has {coins} coins.\n"
print("f-Method", f_message)

# instead of defining pre-defined variable, we can display dynamic values as shown below
f_expression_message = f"\n{person.lower()} has {4 * 5} coins.\n"
print("f-expression Method", f_expression_message)

# we can use dictionary values with f message 
f_dictionary_message = f"\n{player['person']} has {player['coins']} coins.\n"
print("f-dictionary Method", f_dictionary_message)

# we can pass formatting options
num = 10
print(f"\n2.75 times of {num} is {2.75 * num:.2f}\n")

for num in range(1,11):
    print(f"2.75 times of {num} is {2.75 * num:.2f}")
print("\n")
    
for num in range(1,11):
    print(f"{num} divided by 4.68 is {num / 4.68:.2%}")
    
# Understand more about format method from internet
# format() method is older method
