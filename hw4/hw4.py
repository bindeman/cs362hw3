#Phillip Bindeman
# CS 362 In Class Activity
# Homework 3


def cube(a):
    if(type(a) is not (int or float)) return "Invalid input"
    #make the first value an absolute value to ensure it is positive
    return abs(a)*a*a
    
def fullname(first, last):
    return first, " ", last
    
def findAvgOfList(a):
if(len(a) == 0) return "Cannot find avg of empty list"
return sum(a) / len(a)
