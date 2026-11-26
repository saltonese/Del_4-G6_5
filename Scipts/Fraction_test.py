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

#----------------------------------------------------------------
# Compariosns
#----------------------------------------------------------------

class TestComparisons:
    def test_equal(self):
        assert Fraction(1, 2) == Fraction (2, 4)
        assert Fraction(0, 3) == Fraction (0, 5)
        assert not (Fraction(1, 2) == Fraction (1, 3))

    def test_not_equal(self):
        assert Fraction(1, 2) != Fraction (1, 3)
        assert not (Fraction(1, 2) != Fraction (2, 4))

    def test_less_than(self):
        assert Fraction(1, 3) < Fraction (1, 2)
        assert Fraction(-1, 2) < Fraction (-1, 3)
        assert Fraction(-1, 2) < Fraction (1, 100)
        assert not (Fraction(1, 2) < Fraction (2, 4))

    def test_less_than_or_equal(self):
        assert Fraction(1, 3) <= Fraction(1, 2)
        assert Fraction(2, 4) <= Fraction(1, 2)
        assert not (Fraction(2, 3) <= Fraction(1, 2))

    def test_greater_than(self):
        assert Fraction(3, 4) > Fraction(2, 3)
        assert Fraction(-1, 3) > Fraction(-1, 2)
        assert not (Fraction(1, 2) > Fraction(2, 4))

    def test_greater_than_or_equal(self):
        assert Fraction(3, 4) >= Fraction(2, 3)
        assert Fraction(1, 2) >= Fraction(2, 4)
        assert not (Fraction(1, 3) >= Fraction(1, 2))

    def test_comperison_with_non_fraction(self):
        f = Fraction(1, 2)
        assert f.__eq__(0.5) is NotImplemented
        assert (f == 0.5) is False
        assert (f != 0.5) is True
        with pytest.raises(TypeError):
            f < 1
        with pytest.raises(TypeError):
            f >= "1/2"

    def test_sorting_uses_comparisons(self):
        fractions = [Fraction(3, 4), Fraction(-1, 2), Fraction(1, 3), Fraction(1, 2)]
        assert sorted(fractions) == [Fraction(-1, 2), Fraction(1, 3), Fraction(1, 2), Fraction(3, 4)]

#--------------------------------------------------------------------
# Other special methods
#-------------------------------------------------------------------

class TestStringRepresentations:
    def test_repr(self):
        assert repr(Fraction(3, 4)) == "Fraction(3, 4)"

    def test_repr_is_unambigious(self):
        f = Fraction(-5, 8)
        assert eval(repr(f)) == f

    def test_str(self):
        assert str(Fraction(3, 4)) == "3/4"
        assert str(Fraction(-3, 4)) == "-3/4"

    def test_str_whole_number(self):
        assert str(Fraction(4, 2)) == "2"

class TestArithmatic:
    def test_add(self):
        assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)

    def test_add_result_is_reduced(self):
        result = Fraction(1, 2) + Fraction(1, 2)
        assert (result.numerator, result.denominator) == (1, 1)

    def test_sub(self):
        assert Fraction(1, 2) - Fraction(3, 4) == Fraction(-1, 4)   

    def test_mul (self):
        assert Fraction(2, 3) * Fraction(3, 4) == Fraction(1, 2)

    def test_truediv(self):
        assert Fraction(1, 2) / Fraction(3, 4) == Fraction(2, 3)

    def test_truediv_by_negative_keeps_denominator_positive(self):
        result = Fraction(1, 2) / Fraction(-1, 4)
        assert result == Fraction(-2, 1)
        assert result.denominator > 0           
    
    def test_truediv_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 5)
 
    def test_neg(self):
         assert -Fraction(1, 2) == Fraction(-1, 2)
         assert -Fraction(-1, 2) == Fraction(1, 2)
 
    def test_abs(self):
         assert abs(Fraction(-3, 4)) == Fraction(3, 4)
         assert abs(Fraction(3, 4)) == Fraction(3, 4)
      
