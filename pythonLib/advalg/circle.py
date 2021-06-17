import math

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def area(self):
        return math.pi * self.radius * self.radius

    def inside(self, x, y):
        dx = x - self.x
        dy = y - self.y
        return math.sqrt(dx*dx + dy*dy) <= self.radius