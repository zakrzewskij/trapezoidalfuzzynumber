"""
This test suite includes unit tests for the methods of the TrapezoidalFuzzyNumber class.
"""

import unittest

from fuzzy_numbers.trapezoidal_fuzzy_number import TrapezoidalFuzzyNumber


class TestTrapezoidalFuzzyNumber(unittest.TestCase):
    def test_trapezoidal_number(self):
        """
        Test the initialization of the TrapezoidalFuzzyNumber class.

        Checks that the TrapezoidalFuzzyNumber object is created with the correct attribute values.

        """
        tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        self.assertEqual(tn.lower_left_bound, 1)
        self.assertEqual(tn.upper_left_bound, 2)
        self.assertEqual(tn.upper_right_bound, 3)
        self.assertEqual(tn.lower_right_bound, 4)

    def test_sort(self):
        """
        Test the sort_trapezoidal_values method of the TrapezoidalFuzzyNumber class.

        Checks that the sort_trapezoidal_values method correctly sorts the trapezoidal values.

        """
        result = TrapezoidalFuzzyNumber.sort(3, 1, 4, 2)
        self.assertEqual(result, (1, 2, 3, 4))

    def test_core(self):
        """
        Test the core method of the TrapezoidalFuzzyNumber class.

        Checks that the core method returns the correct core values of the trapezoidal number.

        """
        tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        result = tn.core
        self.assertEqual(result, (2, 3))

    def test_support(self):
        """
        Test the support method of the TrapezoidalFuzzyNumber class.

        Checks that the support method returns the correct support values of the trapezoidal number.

        """
        tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        result = tn.support
        self.assertEqual(result, (1, 4))

    def test_alpha_interval(self):
        """
        Test the alpha_interval method of the TrapezoidalFuzzyNumber class.

        Checks that the alpha_interval method returns the correct alpha interval of the trapezoidal number.

        """
        tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        result = tn.alpha_interval
        self.assertIsInstance(result, tuple)
        self.assertAlmostEqual(result[0], 0.8333333, places=7)
        self.assertIsInstance(result[1], (float, int))
        self.assertAlmostEqual(result[1], 1.6666667, places=7)

    def test_ambiguity(self):
        """
        Test the ambiguity method of the TrapezoidalFuzzyNumber class.

        Checks that the ambiguity method returns the correct ambiguity of the trapezoidal number.

        """
        tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        result = tn.ambiguity
        self.assertAlmostEqual(result, 0.8333333, places=7)

    def test_expected_interval(self):
        """
        Test the expected_interval method of the TrapezoidalFuzzyNumber class.

        Checks that the expected_interval method returns the correct expected interval of the trapezoidal number.

        """
        tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        result = tn.expected_interval
        self.assertEqual(result, (1.5, 3.5))

    def test_value(self):
        """
        Test the value method of the TrapezoidalFuzzyNumber class.

        Checks that the value method returns the correct value of the trapezoidal number.

        """
        tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        result = tn.value
        self.assertEqual(result, 2.5)

    def test_expected_value(self):
        """
        Test the expected_value method of the TrapezoidalFuzzyNumber class.

        Checks that the expected_value method returns the correct expected value of the trapezoidal number.

        """
        tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        result = tn.expected_value
        self.assertEqual(result, 2.5)

    def test_width(self):
        """
        Test the width method of the TrapezoidalFuzzyNumber class.

        Checks that the width method returns the correct width of the trapezoidal number.

        """
        tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        result = tn.width
        self.assertEqual(result, 2.0)

    def test_add(self):
        """
        Test the add method of the TrapezoidalFuzzyNumber class.

        Checks that the add method correctly adds two trapezoidal numbers.

        """
        test_cases_add = [
            (
                TrapezoidalFuzzyNumber(1, 2, 3, 4),
                TrapezoidalFuzzyNumber(2, 3, 4, 5),
                TrapezoidalFuzzyNumber(3, 5, 7, 9),
                "Positive Numbers Case",
            ),
            (
                TrapezoidalFuzzyNumber(-3, -2, -1, 0),
                TrapezoidalFuzzyNumber(-1, 0, 1, 2),
                TrapezoidalFuzzyNumber(-4, -2, 0, 2),
                "Both Negative Numbers Case",
            ),
            (
                TrapezoidalFuzzyNumber(1, 2, 3, 4),
                TrapezoidalFuzzyNumber(-2, -1, 0, 1),
                TrapezoidalFuzzyNumber(-1, 1, 3, 5),
                "One Positive and One Negative Case",
            ),
            (
                TrapezoidalFuzzyNumber(-5, -3, -2, -1),
                TrapezoidalFuzzyNumber(2, 3, 4, 5),
                TrapezoidalFuzzyNumber(-3, 0, 2, 4),
                "One Negative and One Positive Case",
            ),
        ]

        for tn1, tn2, expected_result, description in test_cases_add:
            with self.subTest(description=description):
                result = tn1 + tn2

                # Check the boundaries
                self.assertLessEqual(result.lower_left_bound, result.upper_left_bound)
                self.assertLessEqual(result.upper_left_bound, result.upper_right_bound)
                self.assertLessEqual(result.upper_right_bound, result.lower_right_bound)

                # Check specific boundary values
                self.assertAlmostEqual(
                    result.lower_left_bound, expected_result.lower_left_bound
                )
                self.assertAlmostEqual(
                    result.upper_left_bound, expected_result.upper_left_bound
                )
                self.assertAlmostEqual(
                    result.upper_right_bound, expected_result.upper_right_bound
                )
                self.assertAlmostEqual(
                    result.lower_right_bound, expected_result.lower_right_bound
                )

    def test_sub(self):
        """
        Test the subtraction (__sub__) method of the TrapezoidalFuzzyNumber class.

        Checks that the subtraction method correctly subtracts two trapezoidal numbers.

        """
        test_cases_sub = [
            (
                TrapezoidalFuzzyNumber(1, 2, 3, 4),
                TrapezoidalFuzzyNumber(2, 3, 4, 5),
                TrapezoidalFuzzyNumber(-4, -2, 0, 2),
                "Positive Numbers Case",
            ),
            (
                TrapezoidalFuzzyNumber(-5, -3, -2, -1),
                TrapezoidalFuzzyNumber(-9, -7, -6, -5),
                TrapezoidalFuzzyNumber(0, 3, 5, 8),
                "Negative Numbers Case",
            ),
            (
                TrapezoidalFuzzyNumber(-2, -1, 0, 1),
                TrapezoidalFuzzyNumber(1, 2, 3, 4),
                TrapezoidalFuzzyNumber(-6, -4, -2, 0),
                "One Negative and One Positive Case",
            ),
            (
                TrapezoidalFuzzyNumber(-5, -3, -2, -1),
                TrapezoidalFuzzyNumber(2, 3, 4, 5),
                TrapezoidalFuzzyNumber(-10, -7, -5, -3),
                "One Negative and One Positive Case 2",
            ),
        ]

        for tn1, tn2, expected_result, description in test_cases_sub:
            with self.subTest(description=description):
                result = tn1 - tn2

                # Check the boundaries
                self.assertLessEqual(result.lower_left_bound, result.upper_left_bound)
                self.assertLessEqual(result.upper_left_bound, result.upper_right_bound)
                self.assertLessEqual(result.upper_right_bound, result.lower_right_bound)

                # Check specific boundary values
                self.assertAlmostEqual(
                    result.lower_left_bound, expected_result.lower_left_bound
                )
                self.assertAlmostEqual(
                    result.upper_left_bound, expected_result.upper_left_bound
                )
                self.assertAlmostEqual(
                    result.upper_right_bound, expected_result.upper_right_bound
                )
                self.assertAlmostEqual(
                    result.lower_right_bound, expected_result.lower_right_bound
                )

    def test_neg(self):
        """
        Test the negation (__neg__) method of the TrapezoidalFuzzyNumber class.

        Checks that the negation method correctly returns the symmetric image of a trapezoidal number.
        The symmetric image of a trapezoidal number is obtained by reflecting the trapezoid across the vertical axis
        passing through the centroid.

        Test cases include both positive and negative trapezoidal numbers.

        """
        # Test case with a positive trapezoidal number
        tn1 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        result1 = -tn1

        # Assert the properties of the resulting trapezoidal fuzzy number
        self.assertEqual(result1.lower_left_bound, -4)
        self.assertEqual(result1.upper_left_bound, -3)
        self.assertEqual(result1.upper_right_bound, -2)
        self.assertEqual(result1.lower_right_bound, -1)

        # Test case with a negative trapezoidal number
        tn2 = TrapezoidalFuzzyNumber(-4, -3, -2, -1)
        result2 = -tn2

        # Assert the properties of the resulting trapezoidal fuzzy number
        self.assertEqual(result2.lower_left_bound, 1)
        self.assertEqual(result2.upper_left_bound, 2)
        self.assertEqual(result2.upper_right_bound, 3)
        self.assertEqual(result2.lower_right_bound, 4)

    def test_mul(self):
        """
        Test the multiplication method of the TrapezoidalFuzzyNumber class.

        Checks that the multiplication method correctly handles both trapezoidal fuzzy numbers
        and floats as multipliers.

        Test cases include various combinations of positive values.
        """
        test_cases_mul = [
            (
                TrapezoidalFuzzyNumber(1, 2, 3, 4),
                TrapezoidalFuzzyNumber(2, 3, 4, 5),
                TrapezoidalFuzzyNumber(2, 6, 12, 20),
                "Multiplication with TrapezoidalFuzzyNumber: Case 1",
            ),
            (
                TrapezoidalFuzzyNumber(3, 4, 5, 6),
                TrapezoidalFuzzyNumber(1, 2, 3, 4),
                TrapezoidalFuzzyNumber(3, 8, 15, 24),
                "Multiplication with TrapezoidalFuzzyNumber: Case 2",
            ),
            (
                TrapezoidalFuzzyNumber(1, 2, 3, 4),
                2.0,
                TrapezoidalFuzzyNumber(2, 4, 6, 8),
                "Multiplication with float: Case 1",
            ),
        ]

        for operand1, operand2, expected_result, description in test_cases_mul:
            with self.subTest(description=description):
                result = operand1 * operand2

                # Check the boundaries
                self.assertLessEqual(result.lower_left_bound, result.upper_left_bound)
                self.assertLessEqual(result.upper_left_bound, result.upper_right_bound)
                self.assertLessEqual(result.upper_right_bound, result.lower_right_bound)

                # Check ambiguity and width
                self.assertAlmostEqual(result.ambiguity, expected_result.ambiguity)
                self.assertAlmostEqual(result.width, expected_result.width)

                # Check specific boundary values
                self.assertAlmostEqual(
                    result.lower_left_bound, expected_result.lower_left_bound
                )
                self.assertAlmostEqual(
                    result.upper_left_bound, expected_result.upper_left_bound
                )
                self.assertAlmostEqual(
                    result.upper_right_bound, expected_result.upper_right_bound
                )
                self.assertAlmostEqual(
                    result.lower_right_bound, expected_result.lower_right_bound
                )

    def test_rmul(self):
        """
        Test the multiplication method of the TrapezoidalFuzzyNumber class with valid trapezoidal numbers.

        Checks that the multiplication method correctly multiplies two valid trapezoidal numbers.

        Test cases include various combinations of positive and negative values.
        """
        test_cases_rmul = [
            (
                TrapezoidalFuzzyNumber(-5, -4, -3, -2),
                TrapezoidalFuzzyNumber(-2, -1, 0, 1),
                TrapezoidalFuzzyNumber(-5, 0, 4, 10),
                "Case 1",
            ),
            (
                TrapezoidalFuzzyNumber(-2, -1, 0, 1),
                TrapezoidalFuzzyNumber(1, 2, 3, 4),
                TrapezoidalFuzzyNumber(-8, -3, 0, 4),
                "Case 2",
            ),
            (
                TrapezoidalFuzzyNumber(-5, -4, -3, -2),
                TrapezoidalFuzzyNumber(1, 2, 3, 4),
                TrapezoidalFuzzyNumber(-20, -12, -6, -2),
                "Case 3",
            ),
            (
                TrapezoidalFuzzyNumber(-1, 0, 1, 1),
                TrapezoidalFuzzyNumber(2, 3, 4, 4),
                TrapezoidalFuzzyNumber(-4, 0, 4, 4),
                "Case 4",
            ),
            (
                TrapezoidalFuzzyNumber(-3, -2, -1, 0),
                TrapezoidalFuzzyNumber(0, 1, 2, 3),
                TrapezoidalFuzzyNumber(-9, -4, -1, 0),
                "Case 5",
            ),
            (
                TrapezoidalFuzzyNumber(-2, -1, 0, 1),
                TrapezoidalFuzzyNumber(-1, 0, 1, 2),
                TrapezoidalFuzzyNumber(-4, -1, 0, 2),
                "Case 6",
            ),
            (
                TrapezoidalFuzzyNumber(-3, -2, -1, 0),
                TrapezoidalFuzzyNumber(-2, -1, 0, 1),
                TrapezoidalFuzzyNumber(-3, 0, 2, 6),
                "Case 7",
            ),
            (
                TrapezoidalFuzzyNumber(-11, -7, -4, -2),
                TrapezoidalFuzzyNumber(-1, 4, 5, 7),
                TrapezoidalFuzzyNumber(-77, -35, -16, 11),
                "Case 8",
            ),
            (
                TrapezoidalFuzzyNumber(1, 2, 4, 5),
                TrapezoidalFuzzyNumber(-6, -4, 6, 7),
                TrapezoidalFuzzyNumber(-30, -16, 24, 35),
                "Case 9",
            ),
            (
                TrapezoidalFuzzyNumber(-4, -2, 1, 3),
                TrapezoidalFuzzyNumber(-5, 2, 4, 7),
                TrapezoidalFuzzyNumber(-28, -8, 4, 21),
                "Case 10",
            ),
        ]

        for tn1, tn2, expected_result, description in test_cases_rmul:
            with self.subTest(description=description):
                # Perform multiplication
                tn_result = tn1 * tn2

                # Assert the properties of the resulting trapezoidal fuzzy number
                self.assertLessEqual(
                    tn_result.lower_left_bound, tn_result.upper_left_bound
                )
                self.assertLessEqual(
                    tn_result.upper_left_bound, tn_result.upper_right_bound
                )
                self.assertLessEqual(
                    tn_result.upper_right_bound, tn_result.lower_right_bound
                )

                # Assert ambiguity and width
                self.assertAlmostEqual(tn_result.ambiguity, expected_result.ambiguity)
                self.assertAlmostEqual(tn_result.width, expected_result.width)

                # Assert specific boundary values
                self.assertAlmostEqual(
                    tn_result.lower_left_bound, expected_result.lower_left_bound
                )
                self.assertAlmostEqual(
                    tn_result.upper_left_bound, expected_result.upper_left_bound
                )
                self.assertAlmostEqual(
                    tn_result.upper_right_bound, expected_result.upper_right_bound
                )
                self.assertAlmostEqual(
                    tn_result.lower_right_bound, expected_result.lower_right_bound
                )

    def test_truediv(self):
        """
        Test the division method of the TrapezoidalFuzzyNumber class with various cases.

        Checks that the division method correctly handles different combinations of trapezoidal numbers.

        Test cases include both positive and negative trapezoidal fuzzy numbers.
        """
        test_cases_truediv = [
            (
                TrapezoidalFuzzyNumber(1, 2, 3, 4),
                TrapezoidalFuzzyNumber(2, 3, 4, 5),
                TrapezoidalFuzzyNumber(0.2, 0.5, 1, 2),
                "Positive Numbers Case",
            ),
        ]

        for tn1, tn2, expected_result, description in test_cases_truediv:
            with self.subTest(description=description):
                tn_result = tn1 / tn2

                # Assert the properties of the resulting trapezoidal fuzzy number
                self.assertLessEqual(
                    tn_result.lower_left_bound, tn_result.upper_left_bound
                )
                self.assertLessEqual(
                    tn_result.upper_left_bound, tn_result.upper_right_bound
                )
                self.assertLessEqual(
                    tn_result.upper_right_bound, tn_result.lower_right_bound
                )

                self.assertAlmostEqual(
                    tn_result.upper_right_bound,
                    expected_result.upper_right_bound,
                    places=4,
                    msg=f"Upper Right Bound assertion failed for {description}",
                )
                self.assertAlmostEqual(
                    tn_result.lower_right_bound,
                    expected_result.lower_right_bound,
                    places=4,
                    msg=f"Lower Right Bound assertion failed for {description}",
                )
                # Create a trapezoidal fuzzy number with invalid values
                invalid_tn = TrapezoidalFuzzyNumber(-1, 2, 3, 4)

                # Create a valid trapezoidal fuzzy number
                valid_tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)

                # Attempt to divide valid_tn by invalid_tn, which should trigger the error
                with self.assertRaises(AssertionError):
                    valid_tn / invalid_tn

    def test_rtruediv(self):
        """
        Test the division method of the TrapezoidalFuzzyNumber class with various cases.

        Checks that the division method correctly handles different combinations of trapezoidal numbers.

        Test cases include both positive and negative trapezoidal fuzzy numbers.
        """
        test_cases_rtruediv = [
            (
                TrapezoidalFuzzyNumber(1, 2, 3, 4),
                TrapezoidalFuzzyNumber(2, 3, 4, 5),
                TrapezoidalFuzzyNumber(0.2, 0.5, 1, 2),
                "Positive Numbers Case",
            ),
        ]

        for tn1, tn2, expected_result, description in test_cases_rtruediv:
            with self.subTest(description=description):
                tn_result = tn1 / tn2

                # Assert the properties of the resulting trapezoidal fuzzy number
                self.assertLessEqual(
                    tn_result.lower_left_bound, tn_result.upper_left_bound
                )
                self.assertLessEqual(
                    tn_result.upper_left_bound, tn_result.upper_right_bound
                )
                self.assertLessEqual(
                    tn_result.upper_right_bound, tn_result.lower_right_bound
                )

                self.assertAlmostEqual(
                    tn_result.upper_right_bound,
                    expected_result.upper_right_bound,
                    places=4,
                    msg=f"Upper Right Bound assertion failed for {description}",
                )
                self.assertAlmostEqual(
                    tn_result.lower_right_bound,
                    expected_result.lower_right_bound,
                    places=4,
                    msg=f"Lower Right Bound assertion failed for {description}",
                )

        # Test case for __rtruediv__
        scalar_value = 2.0
        tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        result = tn.__rtruediv__(scalar_value)

        # Assert the properties of the resulting trapezoidal fuzzy number
        self.assertLessEqual(result.lower_left_bound, result.upper_left_bound)
        self.assertLessEqual(result.upper_left_bound, result.upper_right_bound)
        self.assertLessEqual(result.upper_right_bound, result.lower_right_bound)

        self.assertAlmostEqual(
            result.lower_left_bound,
            0.5,
            places=4,
            msg="Lower Left Bound assertion failed for __rtruediv__",
        )
        self.assertAlmostEqual(
            result.upper_left_bound,
            0.6666667,
            places=4,
            msg="Upper Left Bound assertion failed for __rtruediv__",
        )
        self.assertAlmostEqual(
            result.upper_right_bound,
            1,
            places=4,
            msg="Upper Right Bound assertion failed for __rtruediv__",
        )
        self.assertAlmostEqual(
            result.lower_right_bound,
            2,
            places=4,
            msg="Lower Right Bound assertion failed for __rtruediv__",
        )

    def test_membership_function(self):
        """
        Test the membership_function method of the TrapezoidalFuzzyNumber class.

        Checks that the membership_function method correctly calculates the membership function value for a given input.

        """
        tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        self.assertEqual(tn.membership_function(2.5), 1.0)
        self.assertEqual(tn.membership_function(1.5), 0.5)
        self.assertEqual(tn.membership_function(3.5), 0.5)
        self.assertEqual(tn.membership_function(5.0), 0.0)
