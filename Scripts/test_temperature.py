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

@pytest.mark.parametrize("c_value, unit, expected", [
    (-273.15, "C", -459.67),
    (-40, "C", -40),
    (0, "C", 32),
    (37, "C", 98.6),
    (100, "C", 212)
])
def test_fahrenheit_conversion(c_value, unit, expected):
    temp = Temperature(c_value, unit)
    assert temp.to_fahrenheit() == pytest.approx(expected, abs=1e-9)

@pytest.mark.parametrize("f_value, unit, expected", [
    #(-459.67, "F", 0),
    (-40, "F", 233.15),
    (32, "F", 273.15),
    (98.6, "F", 310.15),
    (212, "F", 373.15)
])
def test_kelvin_conversion(f_value, unit, expected):
    temp = Temperature(f_value, unit)
    assert temp.to_kelvin() == pytest.approx(expected, abs=1e-9)

    
@pytest.mark.parametrize("k_value, unit, expected", [
    (0, "K", -273.15),
    (233.15, "K", -40),
    (273.15, "K", 0),
    (310.15, "K", 37),
    (373.15, "K", 100)
])
def test_celsius_conversion(k_value, unit, expected):
    temp = Temperature(k_value, unit)
    assert temp.to_celsius() == pytest.approx(expected, abs=1e-9)




# Round-trip conversions

temp_c_start = Temperature(25, "C")
temp_f = temp_c_start.convert_to("F")
temp_k = temp_c_start.convert_to("K")
temp_c_end = temp_f.convert_to("C")

def test_round_trip_conversion():
    assert temp_c_start == temp_c_end

# Cross-unit comparisons

def test_equal_cross_unit_comparisons():
    temp_1 = Temperature(0, "C")
    temp_2 = Temperature(32, "F")

    assert temp_1 == temp_2
    assert not (temp_1 != temp_2)
    assert temp_1 <= temp_2
    assert temp_1 >= temp_2
    assert not (temp_1 < temp_2)
    assert not (temp_1 > temp_2)
    
# Formatting

def test_repr_formatting():
    temp = Temperature(25, "C")
    assert repr(temp) == "Temperature(25.0, 'C')"

def test_str_formatting():
    temp = Temperature(25, "C")
    assert str(temp) == "25.00 °C"

# import pytest
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

@pytest.mark.parametrize("c_value, unit, expected", [
    (-273.15, "C", -459.67),
    (-40, "C", -40),
    (0, "C", 32),
    (37, "C", 98.6),
    (100, "C", 212)
])
def test_fahrenheit_conversion(c_value, unit, expected):
    temp = Temperature(c_value, unit)
    assert temp.to_fahrenheit() == pytest.approx(expected, abs=1e-9)

@pytest.mark.parametrize("f_value, unit, expected", [
    (-459.67, "F", 0),
    (-40, "F", 233.15),
    (32, "F", 273.15),
    (98.6, "F", 310.15),
    (212, "F", 373.15)
])
def test_kelvin_conversion(f_value, unit, expected):
    temp = Temperature(f_value, unit)
    assert temp.to_kelvin() == pytest.approx(expected, abs=1e-9)

    
@pytest.mark.parametrize("k_value, unit, expected", [
    (0, "K", -273.15),
    (233.15, "K", -40),
    (273.15, "K", 0),
    (310.15, "K", 37),
    (373.15, "K", 100)
])
def test_celsius_conversion(k_value, unit, expected):
    temp = Temperature(k_value, unit)
    assert temp.to_celsius() == pytest.approx(expected, abs=1e-9)




# Round-trip conversions

temp_c_start = Temperature(25, "C")
temp_f = temp_c_start.convert_to("F")
temp_k = temp_c_start.convert_to("K")
temp_c_end = temp_f.convert_to("C")

def test_round_trip_conversion():
    assert temp_c_start == temp_c_end

# Cross-unit comparisons

def test_equal_cross_unit_comparisons():
    temp_1 = Temperature(0, "C")
    temp_2 = Temperature(32, "F")

    assert temp_1 == temp_2
    assert not (temp_1 != temp_2)
    assert temp_1 <= temp_2
    assert temp_1 >= temp_2
    assert not (temp_1 < temp_2)
    assert not (temp_1 > temp_2)
    
# Formatting

def test_repr_formatting():
    temp = Temperature(25, "C")
    assert repr(temp) == "Temperature(25.0, 'C')"

def test_str_formatting():
    temp = Temperature(25, "C")
    assert str(temp) == "25.00 °C"

# python -m pytest test_temperature.py -v