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