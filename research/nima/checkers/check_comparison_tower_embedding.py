"""Exact embedding of six comparison coordinates into a seven-probe span.

Shared reference f0 and six contrasts b_i=f_i-f0 in fixed G12=10I+J.
Induced metric M=10(I6+J6). This is an explicit bridge choice, not a unique
identification of the two carriers or of the tower witness order.
"""
from fractions import Fraction as F
from itertools import product

N = 6
M = [[F(10*((i == j)+1)) for j in range(N)] for i in range(N)]
Mi = [[F(i == j, 10)-F(1, 70) for j in range(N)] for i in range(N)]

def dot(x, y): return sum(a*b for a,b in zip(x,y))
def mv(A,x): return [dot(row,x) for row in A]
def energy(x): return dot(x,mv(M,x))
assert all(sum(M[i][k]*Mi[k][j] for k in range(N)) == (i == j)
           for i in range(N) for j in range(N))

def state(side,i):
    x = [F(0)]*N
    if i: x[3*side+i-1] = F(1)
    return x

def sub(a,b): return [x-y for x,y in zip(a,b)]
def arrow(side,e): return sub(state(side,e[1]),state(side,e[0]))
edges = [(i,j) for i in range(4) for j in range(4) if i != j]
rows = [sub(arrow(0,e),arrow(1,f)) for e,f in product(edges,repeat=2)]
rows += [sub(state(0,i),state(1,j)) for i,j in product(range(1,4),repeat=2)]
assert len(rows) == 153

# Coefficients q map to ambient coefficients (-sum(q),q1,...,q6,0,...).
def ambient(q): return [-sum(q)]+q+[F(0)]*5
def ambient_inner(a,b): return 10*dot(a,b)+sum(a)*sum(b)
seed = list(map(F,[1,-2,3,0,1,-1]))
assert ambient_inner(ambient(seed),ambient(seed)) == energy(seed)

changed = 0
for r in rows:
    d = mv(Mi,r)
    n = dot(r,d)
    a = dot(r,seed)/n
    projected = [x-v*a for x,v in zip(seed,d)]
    assert dot(r,projected) == 0
    assert energy(seed) == energy(projected)+dot(r,seed)**2/n
    euclidean = [x-v*dot(r,seed)/dot(r,r) for x,v in zip(seed,r)]
    changed += projected != euclidean
    # Metric-aware record exchange, with arbitrary populated record z.
    z = F(2,3)
    out = [x+v*(z-a) for x,v in zip(seed,d)]
    record = a
    assert energy(out)+n*record**2 == energy(seed)+n*z**2
    reverse_a = dot(r,out)/n
    restored = [x+v*(record-reverse_a) for x,v in zip(out,d)]
    assert restored == seed and reverse_a == z
assert changed > 0
# A final comparison span with six independent directions cannot fit in V4.
assert len(seed) == 6 > 4
print('Six contrast coordinates embed into V7 inside V12: induced metric 10(I+J).')
print(f'For the test seed, {changed}/153 metric projections differ from Euclidean ones.')
print('All 153 metric projections and populated-record exchanges conserve the induced budget exactly.')
print('The six-dimensional comparison space cannot embed injectively into V4.')
print('Earlier Euclidean dynamic spectra must be recomputed for this bridge.')
