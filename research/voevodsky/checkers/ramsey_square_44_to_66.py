"""Test direct 4,4 -> 6,6 joins using enlarged sides from the saved 17/24/31 square. Also test all nine induced subgraphs for a nested certificate."""
import json,itertools
from pysat.solvers import Solver
from ramsey_retention_slice import D,check,has
P=D.parent;a=json.loads((P/'ramsey_four_witness_square.json').read_text())['red_masks']+[0]*6
# 31..33: red triangle, blue to old graph. 34..36: blue triangle, red to old graph.
for i,j in itertools.combinations(range(37),2):
 if (31<=i<j<34) or (i<31 and j>=34):a[i]|=1<<j;a[j]|=1<<i
S=list(range(17));L=list(range(17,24))+list(range(31,34));R=list(range(24,31))+list(range(34,37));mask=lambda v:sum(1<<i for i in v)
for x,y in itertools.product(range(3),repeat=2):assert check(a,mask(S+L[:[0,7,10][x]]+R[:[0,7,10][y]]),4+y,4+x)
cs=[]
for red in [False,True]:
 g=a if red else [~v for v in a];groups=[]
 for side in (L,R):
  parts=[]
  for k in range(1,6):
   for t in itertools.combinations(range(10),k):
    if all(g[side[i]]>>side[j]&1 for i,j in itertools.combinations(t,2)):
     h=mask(S)
     for i in t:h&=g[side[i]]
     parts.append((t,h))
  groups.append(parts)
 for (u,h),(v,b) in itertools.product(*groups):
  k=6-len(u)-len(v)
  if k>=0 and has(g,h&b,k):cs.append([(-1 if red else 1)*(10*i+j+1) for i in u for j in v])
with Solver(name='g4',bootstrap_with=cs) as sl:
 assert sl.solve();forced=[v for v in range(1,101) if not all(sl.solve(assumptions=[s*v]) for s in [-1,1])]
out=dict(red_masks=a,left=L,right=R,clauses=len(cs),shortest_clause=min(map(len,cs)),forced=forced);print({k:v for k,v in out.items() if k not in ['red_masks','left','right']});(P/'ramsey_square_44_to_66.json').write_text(json.dumps(out)+'\n')
