"""pytest tests for the Fraction class."""

import pytest

from Task_2_fraction import Fraction

#------------------------------------------------------
# Initieliser
#------------------------------------------------------
class TestInitialiser:
    def test_stores_numerator_and_denominator (self):
        