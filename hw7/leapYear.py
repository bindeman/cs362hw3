#Phillip Bindeman
# CS 362, Winter 2021
# Problem 2, Homework 7

def leapYear(n):
    if(n % 4 == 0 and (n % 100 != 0 or n % 400 == 0)):
        return True
    else:
        return False
