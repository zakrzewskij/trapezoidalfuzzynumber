"""
This module defines the `TrapezoidalAmbiguityMeasurer` class, which extends the functionality of AmbiguityMeasureBase by implementing method, which computes the ambiguity for a list of source NumPy arrays containing trapezoidal fuzzy number.
"""
from typing import Tuple

import numpy as np
from ambiguity.ambiguity_measure_base import AmbiguityMeasure
from fuzzy_numbers.trapezoidal_fuzzy_number import TrapezoidalFuzzyNumber


class TrapezoidalAmbiguityMeasurer(AmbiguityMeasure):
    def measure_ambiguity(self: list[np.ndarray]) -> Tuple[Tuple[float, ...], ...]:
        """
        Computes the ambiguity for list of source NumPy arrays containing trapezoidal fuzzy numbers.

        Parameters
        ----------
        self : list of ndarray
            List of source NumPy arrays containing trapezoidal fuzzy numbers.

        Returns
        -------
        result_tables_ambiguity : tuple of float
            Tuple of tuples representing the ambiguity values for each trapezoidal fuzzy number in the source NumPy arrays.

        Error
        ------
        TypeError
            If the conversion to trapezoidal fuzzy number fails or an error occurs.


        Examples
        --------
        >>> table_X = np.array([
        ...     (65, 75, 85, 85),
        ...     (35, 37, 44, 50),
        ...     (66, 70, 75, 80),
        ...     (70, 74, 80, 84)
        ... ])

        >>> table_Y = np.array([
        ...     (50, 50, 63, 75),
        ...     (39, 47, 52, 60),
        ...     (60, 70, 85, 90),
        ...     (50, 56, 64, 74)
        ... ])

        >>> TrapezoidalAmbiguityMeasurer.measure_ambiguity([table_X, table_Y])
        ((6.666666666666667, 4.833333333333333, 4.0, 4.333333333333333), (8.5, 5.166666666666666, 10.0, 6.666666666666666))

        >>> result = TrapezoidalAmbiguityMeasurer.measure_ambiguity([table_X, table_Y])
        >>> assert all(isinstance(obj, float) for result_tuple in result for obj in result_tuple), f"Invalid types in the result tuple: {result}"

        Notes
        -----
        This function takes a list of NumPy arrays containing trapezoidal fuzzy numbers and calculates the ambiguity value for each trapezoidal fuzzy number. The ambiguity value is a measure of the fuzziness of the trapezoidal fuzzy number and is calculated using the `ambiguity` method of the `TrapezoidalNumber` class.

            The function returns the results as a tuple of tuples, where each inner tuple represents the ambiguity values for the trapezoidal fuzzy numbers in a specific NumPy array. Each element in the inner tuple corresponds to the ambiguity of the trapezoidal fuzzy number in the corresponding position in the NumPy array.

                The ambiguity value represents the spread or uncertainty of the trapezoidal fuzzy number. A lower ambiguity value indicates a more precise and well-defined trapezoidal fuzzy number, while a higher ambiguity value indicates greater fuzziness or uncertainty in the trapezoidal fuzzy number.
        """
        result_tables_ambiguity = tuple(
            tuple(
                (
                    TrapezoidalFuzzyNumber(*row).ambiguity
                    if isinstance(TrapezoidalFuzzyNumber(*row), TrapezoidalFuzzyNumber)
                    else (TrapezoidalFuzzyNumber(*row),)
                )
                for row in source_arr
            )
            for source_arr in self
        )

        assert all(
            isinstance(obj, float)
            for result_tuple in result_tables_ambiguity
            for obj in result_tuple
        ), f"Invalid types in the result tuple: {result_tables_ambiguity}"

        return result_tables_ambiguity
