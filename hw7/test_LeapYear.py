#Phillip Bindeman
# CS 362, Winter 2021
# Problem 2, Homework 7

import unittest
import leapYear

class HW7TestCases(unittest.TestCase):
    def testleapYear(self):
        self.assertEqual(leapYear.leapYear(8), True)
        self.assertEqual(leapYear.leapYear(600), False)
        self.assertEqual(leapYear.leapYear(400), True)

        




