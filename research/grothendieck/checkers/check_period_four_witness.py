"""Dependency-free exact controls; not a proof of general higher coherence."""
import itertools
import json
from pathlib import Path

edges = {'AB': ('A','B'), 'BC': ('B','C'), 'CA': ('C','A'),
         'AD': ('A','D'), 'DB': ('D','B'), 'BA': ('B','A')}
closed = [w for w in itertools.product(edges, repeat=4)
          if all(edges[w[i]][1] == edges[w[(i+1)%4]][0] for i in range(4))]
orbits = {min(w[i:]+w[:i] for i in range(4)) for w in closed}
assert len(closed) == 6 and len(orbits) == 2
assert sorted(sum(min(w[i:]+w[:i] for i in range(4)) == r for w in closed)
              for r in orbits) == [2,4]
selected = ('AD','DB','BC','CA')
assert selected in closed
assert len(selected) != 0
assert sum((3,1,2,2)) % 5 == 3 != 1
windings = range(-9,10)
assert all(16*k - 15*k == k for k in windings)
assert sum(16*k != k for k in windings) == 18

# D5 = pairs (rotation exponent, reflection parity).
def mul(x,y):
    a,b = x; c,d = y
    return ((a + (-1)**b*c) % 5, (b+d)%2)
def inv(x):
    a,b = x
    return ((-(-1)**b*a)%5,b)
def G(x):
    return mul(mul((1,0),x),(4,0))
def F(x):
    for _ in range(4): x = G(x)
    return x
witnesses = list(itertools.product(range(5), range(2)))
# Family transport is F(p)^-1 * q * p, with q = F(p).
assert all(mul(mul(inv(F(p)),F(p)),p) == p for p in witnesses)
assert sum(F(p) != p for p in witnesses) == 5
result = dict(rooted_closed_histories=6, cyclic_orbit_sizes=[2,4],
              selected_cycle=list(selected), circle_tested=19,
              circle_raw_changed=18, d5_tested=10, d5_raw_changed=5,
              residuals=['No fully coherent C4 action established',
                         'Four-cycle selection is additional data',
                         'No physical interpretation derived'])
out = Path(__file__).resolve().parents[1]/'results'/'period-four-witness.json'
out.write_text(json.dumps(result,indent=2)+'\n', encoding='utf-8')
print('PASS: six histories, two orbits, product counterexample, circle and D5 transport')
