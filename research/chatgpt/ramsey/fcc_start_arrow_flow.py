"""Symmetry-equivariant, start-anchored cuboctahedral directed-arrow tours.

An initial dart (directed arrow) and R/B preference select one of the
rotational copies of a 5-vertex seam template. The initial dart is kept
as persistent reference during the route (not a choice at each step).
Both preferences then traverse all 48 darts once and return.
This is a constructed, start-dependent family, not two fixed fields.
"""
from itertools import product, permutations
from math import atan2
V=sorted(v for v in product((-1,0,1),repeat=3) if v.count(0)==1)
vi={v:i for i,v in enumerate(V)}
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
N={i:[j for j in range(12) if dot(sub(V[i],V[j]),sub(V[i],V[j]))==2] for i in range(12)}
ORDER={}
for i in range(12):
 n=V[i];z=(0,0,1)
 x=tuple(2*a-dot(z,n)*b for a,b in zip(z,n));y=cross(n,x)
 ORDER[i]=sorted(N[i],key=lambda j:atan2(dot(sub(V[j],V[i]),y),dot(sub(V[j],V[i]),x)))
D=tuple((i,j) for i in range(12) for j in N[i])
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
G=[]
for p in permutations(range(3)):
 for s in product((-1,1),repeat=3):
  if sign(p)*s[0]*s[1]*s[2]==1:
   G.append(tuple(vi[tuple(s[k]*v[p[k]] for k in range(3))] for v in V))
assert len(G)==24

def turn(d,pref,seams):
 i,j=d;ports=ORDER[j];k=ports.index(i)
 offset=2 if j in seams else (1 if pref=='R' else -1)
 return (j,ports[(k+offset)%4])

def orbit(d,pref,seams):
 seen=set();cur=d
 while cur not in seen:
  seen.add(cur);cur=turn(cur,pref,seams)
 assert cur==d
 return seen

# All 5-vertex sets enabling a single R 48-dart cycle.
sol=[]
for mask in range(1<<12):
 S=frozenset(i for i in range(12) if mask>>i&1)
 if len(S)==5 and len(orbit(D[0],'R',S))==48:sol.append(S)
assert len(sol)==24
S0=sol[0]
ref_edge=tuple(sorted(D[0]))
EDGE_TO_SEAM={}
for g in G:
 edge=tuple(sorted(g[i] for i in ref_edge))
 assert edge not in EDGE_TO_SEAM  # rotational stabilizer of an edge is trivial
 EDGE_TO_SEAM[edge]=frozenset(g[i] for i in S0)
assert len(EDGE_TO_SEAM)==24 and len(set(EDGE_TO_SEAM.values()))==24

for start in D:
 S=EDGE_TO_SEAM[tuple(sorted(start))]
 for pref in 'RB':
  got=orbit(start,pref,S)
  assert len(got)==48 and got==set(D)
for g in G:
 for start in D:
  a,b=(g[start[0]],g[start[1]])
  s=EDGE_TO_SEAM[tuple(sorted(start))]
  rs=EDGE_TO_SEAM[tuple(sorted((a,b)))]
  assert rs==frozenset(g[i] for i in s)
  for pref in 'RB':
   next_d=turn(start,pref,s)
   assert (g[next_d[0]],g[next_d[1]])==turn((a,b),pref,rs)
print('Five-vertex solutions:',len(sol))
print('Rotations:',len(G))
print('Distinct start-undirected-edge references:',len(EDGE_TO_SEAM))
print('Directed starts tested:',len(D))
print('Preferences per start: 2; all return after 48 moves with full arrow coverage')
print('Start reference example:',tuple(V[i] for i in ref_edge))
print('Reference five vertices:',[V[i] for i in sorted(S0)])
