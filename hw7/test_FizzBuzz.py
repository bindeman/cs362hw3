#Phillip Bindeman
# CS 362, Winter 2021
# Problem 1, Homework 7

import unittest
import fizzBuzz

class HW7TestCases(unittest.TestCase):
    def testFizzBuzz(self):
        self.assertEqual(fizzBuzz.fizzBuzz(3), "Fizz")
        self.assertEqual(fizzBuzz.fizzBuzz(15), "FizzBuzz")






#if __name__ == '__main__':
#unittest.main(verbosity=2)

