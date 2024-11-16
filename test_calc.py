import unittest
import unit_testing

class Testcalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(unit_testing.add(3, 8), 11)
        self.assertEqual(unit_testing.add(-1, 8), 7)
        self.assertEqual(unit_testing.add(-3, 1), -2)

    def test_subtract(self):
        self.assertEqual(unit_testing.subtract(-3, 8), -11)
        self.assertEqual(unit_testing.subtract(7, 1), 6)
        self.assertEqual(unit_testing.subtract(-3, 1), -4)

    def test_multiply(self):
        self.assertEqual(unit_testing.multiply(8, 1), 8)
        self.assertEqual(unit_testing.multiply(-1, 8), -8)
        self.assertEqual(unit_testing.multiply(-3, -1), 3)
         
    def test_divide(self):
        self.assertEqual(unit_testing.divide(8, 2), 4)
        self.assertEqual(unit_testing.divide(2, 2), 1)
        self.assertEqual(unit_testing.divide(-1, -1), 1)
        self.assertEqual(unit_testing.divide(5, 2), 2.5)

        #using the context manager to test exceptions
        with self.assertRaises(ValueError):
            unit_testing.divide(10, 0)


if __name__ == '__main__': 
    unittest.main()