import pytest
from Scripts.Task_1_temperature import Temperature



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

def test_conversions():
    temp_c = Temperature(-273.15, "C")
    temp_f = Temperature(-459.67, "F")
    temp_k = Temperature(0, "K")




    



# Round-trip conversions




# Cross-unit comparisons



# Formatting







# python -m pytest test_temperature.py -v