import unittest

from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
       self.assertEqual(self.calc.add(7,8), 15)
       self.assertEqual(self.calc.add(7,-8), -1)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(-9,20),-29)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(9,9), 81)

    def test_division(self):
       self.assertEqual(self.calc.divide(9, 3), 3)
       with self.assertRaises(ZeroDivisionError):
           self.calc.divide(2,0)
       

if __name__=="__main__":
    unittest.main()
