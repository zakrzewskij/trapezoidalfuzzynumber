"""
This class defines the interface for algebraic fuzzy number classes, providing the structure for performing basic arithmetic operations on fuzzy numbers.
"""

from abc import ABC, abstractmethod
from typing import Union

from fuzzy_numbers.fuzzy_number_base import FuzzyNumber


class AlgebraFuzzyNumber(FuzzyNumber, ABC):
    """
    Abstract base class representing an algebraic fuzzy number.
    """

    def __init__(self: "FuzzyNumber", *args: float) -> None:
        super().__init__(*args)

    @abstractmethod
    def __add__(self: "FuzzyNumber", other: "FuzzyNumber"):
        return NotImplemented

    @abstractmethod
    def __sub__(self: "FuzzyNumber", other: "FuzzyNumber"):
        return NotImplemented

    @abstractmethod
    def __mul__(self: "FuzzyNumber", other: Union["FuzzyNumber", float]):
        return NotImplemented

    @abstractmethod
    def __truediv__(self: "FuzzyNumber", other: Union["FuzzyNumber", float]):
        return NotImplemented


if __name__ == "__main__":
    import doctest

    doctest.testmod()
