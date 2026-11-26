class Temperature:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

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

    def convert_to(self, target_unit: str) -> Temperature:
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
            return f"{self.value:.2f}°{self.unit.upper()}"
        elif self.unit.upper() == "K":
            return f"{self.value:.2f} {self.unit.upper()}"




            
    def __eq__(self, other):
        if isinstance(other, Temperature):
            return self.to_celsius() == other.to_celsius()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Temperature):
            return self.to_celsius() != other.to_celsius()
        return NotImplemented