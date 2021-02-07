#Phillip Bindeman

import unittest
import hw4

class TestCalculator(unittest.TestCase):
    def testCubing(self):
        self.assertEqual(hw3.cube(2), 8)
        self.assertEqual(hw3.cube(-7), 147)
        self.assertEqual(hw3.cube(123.4), 1879080.904)


        
    def testFindingAvgOfList(self):
        self.assertEqual(hw3.fullname("Phil", "Bindeman"), "Phillip Bindeman")
        self.assertEqual(hw3.fullname("Hi ", "There"), "Hi  There")
        self.assertEqual(hw3.fullname(123, 332), "123 332")

        
    def testFullname(self):
        self.assertEqual(hw3.findAvgOfList([2, 3, 1, 5, 1]), 2.4)
        self.assertEqual(hw3.findAvgOfList([2.4, 3.1, 5.123, 9.12, 4512.12]), 906.3726)
        self.assertEqual(hw3.findAvgOfList([2]), 2)
        self.assertEqual(hw3.findAvgOfList(["7", "2", 2]), "Uncaught Exception")


if __name__ == '__main__':
unittest.main(verbosity=2)
