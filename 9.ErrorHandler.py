# Demonstrate of Error Handling
# Like other programming language, in Python we can use Try and Except instead of Try and Catch
text = input("Enter Anything\n")
try:
    number = int(text)
    print(number)
# Except catch all the errors
except:
    print("Error Occurred")  
 
# Every try we can have multiple except    
x = 20
y = 10
try:
    print(x)
    print(y / 1)
    # When we want raise our own errors
    # in JS we used throw, in python we use raise
    if not type(x) is str:
        raise TypeError("Only String allowed.")
# Name error is a type of error which raised when we access undefined variable
except Exception as error:
    print(f"Custom Error: {error}")
except NameError:
    print("Error occurred because something is not defined.")
except ZeroDivisionError:
    print("denominator can not be zero.")
else:
    print("No Errors.")
finally:
    # Finally block will execute irrespective of error raised or not
    print("Finally block Executed.") 