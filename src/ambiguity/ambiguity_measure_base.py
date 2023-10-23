"""
This module defines an abstract base class for ambiguity measures of fuzzy numbers. Concrete classes should implement the `measure_ambiguity` method to calculate the ambiguity
value for a list of fuzzy numbers.
"""

from abc import ABC, abstractmethod

import numpy as np


class AmbiguityMeasure(ABC):
    """
    Abstract base class representing an ambiguity measure.
    """

    @abstractmethod
    def measure_ambiguity(self: list[np.ndarray]) -> float:
        """
        Return the ambiguity value of the fuzzy number.
        """
        return NotImplemented
