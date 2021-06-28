from typing import Callable

max_tests = [
    (4,4,8),
    (6,6,18),
    (8,10,40),
    (30,10,150),
]

count_tests = [
    (4,4,1234),
    (6,6,5598861),
    (8,10,512615852515459),
    (12,12,162481813349792588536582997),
]

def test_max_iset(max_iset: Callable[[int, int], int]) -> None:
    """Tests the implementation of the DP for maximum independent set"""
    print(f"Testing: {max_iset.__name__}...")
    for r,c,m in max_tests:
        res = max_iset(r,c)
        if res != m: 
            print(f"Max iset {r}x{c} test failed. Expected {m} got {res}")
        else: 
            print(f"Max iset {r}x{c} test passed!")

def test_count_iset(count_iset: Callable[[int,int], int]) -> None:
    """Tests the implementation of the DP for counting independent sets"""
    print(f"Testing: {count_iset.__name__}...")
    for r,c,n in count_tests:
        res = count_iset(r,c)
        if res != n: 
            print(f"Count isets {r}x{c} test failed. Expected {n} got {res}")
        else:
            print(f"Count isets {r}x{c} test passed!")