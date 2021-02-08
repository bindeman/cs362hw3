#Phillip Bindeman

import unittest
import hw4

class TestCalculator(unittest.TestCase):
    def testCubing(self):
        self.assertEqual(hw4.cube(2), 8)
        self.assertEqual(hw4.cube(-7), 147)
        self.assertEqual(hw4.cube("3"), "Invalid input")
        self.assertEqual(hw4.cube(123.4), 1879080.904)
        self.assertEqual(hw4.cube(sqrt(2)), 1879080.904)


    def testFindingAvgOfList(self):
        self.assertEqual(hw4.findAvgOfList([2, 3, 1, 5, 1]), 2.4)
        self.assertEqual(hw4.findAvgOfList([2.4, 3.1, 5.123, 9.12, 4512.12]), 906.3726)
        self.assertEqual(hw4.findAvgOfList([2]), 2)
        self.assertEqual(hw4.findAvgOfList([]), "Cannot find avg of empty list")
        self.assertRaises(TypeError, cs362question2.findAvgOfList, ["7", "2", 2])
    
    
    def testFullname(self):
        self.assertEqual(hw4.fullname("Phil", "Bindeman"), "Phillip Bindeman")
        self.assertEqual(hw4.fullname("Hi ", "There"), "Hi  There")
        self.assertEqual(hw4.fullname("", 332), "332")
        self.assertEqual(hw4.fullname("Phil", 332), "Phil 332")


if __name__ == '__main__':
unittest.main(verbosity=2)
