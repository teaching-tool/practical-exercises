from math import sin, cos, atan2, sqrt, pi
from typing import Iterable, Iterator, Tuple
import itertools

def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371000
    phi1 = lat1 * pi/180
    phi2 = lat2 * pi/180
    delta_phi = (lat2 - lat1) * pi/180
    delta_lambda = (lon2 - lon1) * pi/180

    a = sin(delta_phi/2) ** 2 + cos(phi1) * cos(phi2) * sin(delta_lambda/2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return R * c

def combinations(items: Iterable, count: int) -> Iterator[Tuple]:
    l = list(items)
    assert(0 <= count <= len(l))
    return itertools.combinations(l, count)

def permutations(items: Iterable, count: int) -> Iterator[Tuple]:
    l = list(items)
    assert(0 <= count <= len(l))
    return itertools.permutations(l, count)

def subsets(items: Iterable) -> Iterator[Tuple]:
    l = list(items)
    return itertools.chain.from_iterable(combinations(l, c) for c in range(len(l)+1))

def choose(n: int, k: int) -> int:
    if (k == 0): return 1
    return (n * choose(n-1, k-1)) // k

# TODO statistical physics formula