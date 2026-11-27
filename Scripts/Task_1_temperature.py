class Temperature:
    def __init__(self, value, unit="C"):
        if unit.upper() not in ("C", "F", "K"):
            raise ValueError("Invalid unit. Use C, F or K.")
        self._value = float(value)
        self._unit = unit.upper()
        if self.to_kelvin() < 0:
            raise ValueError("Temperature cannot be below absolute zero.")

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit
    
    def to_celsius(self) -> float:
        if self.unit.upper() == 'C':
            return self.value
        if self.unit.upper() == 'F':
            return (self.value - 32) * (5 / 9)
        if self.unit.upper() == 'K':
            return self.value - 273.15
        
    def to_fahrenheit(self) -> float:
        if self.unit.upper() == 'C':
            return (self.value * (9 / 5)) + 32
        if self.unit.upper() == 'F':
            return self.value
        if self.unit.upper() == 'K':
            return (self.value - 273.15) * (9 / 5) + 32

    def to_kelvin(self) -> float:
        if self.unit.upper() == 'C':
            return self.value + 273.15
        if self.unit.upper() == 'F':
            return (self.value - 32) * (5 / 9) + 273.15
        if self.unit.upper() == 'K':
            return self.value

    def convert_to(self, target_unit: str):
        if target_unit.upper() == 'C':
            value = self.to_celsius()
        elif target_unit.upper() == 'F':
            value = self.to_fahrenheit()
        elif target_unit.upper() == 'K':
            value = self.to_kelvin()
        else:
            raise ValueError("Invalid unit. Please use 'C', 'F', or 'K'.")
        return Temperature(value, target_unit)

    def __repr__(self) -> str:
        return f"Temperature({self.value}, '{self.unit}')"

    def __str__(self) -> str:
        if self.unit.upper() in ("C", "F"):
            return f"{self.value:.2f} °{self.unit.upper()}"
        elif self.unit.upper() == "K":
            return f"{self.value:.2f} {self.unit.upper()}"
            
    def __eq__(self, other):
        if isinstance(other, Temperature):
            temp1 = self.to_celsius()
            temp2 = other.to_celsius()
            if abs(temp1 - temp2) < 1e-9:
                return True
            else:
                return False
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Temperature):
            temp1 = self.to_celsius()
            temp2 = other.to_celsius()
            if abs(temp1 - temp2) >= 1e-9:
                return True
            else:
                return False
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Temperature):
            temp1 = self.to_celsius()
            temp2 = other.to_celsius()
            if temp1 - temp2 < -1e-9:
                return True
            else:
                return False
        return NotImplemented
            
    def __le__(self, other):
        if isinstance(other, Temperature):
            return self.__lt__(other) or self.__eq__(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Temperature):
            temp1 = self.to_celsius()
            temp2 = other.to_celsius()
            if temp1 - temp2 > 1e-9:
                return True
            else:
                return False
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Temperature):
            return self.__gt__(other) or self.__eq__(other)
        return NotImplemented




"""
a = Temperature(0, "C")
b = Temperature(32, "F")
c = Temperature(273.15, "K")

# Likhet
print(a == b)
print(b == c)

# Ordering
print(a < Temperature(10, "C"))
print(a > Temperature(-10, "C"))

# Read-only
a_value = 10

# Ugyldig enhet
Temperature(20, "f")
"""





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