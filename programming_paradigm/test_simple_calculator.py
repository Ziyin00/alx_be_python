"""
Unit tests for SimpleCalculator class.
"""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Basic addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

        # Negative numbers
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 15), 5)

        # Large numbers
        self.assertEqual(self.calc.add(1000, 2000), 3000)

        # Decimal numbers
        self.assertEqual(self.calc.add(3.5, 2.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=15)  # Float precision

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Basic subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 0), 0)

        # Negative results
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 5), -5)

        # Negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, -15), 5)

        # Large numbers
        self.assertEqual(self.calc.subtract(2000, 1000), 1000)

        # Decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertEqual(self.calc.subtract(0.3, 0.1), 0.2)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Basic multiplication
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(1, 1), 1)

        # Negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(2, -3), -6)

        # Large numbers
        self.assertEqual(self.calc.multiply(100, 50), 5000)

        # Decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 3), 7.5)
        self.assertEqual(self.calc.multiply(0.5, 0.5), 0.25)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Basic division
        self.assertEqual(self.calc.divide(6, 2), 3.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0.0)

        # Division by zero (edge case)
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

        # Negative numbers
        self.assertEqual(self.calc.divide(-6, 2), -3.0)
        self.assertEqual(self.calc.divide(6, -2), -3.0)
        self.assertEqual(self.calc.divide(-6, -2), 3.0)

        # Large numbers
        self.assertEqual(self.calc.divide(1000, 100), 10.0)

        # Decimal numbers
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(1, 3), 1/3, places=15)  # Float precision

    def test_edge_cases(self):
        """Test edge cases for all operations."""
        # Zero operations
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertIsNone(self.calc.divide(0, 0))

        # One operations
        self.assertEqual(self.calc.add(5, 1), 6)
        self.assertEqual(self.calc.subtract(5, 1), 4)
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.divide(5, 1), 5.0)

        # Very large numbers
        large_num = 999999999
        self.assertEqual(self.calc.add(large_num, 1), large_num + 1)
        self.assertEqual(self.calc.multiply(large_num, 2), large_num * 2)


if __name__ == "__main__":
    unittest.main()
