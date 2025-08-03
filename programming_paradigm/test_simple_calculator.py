import unittest

from simple_calculator import SimpleCalculator

class TestAdd(unittest.TestCase):
    
    def test_addition(self):
       self.cal = SimpleCalculator()
       self.assertEqual(self.cal.add(7,8), 15)
       self.assertEqual(self.cal.add(7,-8), -1)

    def test_subtraction(self):
        self.cal = SimpleCalculator()
        self.assertEqual(self.cal.subtract(-9,20),-29)

    def test_multiplication(self):
        self.cal = SimpleCalculator() 
        self.assertEqual(self.cal.multiply(9,9), 81)

    def test_division(self):
       self.cal = SimpleCalculator()
       with self.assertRaises(ZeroDivisionError):
           self.cal.divide(2,0)
       

if __name__=="__main__":
    unittest.main()
