#Phillip Bindeman
# CS 362, Winter 2021
# Problem 1, Homework 7

def fizzBuzz(n):
    if(n%3 == 0 and n%5 == 0):
        return "FizzBuzz"
    elif (n%3 == 0):
        return "Fizz"
    elif (n%5 == 0):
        return "Buzz"
    else:
        return "todo"
