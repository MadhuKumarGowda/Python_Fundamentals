# lambda function is a single expression the returns a value
sqr = lambda num : num * num

#above lambda code is equal to
# def sqr(num): return num * num 

print(sqr(3))

addTwo =  lambda num1,num2: num1 + num2

print(addTwo(5,8))

print(" Lambda with closure ".center(50,"#"))

def funBuilder(x):
    return lambda num: num + x

addTen = funBuilder(10) # this will return lambda function as return
addTwenty = funBuilder(20) # this will return lambda function as return

print(addTen(5))  # This actually execute the lambda with parameter
print(addTwenty(15))

print(" High order functions ".center(50,"#"))
# High order function is nothing but a function which accept one/more functions as arguments
# or function which return a function as a result

print(" Map method ".center(50,"#"))
numbers = [3,2,5,6,8,12,15]

sqr_nums = map(lambda num: num*num, numbers)
print(list(sqr_nums))

print(" Filter method ".center(50,"#"))

odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))

print(" Reduce method ".center(50,"#"))
from functools import reduce

numbers_list = [1,2,3,4,5,6,7,8,9]

total = reduce(lambda acc,curr: acc + curr, numbers_list,0)
print(total)
# there is built in method to sum of all numbers
print(sum(numbers_list,0))

# Sum built in method is far better than reduce in above use case

namesList = ["Madhu Kumar", "Mala", "Abhi", "Yukthishree"]

char_count = reduce(lambda acc, curr: acc + len(curr), namesList, 0)
print(char_count)


