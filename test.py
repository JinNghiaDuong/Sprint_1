import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        calc.add(2)
        self.assertEqual(calc.memory, 2)
        
    def test_subtract(self):
        calc = Calculator()
        calc.subtract(2)
        self.assertEqual(calc.memory, -2)
        
    def test_multiply(self):
        calc = Calculator()
        calc.multiply(2)
        self.assertEqual(calc.memory, 0)
        
    def test_divide(self):
        calc = Calculator()
        calc.divide(2)
        self.assertEqual(calc.memory, 0)
        with self.assertRaises(ValueError):
            calc.divide(0)
        
    def test_root(self):
        calc = Calculator()
        calc.root(2)
        self.assertEqual(calc.memory, 0)
        
    def test_reset(self):
        calc = Calculator()
        calc.add(2)
        calc.reset()
        self.assertEqual(calc.memory, 0)


if __name__ == '__main__':
    unittest.main()