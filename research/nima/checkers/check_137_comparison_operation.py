"""Exact comparison-weight tests in a fixed carrier Gram geometry.

Use four probes from G12=10I+J: G4=10I4+J4. Tensor features represent
arrow-pair and state-pair slots in one 16-dimensional space. This is an
explicit trial response model; no electromagnetic identification is assumed.
"""
from fractions import Fraction as F
from itertools import product


def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mv(A,x): return [dot(row,x) for row in A]
def tensor(x,y): return [a*b for a in x for b in y]
def sub(x,y): return [a-b for a,b in zip(x,y)]

basis = [[F(i==j) for i in range(4)] for j in range(4)]
G = [[F(10*(i==j)+1) for j in range(4)] for i in range(4)]
Gi = [[F(i==j,10)-F(1,140) for j in range(4)] for i in range(4)]
K = [[G[i//4][j//4]*G[i%4][j%4] for j in range(16)] for i in range(16)]
C = [[Gi[i//4][j//4]*Gi[i%4][j%4] for j in range(16)] for i in range(16)]
assert all(sum(K[i][k]*C[k][j] for k in range(16)) == (i==j)
           for i in range(16) for j in range(16))
edges = [(a,b) for a,b in product(range(4),repeat=2) if a!=b and (a,b)!=(0,1)]
arrows = [sub(basis[b],basis[a]) for a,b in edges]
features = [('arrow',tensor(a,b)) for a,b in product(arrows,repeat=2)]
features += [('state',tensor(a,b)) for a,b in product(basis,repeat=2)]
assert len(features) == 137
raw_total = F(0)
for kind,v in features:
    Kv = mv(K,v)
    norm = dot(v,Kv)
    assert norm == (400 if kind=='arrow' else 121)
    raw_total += norm
    # Metric-orthogonal removal Qx=v*(v^T K x)/(v^T K v).
    # Expected removed norm with second moment C is Kv^T C Kv/norm.
    removed = dot(Kv,mv(C,Kv))/norm
    assert removed == 1
    # Rescaling the same feature preserves this normalized projection.
    scale = F(3,2)
    v2 = [scale*x for x in v]
    Kv2 = mv(K,v2)
    assert dot(Kv2,mv(C,Kv2))/dot(v2,Kv2) == 1
    # After its first update, this comparison has zero residual on reuse.
    Qv = [x-dot(Kv,v)*y/norm for x,y in zip(v,v)]
    assert Qv == [0]*16
assert raw_total == 50336
assert F(121*400,raw_total) == F(3025,3146)
assert sum(K[i][j]*C[j][i] for i in range(16) for j in range(16)) == 16
# A coherent non-isotropic state distinguishes slot responses explicitly.
x = tensor(basis[0],basis[0])
responses = set()
for kind,v in features:
    Kv = mv(K,v)
    responses.add(dot(Kv,x)**2/dot(v,Kv))
assert len(responses) > 1
print('Raw slot norms: arrow400, state121; total50336.')
print(f'Raw normalized arrow-slot weight={F(400,raw_total)}; state-slot weight={F(121,raw_total)}.')
print('Normalized metric projections on fresh isotropic covariance K^-1: expected removal1 for every slot.')
print('One uniformly selected comparison therefore has uniform label probability1/137 if that schedule is chosen.')
print('Initial total expected budget16; repeated same projection has zero further removal.')
print('137 fresh/reset trials yield137 expected units; a closed sequential programme cannot spend that same initial budget137 times.')
print(f'Non-isotropic control has {len(responses)} distinct slot responses.')
