#Phillip Bindeman
# CS 362 Homework III
# Run python file and you will be prompted to enter a number, enter a number and receive result;
#In your terminal enter 'python phillip_bindeman_hw1.py to run the file. Must be in the same directory




def isLeapYear():
  n = input("Enter a year to find out if its a leap year: ")
  
  n = int(n)
  
  if (n % 4 == 0 and (n % 100 != 0 or (n % 100 == 0 and n % 400 == 0))):
    return "It's a leap year!"
  else:
    return "It's not a leap year!"

print(isLeapYear())
