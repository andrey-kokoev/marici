"""Eight-node counterexample: identical nested traversals and Euclidean geometry,
maximal triangle-free A-relations with different independence numbers.
Run with Python 3; no dependencies.
"""
from itertools import combinations
from math import cos, sin, pi

V = range(8)
e = lambda i, j: tuple(sorted((i, j)))
ALL = set(combinations(V, 2))
X = [(cos(pi*i/4), sin(pi*i/4), 0.) for i in V]
a = (0, 1, 2, 3, 4)
b = (0, 3, 6, 1, 4, 7, 2, 5)
A1 = {e(i, (i+1)%8) for i in V} | {e(i, (i+4)%8) for i in range(4)}
A2 = (A1 - {e(4,5),e(6,7)}) | {e(0,6),e(3,5)}

def cycle_edges(cycle):
    return {e(cycle[i], cycle[(i+1)%len(cycle)]) for i in range(len(cycle))}

def independent_sets(A, r):
    return [s for s in combinations(V, r) if all(e(i,j) not in A for i,j in combinations(s,2))]

def has_triangle(A):
    return any(all(e(i,j) in A for i,j in combinations(s,2)) for s in combinations(V,3))

def two_step(A,i,j):
    return any(e(i,k) in A and e(k,j) in A for k in V if k!=i and k!=j)

def check(name,A,expected_alpha):
    B=ALL-A
    assert cycle_edges(a) <= A
    assert cycle_edges(b) <= B
    assert not has_triangle(A)
    assert all(two_step(A,i,j) for i,j in B)  # maximal triangle-free, (A^2)_offdiag=B
    assert all(not two_step(A,i,j) for i,j in A) # no A triangle
    alpha=max(r for r in range(1,9) if independent_sets(A,r))
    assert alpha==expected_alpha
    print(f'{name}: edges={len(A)}; alpha={alpha}; A^2=B (off-diagonal); A/B cycles verified')
    return independent_sets(A,alpha)[0]

for cycle in (a,b):
    for axis in range(3):
        assert abs(sum(X[cycle[(k+1)%len(cycle)]][axis]-X[cycle[k]][axis]
                       for k in range(len(cycle))))<1e-12
print('Same embedded nodes; both Euclidean cycles have zero resultant displacement.')
print('Structure I example B-group:', check('I', A1,3))
print('Structure II example B-group:', check('II', A2,4))
print('Changed A-edges:', sorted(A1-A2), '->', sorted(A2-A1))
