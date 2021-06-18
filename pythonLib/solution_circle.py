from random import random, uniform
from advalg.tests_circle import test_circle_sampler

class CircleSampler:
    def __init__(self, circles):
        self.circles = circles
        self.total_area = sum([c.area() for c in circles])
        self.prob = [c.area() / self.total_area for c in circles]

    def sample(self):
        c_i = self._pick_circle()
        p = self._pick_point(c_i)
        return c_i, p

    def good_sample(self, c_i, p):
        (x,y) = p
        for i in range(c_i):
            c = self.circles[i]
            if c.inside(x, y):
                return False
        return True

    def _pick_circle(self):
        cprob = 0
        r = random()

        for i,p in enumerate(self.prob):
            cprob += p
            if r <= cprob:
                return i

    def _pick_point(self, c_i):
        c = self.circles[c_i]
        x = c.x + uniform(-1, 1) * c.radius
        y = c.y + uniform(-1, 1) * c.radius

        if not c.inside(x,y):
            return self._pick_point(c_i)

        return x,y

test_circle_sampler(CircleSampler, samples=350, delay=50)