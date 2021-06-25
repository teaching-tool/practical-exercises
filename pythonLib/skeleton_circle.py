from typing import List, Tuple
from random import random, uniform
from advalg.circle import Circle
from advalg.tests_circle import test_circle_sampler

# Implement the CircleSampler class below
# Do not change the signature of the methods but feel free to add more
# Points are represented as a tuple of floats (x,y)

class CircleSampler:
    def __init__(self, circles: List[Circle]):
        """Constructs a CircleSampler for the given list of circles"""
        pass

    def sample(self) -> Tuple[int, Tuple[float, float]]:
        """Returns the index of the chosen circle and a point from it"""
        pass

    def good_sample(self, circle_index: int, point: Tuple[int, int]):
        """Is the given sample good?"""
        pass

# Tests your implementation of the CircleSampler
# You can change the number of samples used and the animation delay
test_circle_sampler(CircleSampler, samples=350, delay=50)