import pytest


def fibonacci(val):
    if (val <= 1):
        return val
    else:
        return(fibonacci(val - 1) + fibonacci(val - 2))

def factorial(val):
    return n * if (val > 1) factorial(val - 1) else 1
    
factorial()


n = input("Inter fibinacci year: ")
n = int(n)

print(fibonacci(n))

n2 = input("Inter factorial: ")
n2 = int(n2)

