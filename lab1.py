1 # Create a Time class with hours and minutes.
  # Overload the + operator to add two Time objects correctly.
class Time:
    def __init__(self, hours, minutes):
        total_minutes = hours * 60 + minutes
        self.hours = total_minutes // 60
        self.minutes = total_minutes % 60
    
    def __add__(self, other):
        return Time(self.hours + other.hours, self.minutes + other.minutes)
    
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

# Example usage
time1 = Time(2, 45)
time2 = Time(1, 30)
time3 = time1 + time2
print(time3)  # Output: 04:15

2  # Create a Distance class with attributes feet and inches.
   # Overload the * operator to multiply the distance by a scalar value.(any numeric value)

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet + inches // 12
        self.inches = inches % 12
    
    def __mul__(self, scalar):
        total_inches = (self.feet * 12 + self.inches) * scalar
        return Distance(total_inches // 12, total_inches % 12)
    
    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

# Example usage
dist1 = Distance(5, 8)
dist2 = dist1 * 3
print(dist2)  # Output: 17 feet 0 inches

3  # Create a Rectangle class with length and width.
   # Overload the == operator to compare the area of two rectangles.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def __eq__(self, other):
        return self.length * self.width == other.length * other.width
    
# Example usage
rect1 = Rectangle(4, 5)
rect2 = Rectangle(2, 10)
print(rect1 == rect2)  # Output: True
