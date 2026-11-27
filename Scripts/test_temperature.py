import pytest
from Task_1_temperature import Temperature



# Initialization

temp = Temperature(20) 
                   
def test_default_unit():
    assert temp.unit == "C"

def test_case_insensitive():
    temp1 = Temperature(20, "c")
    temp2 = Temperature(20, "C")
    assert temp1.unit == temp2.unit
    
def test_read_only_bechavior():
    with pytest.raises(AttributeError):
        temp.unit = "F"
    with pytest.raises(AttributeError):
        temp.value = 30

# Validation

def test_invalid_unit():
    with pytest.raises(ValueError):
        Temperature(25, "X")

def test_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-300, "C")
    with pytest.raises(ValueError):
        Temperature(-500, "F")
    with pytest.raises(ValueError):
        Temperature(-10, "K")


# Conversions

@pytest.mark.parametrize("value, unit, expected", [
    (-273.15, "C", 0),
    (-40, "C", -40),
    (0, "C", 32),
    (37, "C", 98.6),
    (100, "C", 212)
])
def test_fahrenheit_conversion(value, unit, expected):
    temp = Temperature(value, unit)
    assert temp.to_fahrenheit() == pytest.approx(expected, abs=1e-9)

@pytest.mark.parametrize("value, unit, expected", [
    (),
    (),
    (),
    (),
    ()
])
def test_fahrenheit_conversion(value, unit, expected):
    temp = Temperature(value, unit)
    assert temp.to_fahrenheit() == pytest.approx(expected, abs=1e-9)

    
@pytest.mark.parametrize("value, unit, expected", [
    (),
    (),
    (),
    (),
    ()
])
def test_fahrenheit_conversion(value, unit, expected):
    temp = Temperature(value, unit)
    assert temp.to_fahrenheit() == pytest.approx(expected, abs=1e-9)




# Round-trip conversions




# Cross-unit comparisons



# Formatting







# python -m pytest test_temperature.py -v