import unittest

from simple_calculator import SimpleCalculator

class TestAdd(unittest.TestCase):
    def test_addition(self):
       calculator = SimpleCalculator()
       result = calculator.add(7,8)
       self.assertEqual(result, 15)

    def test_add_negative(self):
       self.cal = SimpleCalculator()
       result = self.cal.add(7,-8)
       self.assertEqual(result, -1)

    def test_subtraction(self):
        self.cal = SimpleCalculator()
        result = self.cal.subtract(-9,20)
        self.assertEqual(result,-29)

    def test_multiplication(self):
        self.cal = SimpleCalculator() 
        result = self.cal.multiply(9,9)
        self.assertEqual(result, 81)

    def test_division(self):
       self.cal = SimpleCalculator()
       with self.assertRaises(ZeroDivisionError):
           self.cal.divide(2,0)
       

if __name__=="__main__":
    unittest.main()
