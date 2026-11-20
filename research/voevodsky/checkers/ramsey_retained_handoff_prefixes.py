"""Count witnessed handoffs on the fixed tea/delivery prefixes. Standard library."""
from itertools import combinations, permutations

WANTS, REGION = 'TCT', 'EWW'  # Ada, Ben, Cy
CATEGORY, SHIPS = 'TTCCKKJTTT', 'EWEWEWEWEW'
EDGES = list(permutations(range(3), 2))

def counts(k):
    paths = {(a,b): {p for p in range(k) if WANTS[a] == CATEGORY[p] and REGION[b] == SHIPS[p]} for a,b in EDGES}
    shared = sum(len(paths[e] & paths[f]) for e,f in combinations(EDGES, 2))
    total = sum(map(len, paths.values()))
    loops = sum(WANTS[a] == CATEGORY[p] and REGION[a] == SHIPS[p] for a in range(3) for p in range(k))
    assert total + loops == sum(WANTS.count(CATEGORY[p]) * REGION.count(SHIPS[p]) for p in range(k))
    return [len(paths[e]) for e in EDGES], total, shared, total + loops

if __name__ == '__main__':
    for k in range(6,11): print(k,*counts(k))
