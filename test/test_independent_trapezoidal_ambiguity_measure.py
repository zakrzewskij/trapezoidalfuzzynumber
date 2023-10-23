"""
This test suite includes unit tests for the methods of the IndependentTrapezoidalAmbiguityMeasurer class.
"""

import time
import unittest

import numpy as np
from ambiguity.independent_trapezoidal_ambiguity_measure import (
    IndependentTrapezoidalAmbiguityMeasurer,
)


class TestIndependentTrapezoidalAmbiguityMeasurer(unittest.TestCase):
    def test_independent_measure_data_ambiguity(self):
        """
        Test the independent_measure_data_ambiguity function.

        Checks that the independent_measure_data_ambiguity function returns a float value.

        """
        args = ((1, 2, 3, 4), (4.0, 5.0, 6.0, 7.0))
        result = (
            IndependentTrapezoidalAmbiguityMeasurer.independent_measure_data_ambiguity(
                *args
            )
        )
        self.assertIsInstance(result, float)

    def test_independent_algorithm_assertion_error(self):
        """
        Test the independent_measure_data_ambiguity function with an invalid number of input arguments.

        Checks that an AssertionError is raised when the number of input arguments is not equal to 2.

        """
        with self.assertRaises(AssertionError):
            IndependentTrapezoidalAmbiguityMeasurer.independent_measure_data_ambiguity(
                (np.array([1.0, 2.0, 3.0, 4.0]), np.array([4.0, 5.0, 6.0, 7.0]))
            )

    def test_independent_algorithm_accuracy(self):
        """
        Test the accuracy of the independent_measure_data_ambiguity function.

        Checks that the independent_measure_data_ambiguity function returns the expected result for a known test case.

        """
        args = ((1, 2, 3, 4), (1, 2, 3, 4))
        expected_result = 1  # Expected result for the given test case
        result = (
            IndependentTrapezoidalAmbiguityMeasurer.independent_measure_data_ambiguity(
                *args
            )
        )
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_independent_algorithm_performance(self):
        """
        Test the performance of the independent_measure_data_ambiguity function.

        Checks the execution time of the independent_measure_data_ambiguity function for a large input.

        """
        args = (tuple(range(1000)), tuple(range(1000, 2000)))
        start_time = time.time()
        IndependentTrapezoidalAmbiguityMeasurer.independent_measure_data_ambiguity(
            *args
        )
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLessEqual(execution_time, 10.0)


if __name__ == "__main__":
    unittest.main()
