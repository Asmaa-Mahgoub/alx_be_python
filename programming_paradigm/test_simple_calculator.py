import unittest

from simple_calculator import SimpleCalculator

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
       calculator = SimpleCalculator()
       result = calculator.add(7,8)
       self.assertEqual(result, 15)

    def test_add_negative(self):
       calculator = SimpleCalculator()
       result = calculator.add(7,-8)
       self.assertEqual(result, -1)

    def test_subtract(self):
        calculator = SimpleCalculator()
        result = calculator.subtract(-9,20)
        self.assertEqual(result,-29)

    def test_multiply(self):
        calculator = SimpleCalculator() 
        result = calculator.multiply(9,9)
        self.assertEqual(result, 81)

    def test_division(self):
       calculator = SimpleCalculator()
       with self.assertRaises(ZeroDivisionError):
           calculator.divide(2,0)
       

if __name__=="__main__":
    unittest.main()
