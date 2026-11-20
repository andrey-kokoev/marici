"""Check all red offset tables for two free C4 orbits. Standard library only."""
from collections import Counter
from itertools import combinations, product


def main():
    vertices = range(8)  # U_i=i, V_i=4+i
    within = [set(), {2}, {1, 3}, {1, 2, 3}]
    counts = Counter()
    tables = []
    for u, v, mask in product(within, within, range(16)):
        cross = {d for d in range(4) if mask >> d & 1}
        def red(i, j):
            # i < j, so a cross-orbit edge is always read U -> V.
            offsets = cross if i//4 != j//4 else (u if i < 4 else v)
            return (j-i) % 4 in offsets
        triangles = sum(all(red(i,j) for i,j in combinations(t,2)) for t in combinations(vertices,3))
        blue4 = sum(not any(red(i,j) for i,j in combinations(t,2)) for t in combinations(vertices,4))
        counts['tested'] += 1
        if not triangles:
            counts['triangle-free'] += 1
            if not blue4:
                tables.append((sorted(u),sorted(v),sorted(cross)))
        if (u,v,cross)==({1,3},{1,3},{0}): assert (triangles,blue4)==(0,2)
        if (u,v,cross)==({2},{2},{0,3}): assert (triangles,blue4)==(0,0)
    print(counts,'valid tables',len(tables)); print(*tables,sep='\n')

if __name__=='__main__': main()
