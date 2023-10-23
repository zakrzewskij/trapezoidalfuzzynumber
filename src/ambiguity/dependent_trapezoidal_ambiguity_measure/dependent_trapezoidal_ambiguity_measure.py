"""
This module defines the `DependentTrapezoidalAmbiguityMeasurer` class, which extends the functionality of `TrapezoidalAmbiguityMeasurer` by implementing a permutation algorithm for testing the equality of ambiguity in two dependent fuzzy samples.
"""

import random
from typing import Tuple, Iterable

import numpy as np
from ambiguity.trapezoidal_ambiguity_measure import TrapezoidalAmbiguityMeasurer
from numpy import ndarray


class DependentTrapezoidalAmbiguityMeasurer(TrapezoidalAmbiguityMeasurer):
    def dependent_measure_data_ambiguity(*args: Iterable[ndarray]) -> float:
        """
        Permutation algorithm for testing equality of ambiguity in two dependent fuzzy samples.

        Parameters
        ----------
        *args : Iterable[ndarray]
            Input arguments consisting of two NumPy arrays.

        Returns
        -------
        float
            Result of the algorithmic calculations, which is the value of the test probability. (P-VALUE)

        Error
        ------
        AssertionError
            If the number of input arguments is not equal to 2.

        Notes
        -----
        Permutation algorithm for testing equality of ambiguity in two dependent fuzzy samples that tests the hypothesis H₀ : AMB(X) = AMB(Y) against the alternative hypothesis H₁ : AMB(X) ≠ AMB(Y) of equal ambiguity in two fuzzy samples.

        Examples
        --------
        >>> table_X = np.array([
        ...     (65, 75, 85, 85),
        ...     (35, 37, 44, 50),
        ...     (66, 70, 75, 80),
        ...     (70, 74, 80, 84),
        ...     (65, 70, 75, 80),
        ...     (45, 50, 57, 65),
        ...     (60, 66, 70, 75),
        ...     (65, 65, 70, 76),
        ...     (60, 65, 75, 80),
        ...     (55, 60, 66, 70),
        ...     (60, 65, 70, 74),
        ...     (30, 44, 46, 54),
        ...     (60, 65, 75, 75),
        ...     (70, 75, 85, 85),
        ...     (44, 45, 50, 56),
        ...     (51, 56, 64, 70),
        ...     (40, 46, 54, 60),
        ...     (55, 60, 65, 70),
        ...     (80, 85, 90, 94),
        ...     (80, 84, 90, 90),
        ... ])

        >>> table_Y = np.array([
        ...     (50, 50, 63, 75),
        ...     (39, 47, 52, 60),
        ...     (60, 70, 85, 90),
        ...     (50, 56, 64, 74),
        ...     (39, 45, 53, 57),
        ...     (55, 60, 70, 76),
        ...     (50, 50, 57, 67),
        ...     (65, 67, 80, 87),
        ...     (50, 50, 65, 75),
        ...     (50, 55, 64, 70),
        ...     (39, 46, 53, 56),
        ...     (19, 29, 41, 50),
        ...     (40, 47, 52, 56),
        ...     (54, 55, 65, 76),
        ...     (59, 65, 75, 85),
        ...     (50, 52, 57, 60),
        ...     (60, 60, 70, 80),
        ...     (50, 54, 61, 67),
        ...     (40, 46, 50, 50),
        ...     (44, 50, 56, 66),
        ... ])

        >>> result = DependentTrapezoidalAmbiguityMeasurer.dependent_measure_data_ambiguity(*TrapezoidalAmbiguityMeasurer.measure_ambiguity([table_X, table_Y]))
        >>> 0.001 <= result <= 0.003
        True
        """
        assert len(args) == 2, "Exactly 2 arguments are required."

        counter_d: int = 0
        k: int = 10000

        concat_z: Tuple[float, ...] = tuple(x - y for x, y in zip(*args))
        t_0: float = sum(concat_z)

        for _ in range(k):
            dependent_algo: float = sum(
                [random.choice([-1, 1]) * value for value in concat_z]
            )

            if abs(dependent_algo) >= abs(t_0):
                counter_d += 1

        return counter_d / k
