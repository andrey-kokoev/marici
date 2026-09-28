"""Periodic covariance of a provisional comparison-back-action programme.

Six potential coordinates, 153 comparison rows, 12 sweeps per programme.
Each step projects onto its equality then adds independent zero-mean noise
inside that equality plane. Covariance injection = strength*P/5, so expected
injected squared norm per step is strength. Euclidean metric and isotropic
noise are explicit trial choices. No measured constants or files used.
"""
from itertools import product

N=6
edges=[(i,j) for i in range(4) for j in range(4) if i!=j]
def state(side,i):
    x=[0.]*N
    if i: x[3*side+i-1]=1.
    return x

def sub(a,b): return [x-y for x,y in zip(a,b)]
def arrow(side,e): return sub(state(side,e[1]),state(side,e[0]))
rows=[sub(arrow(0,e),arrow(1,f)) for e,f in product(edges,repeat=2)]
rows += [sub(state(0,i),state(1,j)) for i,j in product(range(1,4),repeat=2)]
assert len(rows)==153

def zero(): return [[0.]*N for _ in range(N)]
def trace(a): return sum(a[i][i] for i in range(N))
def step(c,r,strength):
    norm=sum(v*v for v in r)
    cr=[sum(c[i][j]*r[j] for j in range(N)) for i in range(N)]
    rcr=sum(r[i]*cr[i] for i in range(N))
    out=[[c[i][j]-(r[i]*cr[j]+cr[i]*r[j])/norm
          +r[i]*r[j]*rcr/norm**2
          +strength*((i==j)-r[i]*r[j]/norm)/(N-1)
          for j in range(N)] for i in range(N)]
    # Current comparison remains satisfied after tangent-plane back-action.
    assert max(abs(sum(out[i][j]*r[j] for j in range(N))) for i in range(N))<1e-9
    assert abs(trace(out)-(trace(c)-rcr/norm+strength))<1e-9
    return out,rcr/norm

def sweep(c,strength):
    removed=0.
    for r in rows:
        c,drop=step(c,r,strength)
        removed+=drop
    return c,removed

c=zero()
for iteration in range(1,1001):
    nxt,removed=sweep(c,1.)
    difference=max(abs(nxt[i][j]-c[i][j]) for i in range(N) for j in range(N))
    c=nxt
    if difference<1e-12: break
else: raise AssertionError('periodic covariance did not converge')
assert abs(removed-153)<1e-8
# Direct check that covariance response scales with injection strength.
half,drop=sweep([[v/2 for v in row] for row in c],.5)
assert max(abs(half[i][j]-c[i][j]/2) for i in range(N) for j in range(N))<1e-11
quiet,drop0=sweep(zero(),0.)
assert trace(quiet)==drop0==0
residual=sum(sum(r[i]*c[i][j]*r[j] for i in range(N) for j in range(N)) for r in rows)
print(f'Periodic covariance converged after {iteration} sweeps.')
print(f'Unit injection: end-sweep state variance={trace(c):.12f}')
print(f'Unit injection: sum of comparison variances={residual:.12f}')
print(f'Settling removes {removed:.12f} squared-resource units per153-slot sweep.')
print('12 sweeps: injected and removed budgets=1836*strength each at stationarity.')
print('Every attempt separately retains its unit traversal cost.')
print('Noise strength0 -> floor0; halving strength halves covariance and settling budget.')
print('Back-action and balance tests passed within stated floating tolerances.')
