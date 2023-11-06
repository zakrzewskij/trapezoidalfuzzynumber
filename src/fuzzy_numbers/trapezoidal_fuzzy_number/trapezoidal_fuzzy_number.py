"""
This module defines a concrete class for representing trapezoidal fuzzy numbers.
"""

from typing import Optional, Tuple, Callable, Union

import numpy as np
from fuzzy_numbers.algebra_fuzzy_number import AlgebraFuzzyNumber
from fuzzy_numbers.fuzzy_number_base import FuzzyNumber


class TrapezoidalFuzzyNumber(AlgebraFuzzyNumber, FuzzyNumber):
    """
    Class representing a trapezoidal fuzzy number.

    Parameters
    ----------
    *args : float
        Four values representing the trapezoidal fuzzy number (lower_left_bound, upper_left_bound, upper_right_bound, lower_right_bound).
        In the documentation to standardise conventions, all descriptions will be presented as 𝑇𝑟𝑎(a₁, a₂, a₃, a₄).
    """

    def __init__(self, *args: float) -> None:
        """
        Initialize a TrapezoidalFuzzyNumber object.

        Parameters
        ----------
        *args : float
            The four values representing the trapezoidal fuzzy number (a₁, a₂, a₃, a₄).

        Error
        ------
        ValueError
            The attributes a₁, a₂, a₃, a₄ of the trapezoidal fuzzy number are not floating-point values.
        ValueError
            The trapezoidal fuzzy number does not have exactly four boundaries, or the boundaries are invalid, specifically, if they do not follow the order: a₁ ≤ a₂ ≤ a₃ ≤ a₄.

        Examples
        --------
        >>> tn1 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> tn2 = TrapezoidalFuzzyNumber(-1, 0, 2, 3)

        """
        super().__init__(*args)
        (
            self.lower_left_bound,
            self.upper_left_bound,
            self.upper_right_bound,
            self.lower_right_bound,
        ) = args

        assert len(args) == 4, "TrapezoidalFuzzyNumber requires exactly 4 boundaries."
        assert all(
            args[i] <= args[i + 1] for i in range(len(args) - 1)
        ), "Invalid trapezoidal fuzzy number boundaries"

    @staticmethod
    def sort(*args: float) -> Tuple[float, ...]:
        """
        Sorts the trapezoidal fuzzy number values in ascending order.

        Parameters
        ----------
        *args : float
            The values of the trapezoidal fuzzy number.

        Returns
        -------
        sorted_values : Tuple[float, ...]
            The sorted values of the trapezoidal fuzzy number.

        Notes
        -----
        This static method takes a variable number of arguments (four values representing the trapezoidal fuzzy number 𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄) and sorts them in ascending order.

        Examples
        --------
        >>> result = TrapezoidalFuzzyNumber.sort(4,2,3,1)
        >>> print(result)
        (1, 2, 3, 4)

        """
        return tuple(np.sort(args))

    @property
    def core(self: "TrapezoidalFuzzyNumber") -> Tuple[float, float]:
        """
        Returns
        -------
        core : tuple of float
            The core of the trapezoidal fuzzy number represented by the upper bounds (a₂, a₃).

        Notes
        -----
        The core of a trapezoidal fuzzy number 𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄) is called the set of elements for which the membership value is equal 1, µ_A(x) = 1.

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> print(tn.core)
        (2, 3)

        """
        return self.upper_left_bound, self.upper_right_bound

    @property
    def support(self: "TrapezoidalFuzzyNumber") -> Tuple[float, float]:
        """
        Returns
        -------
        support : tuple of float
            The support of the trapezoidal fuzzy number represented by the lower bounds (a₁, a₄).

        Notes
        -----
        The support of a trapezoidal fuzzy number 𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄) is called the set of elements for which the membership value is grater than 0, µ_A(x) > 0.

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> print(tn.support)
        (1, 4)

        """
        return self.lower_left_bound, self.lower_right_bound

    @property
    def alpha_interval(self: "TrapezoidalFuzzyNumber") -> tuple[float, float]:
        """
        Returns
        -------
        alpha_interval : np.ndarray
            The alpha-cut interval of the trapezoidal fuzzy number.

        Notes
        -----
        The alpha interval of the trapezoidal fuzzy number 𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄) is defined as a tuple, whose values are calculated according to the formula:
        (a₁ + 2a₂)/6, (a₄ + 2a₃)/6

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> print(tn.alpha_interval)
        (0.8333333333333334, 1.6666666666666667)

        """
        return (
            (self.lower_left_bound + 2 * self.upper_left_bound) / 6,
            (self.lower_right_bound + 2 * self.upper_right_bound) / 6,
        )

    @property
    def ambiguity(self: "TrapezoidalFuzzyNumber") -> float:
        """
        Returns the ambiguity of the trapezoidal fuzzy number.

        Returns
        -------
        ambiguity : float
            The ambiguity of the trapezoidal fuzzy number.

        Notes
        -----
        In a general context, the uncertainty described is defined as a function:
            - 𝑈𝑛𝑐: 𝐹(ℝ) → ℝ{0}, where 𝑈𝑛𝑐(𝐴) = 0 means there is no uncertainty of the considered type in the fuzzy set 𝐴.

        Ambiguity, concerning trapezoidal fuzzy numbers, is defined as follows:
            - Amb(A) = s + (r + l)/6
            - where 𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄),
            - s = (a₃ - a₂)/2, c = (a₃ + a₂)/2, l = a₂ - a₁, r = a₄ - a₃

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> print(tn.ambiguity)
        0.8333333333333333

        """
        s = (self.upper_right_bound - self.upper_left_bound) / 2
        r = self.lower_right_bound - self.upper_right_bound
        l = self.upper_left_bound - self.lower_left_bound
        return s + (r + l) / 6

    @property
    def expected_interval(self: "TrapezoidalFuzzyNumber") -> Tuple[float, float]:
        """
        Returns the expected interval of the trapezoidal fuzzy number.

        Returns
        -------
        expected_interval : tuple of float
            The expected interval of the trapezoidal fuzzy number.

        Notes
        -----
        Expected interval, concerning the trapezoidal fuzzy number, is defined as the arithmetic mean of the values of the same side of the trapezoidal fuzzy number, according to the formula:
        (a₁ + a₂)/2, (a₃ + a₄)/2

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> print(tn.expected_interval)
        (1.5, 3.5)

        """
        return 0.5 * (self.lower_left_bound + self.upper_left_bound), 0.5 * (
            self.lower_right_bound + self.upper_right_bound
        )

    @property
    def value(self: "TrapezoidalFuzzyNumber") -> float:
        """

        Returns
        -------
        value : float
            The value of the trapezoidal fuzzy number.

        Notes
        -----
        The value of the trapezoidal fuzzy number is calculated by summing the values of the tuple of the resulting alpha_interval method, according to the formula:
        (a₁ + 2a₂ + 2a₃ + a₄)/6

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> print(tn.value)
        2.5

        """
        start, end = self.alpha_interval
        return end + start

    @property
    def expected_value(self: "TrapezoidalFuzzyNumber") -> float:
        """

        Returns
        -------
        expected_value : float
            The expected value of the trapezoidal fuzzy number.

        Notes
        -----
        The expectation value of the trapezoidal fuzzy number is the arithmetic mean values of the tuple of the resulting expected_interval method, according to the formula:
        (a₁ + a₂ + a₃ + a₄)/4

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> print(tn.expected_value)
        2.5

        """
        start, end = self.expected_interval
        return (start + end) / 2

    @property
    def width(self: "TrapezoidalFuzzyNumber") -> float:
        """
        Returns the width of the trapezoidal fuzzy number.

        Returns
        -------
        width : float
            The width of the trapezoidal fuzzy number.

        Notes
        -----
        The width of the trapezoidal fuzzy number is defined as the largest value of the membership function h(𝐴) = sup µₐ(x), which is the difference between the values of the tuple of the resulting expected_interval method , according to the formula:
        ((-a₁) + (-a₂) + a₃ + a₄)/2

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> print(tn.width)
        2.0

        """
        start, end = self.expected_interval
        return end - start

    @property
    def is_near_zero(self: "TrapezoidalFuzzyNumber") -> bool:
        """
        Check if the trapezoidal fuzzy number is a near-zero TrFN (Trapezoidal Fuzzy Number).

        Returns
        -------
        bool
            True if the trapezoidal fuzzy number is a near-zero TrFN, False otherwise.

        Notes
        -----
        A trapezoidal fuzzy number is arbitrary whether the attributes a₁, a₂, a₃, a₄ of a trapezoidal fuzzy number satisfy the condition a₁ < a₂ ≤ a₃ < 0 < a₄ or a₁ < a₂ < 0 < a₃ < a₄ or a₁ < 0 ≤ a₂ < a₃ < a₄, which are conditions for a near-zero trapezoidal fuzzy number.

        Examples
        --------
        >>> obj = TrapezoidalFuzzyNumber(-1, 0, 0.5, 1)
        >>> print(obj.is_near_zero)
        True

        >>> obj = TrapezoidalFuzzyNumber(-2, 2, 3, 4)
        >>> print(obj.is_near_zero)
        True

        >>> obj = TrapezoidalFuzzyNumber(0, 0.5, 1, 2)
        >>> print(obj.is_near_zero)
        False

        >>> obj = TrapezoidalFuzzyNumber(-5, -2, -1, 0)
        >>> print(obj.is_near_zero)
        False
        """
        return (
            (
                self.lower_left_bound
                < self.upper_left_bound
                <= self.upper_right_bound
                < 0
                < self.lower_right_bound
            )
            or (
                self.lower_left_bound
                < self.upper_left_bound
                < 0
                < self.upper_right_bound
                < self.lower_right_bound
            )
            or (
                self.lower_left_bound
                < 0
                <= self.upper_left_bound
                < self.upper_right_bound
                < self.lower_right_bound
            )
        )

    # TODO
    @property
    def is_positive(self: "TrapezoidalFuzzyNumber") -> bool:
        """
        Check if the trapezoidal fuzzy number is positive.

        Returns
        -------
        bool
            True if the trapezoidal fuzzy number is positive, False otherwise.

        Notes
        -----
        The trapezoidal fuzzy number is positive if and only if the a₁ is greater than or equal to 0.

        Examples
        --------
        >>> obj = TrapezoidalFuzzyNumber(-2, -1, 0, 1)
        >>> print(obj.is_positive)
        False

        >>> obj = TrapezoidalFuzzyNumber(0, 0, 1, 2)
        >>> print(obj.is_positive)
        True

        >>> obj = TrapezoidalFuzzyNumber(0, 2, 5, 6)
        >>> print(obj.is_positive)
        True

        """
        return self.lower_left_bound >= 0

    # TODO
    @property
    def is_negative(self: "TrapezoidalFuzzyNumber") -> bool:
        """
        Check if the trapezoidal fuzzy number is negative.

        Returns
        -------
        bool
            True if the trapezoidal fuzzy number is negative, False otherwise.

        Notes
        -----
        The trapezoidal fuzzy number is negative if and only if the a₁ atrubute of the trapezoidal fuzzy number is less than 0.

        Examples
        --------
        >>> obj = TrapezoidalFuzzyNumber(-3,-2,-1,0)
        >>> print(obj.is_negative)
        True

        >>> obj = TrapezoidalFuzzyNumber(0,1,2,3)
        >>> print(obj.is_negative)
        False

        """
        return self.lower_right_bound <= 0

    @property
    def is_arbitrary(self: "TrapezoidalFuzzyNumber") -> bool:
        """
        Check if the trapezoidal fuzzy number is arbitrary.

        Returns
        -------
        bool
            True if the a₁ attribute of the trapezoidal fuzzy number is less than 0 and the a₄ attribute of the trapezoidal fuzzy number is greater than 0, otherwise False.

        Notes
        -----
        The trapezoidal fuzzy number is arbitrary if and only if the a₁and a₄ of the trapezoidal fuzzy number satisfies the condition a₁ < 0 <  a₄.

        Examples
        --------
        >>> obj = TrapezoidalFuzzyNumber(-2, 1, 2, 3)
        >>> print(obj.is_arbitrary)
        True

        >>> obj = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> print(obj.is_arbitrary)
        False

        >>> obj = TrapezoidalFuzzyNumber(0, 0, 3, 4)
        >>> print(obj.is_arbitrary)
        False
        """
        return self.lower_left_bound < 0 < self.lower_right_bound

    def __add__(
        self: "TrapezoidalFuzzyNumber", other: "TrapezoidalFuzzyNumber"
    ) -> "TrapezoidalFuzzyNumber":
        """
        Add two trapezoidal fuzzy numbers.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber
            The first trapezoidal fuzzy number.
        other : TrapezoidalFuzzyNumber
            The other trapezoidal fuzzy number to add.

        Returns
        -------
        result : TrapezoidalFuzzyNumber
            The result of adding two trapezoidal fuzzy numbers.

        Notes
        -----
        The addition of two trapezoidal fuzzy numbers 𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄) and 𝐵 = 𝑇𝑟𝑎(b₁, b₂, b₃, b₄) is performed by adding the corresponding values 𝑇𝑟𝑎(a₁ + b₁, a₂ + b₂, a₃ + b₃, a₄ + b₄) of both trapezoidal fuzzy numbers.
        Examples
        --------
        >>> tn1 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> tn2 = TrapezoidalFuzzyNumber(2, 3, 4, 5)
        >>> tn3 = tn1 + tn2
        >>> print(tn3)
        TrapezoidalFuzzyNumber(a=3, b=5, c=7, d=9)
        Support: (3, 9)
        Core: (5, 7)
        Ambiguity of the trapezoidal fuzzy number: 1.6667)

        """
        (
            lower_left_bound,
            upper_left_bound,
            upper_right_bound,
            lower_right_bound,
        ) = self.sort(
            self.lower_left_bound + other.lower_left_bound,
            self.upper_left_bound + other.upper_left_bound,
            self.upper_right_bound + other.upper_right_bound,
            self.lower_right_bound + other.lower_right_bound,
        )

        return TrapezoidalFuzzyNumber(
            lower_left_bound, upper_left_bound, upper_right_bound, lower_right_bound
        )

    def __sub__(
        self: "TrapezoidalFuzzyNumber", other: "TrapezoidalFuzzyNumber"
    ) -> "TrapezoidalFuzzyNumber":
        """
        Subtract two trapezoidal fuzzy numbers.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber
            The first trapezoidal fuzzy number.
        other : TrapezoidalFuzzyNumber
            The other trapezoidal fuzzy number to subtract.

        Returns
        -------
        result : TrapezoidalFuzzyNumber
            The result of subtracting two trapezoidal fuzzy numbers.

        Notes
        -----
        The subtraction of two trapezoidal fuzzy numbers 𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄) and 𝐵 = 𝑇𝑟𝑎(b₁, b₂, b₃, b₄) is performed by subtracting the corresponding values 𝑇𝑟𝑎(a₁ - b₄, a₂ - b₃, a₃ - b₂, a₄ - b₁) of both trapezoidal fuzzy numbers.

        Examples
        --------
        >>> tn1 = TrapezoidalFuzzyNumber(3, 4, 5, 6)
        >>> tn2 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> tn3 = tn1 - tn2
        >>> print(tn3)
        TrapezoidalFuzzyNumber(a=-1, b=1, c=3, d=5)
        Support: (-1, 5)
        Core: (1, 3)
        Ambiguity of the trapezoidal fuzzy number: 1.6667)

        """
        (
            lower_left_bound,
            upper_left_bound,
            upper_right_bound,
            lower_right_bound,
        ) = self.sort(
            self.lower_left_bound - other.lower_right_bound,
            self.upper_left_bound - other.upper_right_bound,
            self.upper_right_bound - other.upper_left_bound,
            self.lower_right_bound - other.lower_left_bound,
        )

        return TrapezoidalFuzzyNumber(
            lower_left_bound, upper_left_bound, upper_right_bound, lower_right_bound
        )

    def __neg__(self: "TrapezoidalFuzzyNumber") -> "TrapezoidalFuzzyNumber":
        """

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber
             The trapezoidal fuzzy number.

        Returns
        -------
        TrapezoidalFuzzyNumber
            Symmetric image of a trapezoidal fuzzy number.

        Notes
        -----
        The symmetric image of the trapezoidal fuzzy number is obtained by reflecting the trapezoid across the vertical axis passing through the centroid.

        Examples
        --------
        >>> num = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> symmetric_num = -num
        >>> print(symmetric_num)
        TrapezoidalFuzzyNumber(a=-4, b=-3, c=-2, d=-1)
        Support: (-4, -1)
        Core: (-3, -2)
        Ambiguity of the trapezoidal fuzzy number: 0.8333)

        """
        values = (
            self.lower_right_bound,
            self.upper_right_bound,
            self.upper_left_bound,
            self.lower_left_bound,
        )
        negated_values = tuple(map(lambda x: -x, values))
        return TrapezoidalFuzzyNumber(*negated_values)

    def __mul__(
        self: "TrapezoidalFuzzyNumber", other: Union["TrapezoidalFuzzyNumber", float]
    ) -> "TrapezoidalFuzzyNumber":
        """
        Perform right-side multiplication between trapezoidal fuzzy numbers and number.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber
            The trapezoidal fuzzy number.
        other : float
            Number by which the trapezoidal fuzzy number is multiplied.

        Returns
        -------
        TrapezoidalFuzzyNumber
            The result of right-side multiplication of trapezoidal fuzzy number by number.

        Examples
        --------
        >>> tn1 = TrapezoidalFuzzyNumber(-3, -1, 0, 4)
        >>> tn2 = 2.0
        >>> result = tn1 * tn2
        >>> print(result)
        TrapezoidalFuzzyNumber(a=-6, b=-2, c=0, d=8)
        Support: (-6, 8)
        Core: (-2, 0)
        Ambiguity of the trapezoidal fuzzy number: 3.0000)

        """
        if isinstance(other, TrapezoidalFuzzyNumber):
            return self.__rmul__(other)
        elif isinstance(other, float):
            multiply_internal: Callable[
                ["TrapezoidalFuzzyNumber", "TrapezoidalFuzzyNumber"],
                Tuple[float, float],
            ] = lambda x, y: (other * x, other * y)
            return TrapezoidalFuzzyNumber(
                min(multiply_internal(self.lower_left_bound, self.lower_right_bound)),
                min(multiply_internal(self.upper_left_bound, self.upper_right_bound)),
                max(multiply_internal(self.upper_left_bound, self.upper_right_bound)),
                max(multiply_internal(self.lower_left_bound, self.lower_right_bound)),
            )
        else:
            raise TypeError(
                "Unsupported operand type. The multiplier must be either TrapezoidalFuzzyNumber or float."
            )

    def __rmul__(
        self: "TrapezoidalFuzzyNumber", other: "TrapezoidalFuzzyNumber"
    ) -> "TrapezoidalFuzzyNumber":
        """
        Perform right-side multiplication between two trapezoidal fuzzy numbers.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber
            The trapezoidal fuzzy number.
        other : TrapezoidalFuzzyNumber
            The other trapezoidal fuzzy number for multiplication.

        Returns
        -------
        TrapezoidalFuzzyNumber
            The result of the arbitrary multiplication.

        Notes
        -----
        Right-side multiplication is a special type of multiplication in which the current trapezoidal fuzzy number is on the right-hand side of the multiplication operator (*). The right-side multiplication can result in one of the following cases:
           - Arbitrary multiplication: If both trapezoidal fuzzy numbers have arbitrary boundaries, the result is obtained by performing the arbitrary multiplication of the two trapezoidal fuzzy numbers.
           - Restricted multiplication: If both trapezoidal fuzzy numbers have the same sign (both positive or both negative), the result is obtained by performing restricted multiplication, element-wise multiplication of the boundaries.
           - Semi-restricted multiplication: If one trapezoidal fuzzy number has arbitrary boundaries, and the other has semi-restricted boundaries (a₁ < a₂ ≤ 0 ≤ a₃ < a₄), the result is obtained by performing semi-restricted multiplication.
           - Semi-restricted multiplication with near-zero: If one trapezoidal fuzzy number has near-zero boundaries and the other has arbitrary boundaries, the result is obtained by performing semi-restricted multiplication with near-zero.

        Examples
        --------
        >>> tn1 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> tn2 = TrapezoidalFuzzyNumber(-1, 0, 2, 3)
        >>> tn3 = TrapezoidalFuzzyNumber(-4, -3, -2, 0)
        >>> tn4 = TrapezoidalFuzzyNumber(-1, 0, 0, 4)

        >>> tn = tn1 * tn2
        >>> print(tn)
        TrapezoidalFuzzyNumber(a=-4, b=0, c=6, d=12)
        Support: (-4, 12)
        Core: (0, 6)
        Ambiguity of the trapezoidal fuzzy number: 4.6667)

        >>> tn = tn1 * tn3
        >>> print(tn)
        TrapezoidalFuzzyNumber(a=-16, b=-9, c=-4, d=0)
        Support: (-16, 0)
        Core: (-9, -4)
        Ambiguity of the trapezoidal fuzzy number: 4.3333)

        >>> tn = tn1 * tn4
        >>> print(tn)
        TrapezoidalFuzzyNumber(a=-4, b=0, c=0, d=16)
        Support: (-4, 16)
        Core: (0, 0)
        Ambiguity of the trapezoidal fuzzy number: 3.3333)

        >>> tn = tn2 * tn3
        >>> print(tn)
        TrapezoidalFuzzyNumber(a=-12, b=-6, c=0, d=4)
        Support: (-12, 4)
        Core: (-6, 0)
        Ambiguity of the trapezoidal fuzzy number: 4.6667)

        """
        if self.is_arbitrary and other.is_arbitrary:
            return TrapezoidalFuzzyNumber.arbitrary_multiplication(self, other)
        else:
            if (
                (self.is_positive and other.is_positive)
                or (self.is_negative and other.is_negative)
                or (self.is_positive and other.is_negative)
                or (self.is_negative and other.is_positive)
            ):
                return TrapezoidalFuzzyNumber.restricted_multiplication(self, other)
            else:
                if (self.is_arbitrary and (other.is_positive or other.is_negative)) or (
                    other.is_arbitrary and (self.is_positive or self.is_negative)
                ):
                    return self.semi_restricted_multiplication(other)
                else:
                    if (self.is_near_zero and other.is_arbitrary) or (
                        self.is_arbitrary and other.is_near_zero
                    ):
                        return self.semi_restricted_with_near_zero_multiplication(other)
                    else:
                        raise ValueError(
                            "Invalid combination of trapezoidal fuzzy numbers."
                        )

    def arbitrary_multiplication(
        self: "TrapezoidalFuzzyNumber", other: "TrapezoidalFuzzyNumber"
    ) -> "TrapezoidalFuzzyNumber":
        """
        Perform the arbitrary multiplication of two trapezoidal fuzzy numbers.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber
            The trapezoidal fuzzy number.
        other : TrapezoidalFuzzyNumber
            The other trapezoidal fuzzy number to multiply with.

        Returns
        -------
        TrapezoidalFuzzyNumber
            The result of the arbitrary multiplication.

        Notes
        -----
        The arbitrary multiplication of two trapezoidal fuzzy numbers  𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄), 𝐵 = 𝑇𝑟𝑎(b₁, b₂, b₃, b₄) is defined as follows:
            - E = min(a₁ * b₁, a₁ * b₄, a₄ * b₁, a₄ * b₄)
            - F = min(a₂ * b₂, a₂ * b₃, a₃ * b₂, a₃ * b₃)
            - G = max(a₂ * b₂, a₂ * b₃, a₃ * b₂, a₃ * b₃)
            - H = max(a₁ * b₁, a₁ * b₄, a₄ * b₁, a₄ * b₄)
            - Tra(E, F, G, H)

        Examples
        --------
        >>> tn1 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> tn2 = TrapezoidalFuzzyNumber(2, 3, 4, 5)
        >>> result = tn1.arbitrary_multiplication(tn2)
        >>> result
        TrapezoidalFuzzyNumber(a=2, b=6, c=12, d=20, support=(2, 20), core=(6, 12), ambiguity=5.0000, width=12.0000)

        """
        return TrapezoidalFuzzyNumber(
            min(
                self.lower_left_bound * other.lower_left_bound,
                self.lower_left_bound * other.lower_right_bound,
                self.lower_right_bound * other.lower_left_bound,
                self.lower_right_bound * other.lower_right_bound,
            ),
            min(
                self.upper_left_bound * other.upper_left_bound,
                self.upper_left_bound * other.upper_right_bound,
                self.upper_right_bound * other.upper_left_bound,
                self.upper_right_bound * other.upper_right_bound,
            ),
            max(
                self.upper_left_bound * other.upper_left_bound,
                self.upper_left_bound * other.upper_right_bound,
                self.upper_right_bound * other.upper_left_bound,
                self.upper_right_bound * other.upper_right_bound,
            ),
            max(
                self.lower_left_bound * other.lower_left_bound,
                self.lower_left_bound * other.lower_right_bound,
                self.lower_right_bound * other.lower_left_bound,
                self.lower_right_bound * other.lower_right_bound,
            ),
        )

    def restricted_multiplication(
        self: "TrapezoidalFuzzyNumber", other: "TrapezoidalFuzzyNumber"
    ) -> "TrapezoidalFuzzyNumber":
        """
        Perform restricted multiplication between two trapezoidal fuzzy numbers.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber
            The trapezoidal fuzzy number.
        other : TrapezoidalFuzzyNumber
            The other trapezoidal fuzzy number for multiplication.

        Returns
        -------
        TrapezoidalFuzzyNumber
            The result of the restricted multiplication.

        Notes
        -----
        Restricted multiplication is performed based on the signs of the trapezoidal fuzzy numbers 𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄), 𝐵 = 𝑇𝑟𝑎(b₁, b₂, b₃, b₄).
            - If both trapezoidal fuzzy numbers are positive, the result is the element-wise multiplication of their boundaries.
            - If both trapezoidal fuzzy numbers are negative, the result is the element-wise multiplication of their boundaries, but in reverse order.
            - If one trapezoidal fuzzy number is positive and the other is negative, the result is the element-wise multiplication of the first trapezoidal fuzzy number's boundaries with the reverse order of the second trapezoidal fuzzy number's boundaries.

        Examples
        --------
        >>> tn1 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> tn2 = TrapezoidalFuzzyNumber(2, 3, 4, 5)
        >>> result = tn1.restricted_multiplication(tn2)
        >>> result
        TrapezoidalFuzzyNumber(a=2, b=6, c=12, d=20, support=(2, 20), core=(6, 12), ambiguity=5.0000, width=12.0000)
        """
        if self.is_positive and other.is_positive:
            return TrapezoidalFuzzyNumber(
                self.lower_left_bound * other.lower_left_bound,
                self.upper_left_bound * other.upper_left_bound,
                self.upper_right_bound * other.upper_right_bound,
                self.lower_right_bound * other.lower_right_bound,
            )
        elif self.is_negative and other.is_negative:
            return TrapezoidalFuzzyNumber(
                self.lower_right_bound * other.lower_right_bound,
                self.upper_right_bound * other.upper_right_bound,
                self.upper_left_bound * other.upper_left_bound,
                self.lower_left_bound * other.lower_left_bound,
            )
        elif self.is_positive and other.is_negative:
            return TrapezoidalFuzzyNumber(
                self.lower_right_bound * other.lower_left_bound,
                self.upper_right_bound * other.upper_left_bound,
                self.upper_left_bound * other.upper_right_bound,
                self.lower_left_bound * other.lower_right_bound,
            )
        elif self.is_negative and other.is_positive:
            return TrapezoidalFuzzyNumber(
                self.lower_left_bound * other.lower_right_bound,
                self.upper_left_bound * other.upper_right_bound,
                self.upper_right_bound * other.upper_left_bound,
                self.lower_right_bound * other.lower_left_bound,
            )

    def semi_restricted_multiplication(
        self: "TrapezoidalFuzzyNumber", other: "TrapezoidalFuzzyNumber"
    ) -> "TrapezoidalFuzzyNumber":
        """
        Perform semi-restricted multiplication between two trapezoidal fuzzy numbers.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber
            The trapezoidal fuzzy number.
        other : TrapezoidalFuzzyNumber
            The other trapezoidal fuzzy number for multiplication.

        Returns
        -------
        TrapezoidalFuzzyNumber
             The result of the semi-restricted multiplication.

        Notes
        -----
        Semi-restricted multiplication is a special type of multiplication that involves one arbitrary trapezoidal fuzzy number and one semi-restricted trapezoidal fuzzy number 𝐵 = 𝑇𝑟𝑎(b₁, b₂, b₃, b₄).

            An arbitrary trapezoidal fuzzy number can have any position of boundaries without any specific order. A semi-restricted trapezoidal fuzzy number should have the property: b₁ < b₂ ≤ 0 ≤ b₃ < b₄.

        Examples
        --------
        >>> tn1 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> tn2 = TrapezoidalFuzzyNumber(-1, 0, 1, 2)
        >>> result = tn1.semi_restricted_multiplication(tn2)
        >>> result
        TrapezoidalFuzzyNumber(a=-4, b=0, c=3, d=8, support=(-4, 8), core=(0, 3), ambiguity=3.0000, width=7.5000)

        """
        if self.is_positive and other.is_arbitrary:
            return TrapezoidalFuzzyNumber(
                min(
                    self.lower_left_bound * other.lower_left_bound,
                    self.lower_right_bound * other.lower_left_bound,
                ),
                min(
                    self.upper_left_bound * other.upper_left_bound,
                    self.upper_right_bound * other.upper_left_bound,
                ),
                max(
                    self.upper_left_bound * other.upper_right_bound,
                    self.upper_right_bound * other.upper_right_bound,
                ),
                max(
                    self.lower_left_bound * other.lower_right_bound,
                    self.lower_right_bound * other.lower_right_bound,
                ),
            )
        elif self.is_negative and other.is_arbitrary:
            return TrapezoidalFuzzyNumber(
                min(
                    self.lower_left_bound * other.lower_right_bound,
                    self.lower_right_bound * other.lower_right_bound,
                ),
                min(
                    self.upper_left_bound * other.upper_right_bound,
                    self.upper_right_bound * other.upper_right_bound,
                ),
                max(
                    self.upper_right_bound * other.upper_left_bound,
                    self.upper_left_bound * other.upper_left_bound,
                ),
                max(
                    self.lower_right_bound * other.lower_left_bound,
                    self.lower_left_bound * other.lower_left_bound,
                ),
            )
        elif self.is_arbitrary and other.is_positive:
            return TrapezoidalFuzzyNumber(
                min(
                    self.lower_left_bound * other.lower_left_bound,
                    self.lower_left_bound * other.lower_right_bound,
                ),
                min(
                    self.upper_left_bound * other.upper_left_bound,
                    self.upper_left_bound * other.upper_right_bound,
                ),
                max(
                    self.upper_right_bound * other.upper_left_bound,
                    self.upper_right_bound * other.upper_right_bound,
                ),
                max(
                    self.lower_right_bound * other.lower_left_bound,
                    self.lower_right_bound * other.lower_right_bound,
                ),
            )
        elif self.is_arbitrary and other.is_negative:
            return TrapezoidalFuzzyNumber(
                min(
                    self.lower_right_bound * other.lower_left_bound,
                    self.lower_right_bound * other.lower_right_bound,
                ),
                min(
                    self.upper_right_bound * other.upper_left_bound,
                    self.upper_right_bound * other.upper_right_bound,
                ),
                max(
                    self.upper_left_bound * other.upper_right_bound,
                    self.upper_left_bound * other.upper_left_bound,
                ),
                max(
                    self.lower_left_bound * other.lower_right_bound,
                    self.lower_left_bound * other.lower_left_bound,
                ),
            )
        else:
            raise ValueError("Invalid combination of trapezoidal fuzzy numbers.")

    def semi_restricted_with_near_zero_multiplication(
        self: "TrapezoidalFuzzyNumber", other: "TrapezoidalFuzzyNumber"
    ) -> "TrapezoidalFuzzyNumber":
        """
        Perform semi-restricted multiplication with near-zero for a trapezoidal fuzzy number.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber
            The trapezoidal fuzzy number.
        other : TrapezoidalFuzzyNumber
            The other trapezoidal fuzzy number for semi-restricted multiplication.

        Returns
        -------
        TrapezoidalFuzzyNumber
            The result of the semi-restricted multiplication with near-zero.

        Notes
        -----
        Semi-restricted multiplication with near-zero is a special type of multiplication where one of the trapezoidal fuzzy number 𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄) has near-zero boundaries (a₁ or a₄ is close to zero) and the other trapezoidal fuzzy number 𝐵 = 𝑇𝑟𝑎(b₁, b₂, b₃, b₄) is arbitrary.

        Examples
        --------
        >>> tn1 = TrapezoidalFuzzyNumber(0, 0.5, 1, 2)
        >>> tn2 = TrapezoidalFuzzyNumber(-1, -0.5, 0, 1)
        >>> result = tn1.semi_restricted_with_near_zero_multiplication(tn2)
        >>> result
        TrapezoidalFuzzyNumber(a=-2, b=-0.5, c=0, d=2, support=(-2, 2), core=(-0.5, 0), ambiguity=0.8333, width=2.2500)

        """
        if (
            self.lower_left_bound
            < self.upper_left_bound
            < self.upper_right_bound
            <= 0
            <= self.lower_right_bound
        ) and other.is_arbitrary:
            return TrapezoidalFuzzyNumber(
                min(
                    self.lower_left_bound * other.lower_right_bound,
                    self.lower_right_bound * other.lower_left_bound,
                ),
                min(
                    self.upper_left_bound * other.upper_right_bound,
                    self.upper_right_bound * other.upper_right_bound,
                ),
                max(
                    self.upper_right_bound * other.upper_left_bound,
                    self.upper_left_bound * other.upper_left_bound,
                ),
                max(
                    self.lower_right_bound * other.lower_right_bound,
                    self.lower_left_bound * other.lower_left_bound,
                ),
            )
        elif (
            self.lower_left_bound
            < self.upper_left_bound
            <= 0
            <= self.upper_right_bound
            < self.lower_right_bound
        ) and other.is_arbitrary:
            return TrapezoidalFuzzyNumber(
                min(
                    self.lower_left_bound * other.lower_right_bound,
                    self.lower_right_bound * other.lower_left_bound,
                ),
                min(
                    self.upper_left_bound * other.upper_right_bound,
                    self.upper_right_bound * other.upper_left_bound,
                ),
                max(
                    self.upper_left_bound * other.upper_left_bound,
                    self.upper_right_bound * other.upper_right_bound,
                ),
                max(
                    self.lower_right_bound * other.lower_right_bound,
                    self.lower_left_bound * other.lower_left_bound,
                ),
            )
        elif (
            self.lower_left_bound
            <= 0
            <= self.upper_left_bound
            < self.upper_right_bound
            < self.lower_right_bound
        ) and other.is_arbitrary:
            return TrapezoidalFuzzyNumber(
                min(
                    self.lower_left_bound * other.lower_right_bound,
                    self.lower_right_bound * other.lower_left_bound,
                ),
                min(
                    self.upper_left_bound * other.upper_right_bound,
                    self.upper_right_bound * other.upper_left_bound,
                ),
                max(
                    self.upper_left_bound * other.upper_right_bound,
                    self.upper_right_bound * other.upper_right_bound,
                ),
                max(
                    self.lower_right_bound * other.lower_right_bound,
                    self.lower_left_bound * other.lower_left_bound,
                ),
            )
        elif self.is_arbitrary and (
            other.lower_left_bound
            < other.upper_left_bound
            < other.upper_right_bound
            <= 0
            <= other.lower_right_bound
        ):
            return TrapezoidalFuzzyNumber(
                min(
                    self.lower_right_bound * other.lower_left_bound,
                    self.lower_left_bound * other.lower_right_bound,
                ),
                min(
                    self.upper_right_bound * other.upper_left_bound,
                    self.upper_right_bound * other.upper_right_bound,
                ),
                max(
                    self.upper_left_bound * other.upper_right_bound,
                    self.upper_left_bound * other.upper_left_bound,
                ),
                max(
                    self.lower_left_bound * other.lower_left_bound,
                    self.lower_right_bound * other.lower_right_bound,
                ),
            )
        elif self.is_arbitrary and (
            other.lower_left_bound
            < other.upper_left_bound
            <= 0
            <= other.upper_right_bound
            < other.lower_right_bound
        ):
            return TrapezoidalFuzzyNumber(
                min(
                    self.lower_right_bound * other.lower_left_bound,
                    self.lower_left_bound * other.lower_right_bound,
                ),
                min(
                    self.upper_right_bound * other.upper_left_bound,
                    self.upper_left_bound * other.upper_right_bound,
                ),
                max(
                    self.upper_left_bound * other.upper_left_bound,
                    self.upper_right_bound * other.upper_right_bound,
                ),
                max(
                    self.lower_left_bound * other.lower_left_bound,
                    self.lower_right_bound * other.lower_right_bound,
                ),
            )
        elif self.is_arbitrary and (
            other.lower_left_bound
            <= 0
            <= other.upper_left_bound
            < other.upper_right_bound
            < other.lower_right_bound
        ):
            return TrapezoidalFuzzyNumber(
                min(
                    self.lower_right_bound * other.lower_left_bound,
                    self.lower_left_bound * other.lower_right_bound,
                ),
                min(
                    self.upper_left_bound * other.upper_left_bound,
                    self.upper_left_bound * other.upper_right_bound,
                ),
                max(
                    self.upper_right_bound * other.upper_left_bound,
                    self.upper_right_bound * other.upper_right_bound,
                ),
                max(
                    self.lower_left_bound * other.lower_left_bound,
                    self.lower_right_bound * other.lower_right_bound,
                ),
            )
        else:
            raise ValueError("Invalid combination of trapezoidal fuzzy numbers.")

    def __truediv__(
        self: Union["TrapezoidalFuzzyNumber", float], other: "TrapezoidalFuzzyNumber"
    ) -> "TrapezoidalFuzzyNumber":
        """
        Divide a trapezoidal fuzzy number by another trapezoidal fuzzy number.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber or float
            The first trapezoidal fuzzy number.
        other : TrapezoidalFuzzyNumber
            The other trapezoidal fuzzy number for divide.

        Returns
        -------
        result : TrapezoidalFuzzyNumber
            The result of dividing the by the trapezoidal fuzzy number.

        Notes
        -----
        The __truediv__ method is internally linked to the __rtruediv__ method to support division of a scalar float by the trapezoidal fuzzy number.

        Examples
        --------
        >>> tn1 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> tn2 = TrapezoidalFuzzyNumber(2, 3, 4, 5)
        >>> tn3 = tn1 / tn2
        >>> print(tn3)
        TrapezoidalFuzzyNumber(a=0.2, b=0.5, c=1, d=2)
        Support: (0.2, 2)
        Core: (0.5, 1)
        Ambiguity of the trapezoidal fuzzy number: 0.4667)

        """
        if isinstance(self, TrapezoidalFuzzyNumber):
            assert self.is_positive, "TrapezoidalFuzzyNumber must be positive."
            values = [
                other.lower_left_bound,
                other.upper_left_bound,
                other.upper_right_bound,
                other.lower_right_bound,
            ]
            assert all(
                isinstance(val, (int, float)) and val > 0 for val in values
            ), "All values in `other` must be non-zero positive real numbers."
        elif isinstance(self, float):
            assert self > 0, "The float value must be a non-zero positive real number."
            return other.__rtruediv__(self)
        else:
            raise ValueError(
                "Invalid type for division. Expected TrapezoidalFuzzyNumber or float."
            )

        (
            lower_left_bound,
            upper_left_bound,
            upper_right_bound,
            lower_right_bound,
        ) = sorted(
            [
                self.lower_left_bound / other.lower_right_bound,
                self.upper_left_bound / other.upper_right_bound,
                self.upper_right_bound / other.upper_left_bound,
                self.lower_right_bound / other.lower_left_bound,
            ]
        )

        return TrapezoidalFuzzyNumber(
            lower_left_bound, upper_left_bound, upper_right_bound, lower_right_bound
        )

    def __rtruediv__(
        self: "TrapezoidalFuzzyNumber", number: Union[int, float]
    ) -> "TrapezoidalFuzzyNumber":
        """
        Divide a number by a trapezoidal fuzzy number.

        Parameters
        ----------
        number : int or float
            The number to be divided by the trapezoidal fuzzy number.

        Returns
        -------
        result : TrapezoidalFuzzyNumber
            The result of the division the number by trapezoidal fuzzy number.

        Notes
        -----
        Division of a scalar by the trapezoidal fuzzy number is not commutative, so the order matters. It calculates the result as number / self (scalar divided by trapezoidal fuzzy number).

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> scalar_value = 2.0
        >>> result = scalar_value / tn
        >>> print(result)
        TrapezoidalFuzzyNumber(a=0.5, b=0.666667, c=1, d=2)
        Support: (0.5, 2)
        Core: (0.666667, 1)
        Ambiguity of the trapezoidal fuzzy number: 0.3611)

        """
        assert (
            isinstance(number, (int, float)) and number > 0
        ), "Number must be a non-zero positive real number."

        return TrapezoidalFuzzyNumber(
            number / self.lower_right_bound,
            number / self.upper_right_bound,
            number / self.upper_left_bound,
            number / self.lower_left_bound,
        )

    def __repr__(self: "TrapezoidalFuzzyNumber") -> str:
        """
        Return a string representation of the trapezoidal fuzzy number.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber or float
            The trapezoidal fuzzy number.

        Returns
        -------
        representation : str
            String representation of the trapezoidal fuzzy number.

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> print(tn.__repr__())
        TrapezoidalFuzzyNumber(a=1, b=2, c=3, d=4, support=(1, 4), core=(2, 3), ambiguity=0.8333, width=2.0000)

        Notes
        -----
        The string representation is returned in the format 𝑇𝑟𝑎(a₁, a₂, a₃, a₄), support, core, ambiguity, width).
        """
        parameters = (
            f"a={self.lower_left_bound:g}, b={self.upper_left_bound:g}, c={self.upper_right_bound:g}, "
            f"d={self.lower_right_bound:g}"
        )
        support = f"support=({self.support[0]:g}, {self.support[1]:g})"
        core = f"core=({self.core[0]:g}, {self.core[1]:g})"
        ambiguity = f"ambiguity={self.ambiguity:.4f}"
        width = f"width={self.width:.4f}"

        return f"TrapezoidalFuzzyNumber({parameters}, {support}, {core}, {ambiguity}, {width})"

    def __str__(self: "TrapezoidalFuzzyNumber") -> str:
        """
        Return a string representation of the trapezoidal fuzzy number.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber or float
            The trapezoidal fuzzy number.

        Returns
        -------
        representation : str
            String representation of the trapezoidal fuzzy number.


        Notes
        -----
        The string representation is returned in the format:
            The string representation is returned in the format:
            'TrapezoidalFuzzyNumber(a₁, a₂, a₃, a₄)
            \nSupport:(min_support, max_support)
            \nCore: (min_core, max_core)
            \nAmbiguity of the trapezoidal fuzzy number: ambiguity_value)'

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> print(tn)
        TrapezoidalFuzzyNumber(a=1, b=2, c=3, d=4)
        Support: (1, 4)
        Core: (2, 3)
        Ambiguity of the trapezoidal fuzzy number: 0.8333)

        """
        parameters = (
            f"a={self.lower_left_bound:g}, b={self.upper_left_bound:g}, c={self.upper_right_bound:g}, "
            f"d={self.lower_right_bound:g})"
        )
        support = f"Support: ({self.support[0]:g}, {self.support[1]:g})"
        core = f"Core: ({self.core[0]:g}, {self.core[1]:g})"
        ambiguity = f"Ambiguity of the trapezoidal fuzzy number: {self.ambiguity:.4f}"

        return f"TrapezoidalFuzzyNumber({parameters}\n{support}\n{core}\n{ambiguity})"

    def membership_function(self: "TrapezoidalFuzzyNumber", position: float) -> float:
        """
        Compute the membership function value of the trapezoidal fuzzy number at a given position.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber
            The trapezoidal fuzzy number.
        position : float
            The position at which to compute the membership function value.

        Returns
        -------
        membership : float
            The membership function value of the trapezoidal fuzzy number at the given position.

        Notes
        -----
        The membership function value of a trapezoidal fuzzy number 𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄) is defined as follows:

        µ_A(x) = {
                0                           for x < a₁, \n
                (x - a₁) / (a₂ - a₁)     for a₁ ≤ x < a₂, \n
                1                           for a₂ ≤ x < a₃, \n
                (a₄ - x) / (a₄ - a₃)     for a₃ < x ≤ a₄, \n
                0                           for x > a₄. \n
            }

                Membership function assume 0 value when the x element doesn't belong to the fuzzy set  A.

                    Membership function takes the value  1 when the x element fully belongs to the fuzzy set  A.

                        Membership function takes the value beetwen 0 and 1 when the x element partly belongs to the fuzzy set  A.

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
        >>> print(tn.membership_function(2.5))
        1

        """
        return (
            0
            if position < self.lower_left_bound or position > self.lower_right_bound
            else (position - self.lower_left_bound)
            / (self.upper_left_bound - self.lower_left_bound)
            if self.lower_left_bound <= position < self.upper_left_bound
            else 1
            if self.upper_left_bound <= position < self.upper_right_bound
            else (self.lower_right_bound - position)
            / (self.lower_right_bound - self.upper_right_bound)
        )

    def calculate_alpha_cut(
        self: "TrapezoidalFuzzyNumber",
    ) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """
        Calculate the alpha-cut of the trapezoidal fuzzy number.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber
            The trapezoidal fuzzy number.

        Returns
        -------
        alpha_cut :
            Tuple[Tuple[float, float], Tuple[float, float]] Tuple containing two sub-tuples representing the alpha-cut values.
        support :
            Tuple[float, float] Tuple containing the support values  of the trapezoidal fuzzy number.

        Notes
        -----
        The alpha-cut of a trapezoidal fuzzy number 𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄) is a crisp interval obtained by
        cutting off the tails of the trapezoid according to the membership function value.

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(0.2, 0.5, 1, 2)
        >>> tn_alpha_cut = tn.calculate_alpha_cut()
        >>> print(tn_alpha_cut)
        ((0.5, 1), (0.2, 2))
        >>> tn_alpha_cut, support = tn.calculate_alpha_cut()
        >>> print(support)
        (0.2, 2)

        """
        return (
            (
                (self.upper_left_bound - self.lower_left_bound) + self.lower_left_bound,
                -(self.lower_right_bound - self.upper_right_bound)
                + self.lower_right_bound,
            ),
            self.support,
        )

    def membership_function_string(
        self: "TrapezoidalFuzzyNumber", position: "Optional[float]" = None
    ) -> str:
        """
        Format the fuzzy function string.

        Parameters
        ----------
        self : TrapezoidalFuzzyNumber
            The trapezoidal fuzzy number.
        position : float or None, optional
            The value of 'x' to be used in the fuzzy function. If not provided, the string 'x' will be used.

        Returns
        -------
        str
            The formatted membership string.

        Notes
        -----
        The membership function value of a trapezoidal fuzzy number 𝐴 = 𝑇𝑟𝑎(a₁, a₂, a₃, a₄) is defined as follows:

        µ_A(x) = {
                0                           for x < a₁,\n
                (x - a₁) / (a₂ - a₁)     for a₁ ≤ x < a₂,\n
                1                           for a₂ ≤ x < a₃,\n
                (a₄ - x) / (a₄ - a₃)     for a₃ < x ≤ a₄,\n
                0                           for x > a₄.\n
                }

        Examples
        --------
        >>> tn = TrapezoidalFuzzyNumber(-1, -0.25, 0.76, 4)
        >>> fuzzy_str = tn.membership_function_string()
        >>> print(fuzzy_str)
                0                 x ∈ (-∞, -1),
                (x + 1)/0.75      x ∈ [-1,  -0.25),
        µ(x) =  1                 x ∈ [-0.25,  0.76],
                (4 - x)/3.24      x ∈ (0.76,  4],
                0                 x ∈ (4, ∞).
        """

        if position is None:
            position = "x"

        lines = [
            f'{" " * 8}0{" " * 17}x \u2208 (-\u221E, {self.lower_left_bound}),',
            f'{" " * 8}({position} {"+" if self.lower_left_bound < 0 else "-"} {abs(self.lower_left_bound)})/{self.upper_left_bound - self.lower_left_bound}{" " * 6}x \u2208 [{self.lower_left_bound},  {self.upper_left_bound}),',
            f'{chr(181)}(x) = {" " * 1}1{" " * 17}x \u2208 [{self.upper_left_bound},  {self.upper_right_bound}],',
            f'{" " * 8}({self.lower_right_bound} - {position})/{self.lower_right_bound - self.upper_right_bound}{" " * 6}x \u2208 ({self.upper_right_bound},  {self.lower_right_bound}],',
            f'{" " * 8}0{" " * 17}x \u2208 ({self.lower_right_bound}, \u221E).',
        ]
        return "\n".join(lines)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
