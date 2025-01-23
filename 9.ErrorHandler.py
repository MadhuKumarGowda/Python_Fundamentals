# Demonstrate of Error Handling
# Like other programming language, in Python we can use Try and Except instead of Try and Catch
text = input("Enter Anything")
try:
    number = int(text)
    print(number)
except:
    print("Error Occurred")  