import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width=None):
        if width is None:
            area = math.pi * length * length
            return round(area,2)
        else:
            area_two = length * width
            return area_two
    
    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
