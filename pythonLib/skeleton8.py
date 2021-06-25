from advalg.helpers import subsets
from advalg.graph_helpers import make_grid
from advalg.tests8 import test_max_iset, test_count_iset

# In both functions below you may assume that n >= m
# You can use make_grid(n,m) to create a grid with n rows and m columns

def max_indepset(n: int, m: int) -> int:
    """Returns the size of the maximum Independent Set in a n x m grid"""
    pass

def count_indepset(n: int, m: int) -> int:
    """Returns the number of Independent Sets in a n x m grid"""
    pass

#Testing
test_max_iset(max_indepset)
test_count_iset(count_indepset)