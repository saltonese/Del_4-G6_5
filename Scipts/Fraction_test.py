"""pytest tests for the Fraction class."""

import pytest

from Task_2_fraction import Fraction

#------------------------------------------------------
# Initieliser
#------------------------------------------------------
class TestInitialiser:
    def test_stores_numerator_and_denominator (self):
        f = Fraction(3,4)
        assert (f.numerator, f.denominator) == (3,4)

    def test_default_denominator_is_one(self):
        f = Fraction(5)
        assert (f.numerator, f.denominator) == (5,1)

