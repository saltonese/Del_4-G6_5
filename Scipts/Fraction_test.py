"""pytest tests for the Fraction class."""

import pytest

from Task_2_fraction import Fraction

#------------------------------------------------------
# Initieliser
#------------------------------------------------------
class TestInitialiser:
    def test_stores_numerator_and_denominator (self):
        f = Fraction(3, 4)
        assert (f.numerator, f.denominator) == (3,4)

    def test_default_denominator_is_one(self):
        f = Fraction(5)
        assert (f.numerator, f.denominator) == (5,1)

    def test_is_reduced_to_lowest_terms(self):
        f = Fraction(6, 8)
        assert (f.numerator, f.denominator) == (3, 4)

    def test_negative_numerator_is_allowed(self):
        f = Fraction(-2, 6)
        assert (f.numerator, f.denominator) == (-1, 3)

    def test_zero_numerator(self):
        f = Fraction(0, 7)
        assert (f.numerator, f.denominator) == (0, 1)

    @pytest.mark.parametrize("denominator", [0, -1, -5])
    def test_non_positive_denominator_raises_value_error(self, denominator):
        with pytest.raises(ValueError):
            Fraction(1, denominator)

    @pytest.mark.parametrize("numerator, denominator", [
        (1.5, 2), (1, 2.0), ("1", 2), (1, "2"), (None, 2), (1, None), 
        (True, 2), (1, False),
    ])
    def test_non_integers_raise_type_error(self, numerator, denominator):
        with pytest.raises(TypeError):
            Fraction(numerator, denominator)

    def test_attributes_are_read_only(self):
        f = Fraction(1, 2)
        with pytest.raises(AttributeError):
            f.numerator = 3
        with pytest.raises(AttributeError):
            f.denominator = 3

