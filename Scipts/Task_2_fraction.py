"""A Fraction class with comparionsn and arithmatic via special methods """

from math import gcd #greatest commom denominator


class Fraction:
    """An imutable fraction numerator/denominatior
    
    The denominatior must be a strictly positive integer. Fractions are stored
    lowest terms, so Fraction(2, 4) and Fraction(1, 2) hold identical data.
    """

    def __init__(self, numerator, denominator = 1):
        for name, part in (("numarator", numerator),("denominator", denominator)):
            # bool is a subclass of int in pyhton, so we exclude it
            if isinstance(part, bool) or not isinstance(part, int):
                raise TypeError(f"{name} must be an integer, got {type(part).__name__}")
            if denominator <= 0:
                raise ValueError("denominator msut be more than 0 (X > 0)")

        # reduce to lowest terms. gcd is always >= 1 because denominator > 0
        divisor = gcd(numerator, denominator)
        self._numerator = numerator // divisor
        self._denominator = denominator // divisor

    #----------------------------------------------------------------------------
    # Read-only attributes
    #--------------------------------------------------------------------------------
    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    #-----------------------------------------------------------------------------
    # String repersentaions
    #----------------------------------------------------------------------
    def __repr__(self):
        return f"fraction({self._numerator}, {self._denominator})"

    def __str__(self):
        if self._denominator == 1:
            return str(self._numerator)
        return f"{self._numerator} / {self._denominator}"

    #---------------------------------------------------------------------
    # Comparisons. Cross-multiplication avoids floating point entierly:
    #   a/b < c/d  <=>  a*b < c*d   (valid beacuse b, d > 0)
    # This is why the denominator must be positive: multipying an inequality
    # with a negative number would flip its dirction
    # -----------------------------------------------------------
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._numerator * other._denominator == other._numerator * self._denominator

    def __ne__(self, other):
        result = self.__eq__(other)
        return result if result is NotImplemented else not result

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._numerator * other._denominator < other._numerator * self._denominator

    def __le__ (self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._numerator * other._denominator <= other._numerator * self._denominator

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._numerator * other._denominator > other._numerator * self._denominator

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._numerator * other._denominator >= other._numerator * self._denominator

    #--------------------------------------------------------------------
    # arithmetic
    #---------------------------------------------------------------------
    def __add__(self, other):
        if
    

