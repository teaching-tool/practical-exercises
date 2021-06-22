from collections import deque
from advalg.helpers import subsets
from advalg.graph_helpers import make_grid
from advalg.tests8 import test_max_iset, test_count_iset

# Assume rows >= cols
def grid_decomp(rows,cols):
    decomp = [{"type": "leaf", 'bag': []}]
    bag = deque()

    for r in range(rows):
        for c in range(cols):
            if len(bag) > cols:
                v = bag.popleft()
                decomp.append({'type': 'forget', 'bag': list(bag), 'v': v})
            v = r * cols + c
            bag.append(v)
            decomp.append({'type': 'introduce', 'bag': list(bag), "v": v})

    return decomp

def max_indepset(rows, cols):
    graph = make_grid(rows,cols)
    decomp = grid_decomp(rows,cols)
    table = [{} for t in range(len(decomp))]

    for t,node in enumerate(decomp):
        for s in map(frozenset,subsets(node['bag'])):
            if node['type'] == 'leaf':
                table[t][s] = 0
            elif node['type'] == 'introduce':
                if node['v'] not in s:
                    table[t][s] = table[t-1][s]
                elif any([graph.edge_exists(u,node["v"]) for u in s]):
                    table[t][s] = -float('inf')
                else:
                    table[t][s] = table[t-1][s-{node["v"]}] + 1
            elif node['type'] == 'forget':
                v = node["v"]
                table[t][s] = max(table[t-1][s], table[t-1][s.union({v})])

    return max(table[-1].values())

def count_indepset(rows, cols):
    graph = make_grid(rows,cols)
    decomp = grid_decomp(rows,cols)
    table = [{} for t in range(len(decomp))]

    for t,node in enumerate(decomp):
        for s in map(frozenset,subsets(node['bag'])):
            if node['type'] == 'leaf':
                table[t][s] = 1
            elif node['type'] == 'introduce':
                if node['v'] not in s:
                    table[t][s] = table[t-1][s]
                elif any([graph.edge_exists(u,node["v"]) for u in s]):
                    table[t][s] = 0
                else:
                    table[t][s] = table[t-1][s-{node["v"]}]
            elif node['type'] == 'forget':
                v = node["v"]
                table[t][s] = table[t-1][s] + table[t-1][s.union({v})]
        
    return sum(table[-1].values())

#Testing
test_max_iset(max_indepset)
test_count_iset(count_indepset)