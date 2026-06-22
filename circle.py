# Creating a circle class to calculate area and circumference
import math 

# Calculate area of a circle
def calc_area(radius):
    area = math.pi * radius ** 2

    return area

# Calculate circumference of a circle 
def calc_circumference(radius):
    circum = 2 * math.pi * radius
    
    return circum