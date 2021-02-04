#Phillip Bindeman
# CS 362 In Class Activity
# Calculator App


def add(a, b):
    return a+b
    
def subtract(a, b):
    return a-b
    
def multiply(a, b):
    return a*b
    
def divide(a, b):
    if(b == 0):
        return "undefined"
    else:
        return a/float(b)
