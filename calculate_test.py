from calculate import add, subtract, multiply, divide, exponent, floorDivision
import unittest

class CalculateTest(unittest.TestCase): 
    def test_add(self):
        a = 1
        b = 2
        c = a + b
        self.assertEqual(add(), c)
        print('TEST CASE ADDITION OK')

            
     
    def test_subtract(self):
        a = 1
        b = 2
        c = a - b
        self.assertEqual(subtract(), c)
        print('TEST CASE SUBTRACTION OK')
            
    
    def test_multiply(self):
        a = 1
        b = 2
        c = a * b
        self.assertEqual(multiply(), c)
        print('TEST CASE MULTIPLICATION OK')


    def test_divide(self):
        a = 1
        b = 2
        if a == 0 or b == 0:
            raise ZeroDivisionError("You cannot divide by zero")
        else:
            c = a / b
        self.assertEqual(divide(), c)
        print('TEST CASE DIVISION OK')


    def test_exponent(self):
        a = 1
        b = 2
        c = a ** b
        self.assertEqual(exponent(), c)
        print('TEST CASE EXPONENT OK')


    def test_floorDivision(self):
        a = 1
        b = 2
        if a == 0 or b == 0:
            raise ZeroDivisionError("You cannot divide by zero")
        else:
            c = a // b
        self.assertEqual(floorDivision(), c)
        print('TEST CASE FLOOR DIVISION OK')
    
if __name__ == '__main__':
    unittest.main()