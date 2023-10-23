"""
This module defines an abstract base class for representing fuzzy numbers.
"""

from abc import ABC, abstractmethod
from typing import Tuple


class FuzzyNumber(ABC):
    """
    Abstract base class representing a fuzzy number.

    This class defines the interface for fuzzy number classes.

    Definition 1:
        A fuzzy set 𝐴 in a certain space 𝑋 is defined as a set of ordered pairs:
            - 𝐴 = {⟨𝑥, 𝑢𝐴(𝑥)⟩: 𝑥 ∈ 𝑋}
            - where the function 𝜇𝐴:𝑋 → 𝐹([0,1]) is called the membership function of the fuzzy set 𝐴.

    Definition 2:
        A fuzzy set 𝐴 is termed normal if there exists at least one element belonging entirely to the set, i.e.,
            - 𝑥 ∈ 𝑋 such that 𝑢𝐴(𝑥) = 1.

    Definition 3:
        The support of the fuzzy set 𝐴 is defined as the following non-fuzzy set of those elements in the space 𝑋 that fully belong to 𝐴 to any nonzero degree:
            - 𝑠𝑢𝑝𝑝 𝐴 = {𝑥 ∈ 𝑋: 𝜇𝐴(𝑥) > 0}

    Definition 4:
        A fuzzy set 𝐴 is convex if, for all 𝑥₁, 𝑥₂ ∈ 𝑋, and for all 𝜆 ∈ [0,1], the inequality holds:
            - 𝜇𝐴(𝜆𝑥₁ + (1 − 𝜆)𝑥₂) ≥ 𝜇𝐴(𝑥₁) ∧ 𝜇𝐴(𝑥₂) where the operator ∧ denotes the minimum.

    Definition 5:
        A function 𝑓 is upper semi continuous at the point 𝑥₀ ∈ 𝑋 if 𝑥₀ is an isolated point in the set 𝑋 or 𝑥₀ is a limit point of the set 𝑋 and the following holds:
            - lim_{{𝑥→𝑥₀}} 𝑠𝑢𝑝 𝑓(𝑥) ≤ 𝑓(𝑥₀).

    Definition 6:
        A fuzzy subset 𝐴 of the set of real numbers ℝ is called a fuzzy number if and only when:
            - 𝐴 is a normal fuzzy set,
            - 𝐴 is a convex fuzzy set,
            - the membership function of the fuzzy set 𝐴 is semi-continuous from above,
            - the carrier of the fuzzy set is bounded.

    """

    def __init__(self: "FuzzyNumber", *args: float) -> None:
        pass

    @property
    @abstractmethod
    def core(self: "FuzzyNumber") -> Tuple[float, float]:
        """
        Returns the core of the fuzzy number.

        Returns
        -------
        core : tuple of float
            The core of the fuzzy number.

        """

    @property
    @abstractmethod
    def support(self: "FuzzyNumber") -> Tuple[float, float]:
        """
        Returns the support of the fuzzy number.

        Returns
        -------
        support : tuple of float
            The support of the fuzzy number.

        """

    @property
    @abstractmethod
    def alpha_interval(self: "FuzzyNumber") -> Tuple[float, float]:
        """
        Return the alpha-cut interval of the fuzzy number.

        Returns
        -------
        alpha_interval : tuple of float
            The alpha-cut interval of the fuzzy number.

        """

    @property
    @abstractmethod
    def ambiguity(self: "FuzzyNumber") -> float:
        """
        Returns the ambiguity of the fuzzy number.

        Returns
        -------
        ambiguity : float
            The ambiguity of the fuzzy number.

        Notes
        -----
        In a general context, the uncertainty described is defined as a function:
            - 𝑈𝑛𝑐: 𝐹(ℝ) → ℝ{0}, where 𝑈𝑛𝑐(𝐴) = 0 means there is no uncertainty of the considered type in the fuzzy set 𝐴.
        """

    @property
    @abstractmethod
    def expected_interval(self: "FuzzyNumber") -> Tuple[float, float]:
        """
        Return the expected interval of the fuzzy number.

        Returns
        -------
        expected_interval : tuple of float
            The expected interval of the fuzzy number.

        """

    @property
    @abstractmethod
    def expected_value(self: "FuzzyNumber") -> float:
        """
        Return the expected value of the fuzzy number.

        Returns
        -------
        expected_value : float
            The expected value of the fuzzy number.

        """

    @property
    @abstractmethod
    def width(self: "FuzzyNumber") -> float:
        """
        Return the width of the fuzzy number.

        Returns
        -------
        width : float
            The width of the fuzzy number.

        """
