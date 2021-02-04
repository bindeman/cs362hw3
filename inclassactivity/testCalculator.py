#Phillip Bindeman
# CS 362 In Class Activity
# Calculator App
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def testAddition(self):
        self.assertEqual(calculator.add(0, 0), 0)
        self.assertEqual(calculator.add(1, 1), 2)
        self.assertEqual(calculator.add(-1, 2), 1)
        self.assertEqual(calculator.add(5.5, 6.7), 12.2)
        
    def testSubtraction(self):
        self.assertEqual(calculator.subtract(2.3, 0.3), 2.0)
        self.assertEqual(calculator.subtract(8, 3), 5)
        self.assertEqual(calculator.subtract(9, 2), 7)
        self.assertEqual(calculator.subtract(11.5, 1.5), 10.0)
        
    def testMultiplication(self):
        self.assertEqual(calculator.multiply(4, 4), 16)
        self.assertEqual(calculator.multiply(3, 2), 6)
        self.assertEqual(calculator.multiply(5.5, 5.3), 29.15)
        self.assertEqual(calculator.multiply(451, 732), 330132)
        
    def testDivide(self):
        self.assertEqual(calculator.divide(123, 0), "undefined")
        self.assertEqual(calculator.divide(14, 7), 2)
        self.assertEqual(calculator.divide(5, 2), 2.5)
        self.assertEqual(calculator.divide(180.5, 2), 90.25)

if __name__ == '__main__':
unittest.main(verbosity=2)
