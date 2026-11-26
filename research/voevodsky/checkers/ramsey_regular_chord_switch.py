"""Local chord nonimplication under the derived order-23 degree-six condition AND red triangle avoidance. Both graphs share marked header spokes and six-port rim; outside edges may compensate. Not a global change of Ramsey verdict."""
import itertools,json
from pysat.solvers import Solver
from pysat.card import CardEnc
from pysat.formula import IDPool
from ramsey_retention_slice import D,has
n=23;p=2**n-1;pool=IDPool();pairs=list(itertools.combinations(range(n),2));v={e:pool.id(e) for e in pairs};var=lambda i,j:v[tuple(sorted((i,j)))];cs=[]
for i in range(n):cs+=CardEnc.equals([var(i,j) for j in range(n) if j!=i],6,vpool=pool).clauses
for i,j,k in itertools.combinations(range(n),3):cs.append([-var(i,j),-var(i,k),-var(j,k)])
for i,j in itertools.combinations(range(7),2):cs.append([-var(i,j)])
# Replace red 1-7,3-8 by 1-3,7-8. Forbid all triangles in switched graph too. Pin the absent/present edges.
flip={(1,7),(3,8),(1,3),(7,8)}
for e in flip:cs.append([v[e] if e in {(1,7),(3,8)} else -v[e]])
for t in itertools.combinations(range(n),3):
 E=list(itertools.combinations(t,2))
 if any(e in flip for e in E):cs.append([v[e] if e in flip else -v[e] for e in E])
with Solver(name='g4',bootstrap_with=cs) as sl:
 assert sl.solve();m=set(sl.get_model());a=[0]*n
 for (i,j),w in v.items():
  if w in m:a[i]|=1<<j;a[j]|=1<<i
b=a.copy()
for i,j in flip:b[i]^=1<<j;b[j]^=1<<i
for g in (a,b):assert all(x.bit_count()==6 for x in g) and not has(g,p,3)
assert not has(a,127,2) and sum((x&127).bit_count() for x in b[:7])==2
out=dict(before=a,after=b,marked=list(range(7)),red_removed=[[1,7],[3,8]],red_added=[[1,3],[7,8]],global_blue7=[has([~x for x in g],p,7) for g in (a,b)]);print(out['global_blue7']);(D.parent/'ramsey_regular_chord_switch.json').write_text(json.dumps(out,indent=1)+'\n')
