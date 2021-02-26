import unittest
import math
import fibonacci
import fact
import pytest

class FibinacciTest(unittest.TestCase):

    def testFib(self):
        self.assertEqual(fibonacci(1), 1);

    def testFib(self):
        self.assertEqual(fibonacci(7), 8);

    def testFib(self):
        self.assertEqual(fibonacci(31), 1346269);


class TestFact(unittest.TestCase):

    def testFact(self):
        self.assertEqual(factorial(5), 120);

    def testFact(self):
        self.assertEqual(factorial(7), 5040);

    def testFact(self):
        self.assertEqual(factorial(0), 1);

    def testFact(self):
        self.assertEqual(factorial(10), 3,628,800);
        
    def testFact(self):
        self.assertEqual(factorial(2), 2);









if __name__ == '__main__':
    unittest.main()
