#Phillip Bindeman
# CS 362, Winter 2021
# Problem 1, Homework 7

import unittest
import fizzBuzz

class HW7TestCases(unittest.TestCase):
    def testCubing(self):
        self.assertEqual(fizzBuzz.cube(3), "Fizz")
        self.assertEqual(fizzBuzz.cube(4), 4)
        self.assertEqual(fizzBuzz.cube(5), "Buzz")
        self.assertEqual(fizzBuzz.cube(15), "FizzBuzz")
        self.assertEqual(fizzBuzz.cube(17), 17)




if __name__ == '__main__':
unittest.main(verbosity=2)

