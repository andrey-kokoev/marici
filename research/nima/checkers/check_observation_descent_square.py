"""Exact observation/descent square for the fixed stabilizer-probe tower.

H_r has G_r=10I+J. A potential is a probe-difference readout
q_i=<f_i-f0,psi>=10(c_i-c0). Initially observe i=1..6.
Descent removes the last probe by Gram-orthogonal projection.
"""
from fractions import Fraction as F
from itertools import product


def observe(c, labels):
    return [10*(c[i]-c[0]) for i in labels]


def restrict(c):
    r = len(c)
    return [x+c[-1]/(r+9) for x in c[:-1]]


def state(side, i):
    x = [F(0)]*6
    if i:
        x[3*side+i-1] = F(1)
    return x


def sub(a,b): return [x-y for x,y in zip(a,b)]
def arrow(side,e): return sub(state(side,e[1]),state(side,e[0]))
edges = [(i,j) for i in range(4) for j in range(4) if i != j]
rows = [sub(arrow(0,e),arrow(1,f)) for e,f in product(edges,repeat=2)]
rows += [sub(state(0,i),state(1,j)) for i,j in product(range(1,4),repeat=2)]

print('source->target | surviving readouts | descending comparison slots')
for r in range(12,4,-1):
    source_labels = list(range(1,min(6,r-1)+1))
    target_labels = list(range(1,min(6,r-2)+1))
    for j in range(r):
        c = [F(i == j) for i in range(r)]
        assert observe(restrict(c),target_labels) == observe(c,source_labels)[:len(target_labels)]
    count = sum(all(x == 0 for x in row[len(target_labels):]) for row in rows)
    print(f'{r}->{r-1} | {len(target_labels)} | {count}/153')

# At 7->6, q6 is unobservable on the target. Of the original slots,
# precisely those with coefficient of q6 zero factor through deletion.
assert sum(row[-1] == 0 for row in rows) == 78
assert sum(all(x == 0 for x in row[3:]) for row in rows) == 0
# Preserve q6 as an explicit observation record; then every functional is
# reconstructible from (q1,...,q5, record=q6).
q = list(map(F,[1,2,3,4,5,6]))
kept, record = q[:5], q[5]
for row in rows:
    assert sum(a*b for a,b in zip(row,q)) == sum(a*b for a,b in zip(row[:5],kept))+row[5]*record

# Readout metric is inverse contrast Gram. Both are principal-form families.
def readout_metric(n):
    return [[F(i == j,10)-F(1,10*(n+1)) for j in range(n)] for i in range(n)]
def quadratic(A,x):
    return sum(x[i]*A[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))
# The inherited low-readout norm is the minimum high-readout norm over q6.
low = q[:5]
optimal = sum(low)/6
assert quadratic(readout_metric(6),low+[optimal]) == quadratic(readout_metric(5),low)
assert quadratic(readout_metric(6),q) == quadratic(readout_metric(5),low)+F(3,35)*(record-optimal)**2

# Metric-correct comparison updates need not commute with dropping q6.
# In readout coordinates inverse metric is M=10(I+J).
def update(q,row):
    n=len(q)
    direction=[10*(row[i]+sum(row)) for i in range(n)]
    denom=sum(a*b for a,b in zip(row,direction))
    a=sum(x*y for x,y in zip(row,q))/denom
    return [x-y*a for x,y in zip(q,direction)]
# For a descending row its support is within the target; the upper direction
# restricted to surviving coordinates equals the lower direction.
for row in rows:
    if row[-1] == 0:
        assert update(q,row)[:5] == update(q[:5],row[:5])
print('All adjacent observation squares commute exactly on carrier basis vectors.')
print('At 7->6: 78 slots descend, 75 require the removed readout record.')
print('All 78 surviving metric comparison projections commute with readout descent.')
print('Inverse-metric quotient budget and retained-plus-record split checked exactly.')
print('At rung4, no original cross-carrier slot survives for this deletion order without records.')
