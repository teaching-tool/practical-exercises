import math

class Circle:
    def __init__(self, x:float, y:float, radius:float, color):
        """Construct a circle at position (x,y) with the given radius and color"""
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def area(self) -> float:
        """Returns the area of the circle"""
        return math.pi * self.radius * self.radius

    def inside(self, x:float, y:float) -> bool:
        """Is the point (x,y) inside the circle"""
        dx = x - self.x
        dy = y - self.y
        return math.sqrt(dx*dx + dy*dy) <= self.radius