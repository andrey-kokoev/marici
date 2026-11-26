"""Exact two-vertex test for the fixed 31-vertex coloring. Both new vertices must fail both individual sides. Relabeling old vertices is not required."""
import json
from itertools import combinations
from pysat.solvers import Solver
from ramsey_retention_slice import D
P=D.parent;a=json.loads((P/'ramsey_four_witness_square.json').read_text())['red_masks'];cs=[];aux=63
for sign,side in [(1,range(24)),(-1,list(range(17))+list(range(24,31)))]:
 g=a if sign==1 else [~v for v in a];cl=lambda t:all(g[i]>>j&1 for i,j in combinations(t,2));
 for t in combinations(range(31),3):
  if cl(t):cs.append([-sign*63]+[-sign*(i+1+off) for off in (0,31) for i in t])
 for off in (0,31):
  for t in combinations(range(31),4):
   if cl(t):cs.append([-sign*(off+i+1) for i in t])
  opts=[]
  for t in combinations(side,3):
   if cl(t):aux+=1;opts.append(aux);cs.extend([[-aux,sign*(off+i+1)] for i in t])
  cs.append(opts)
with Solver(name='g4',bootstrap_with=cs) as s:
 ok=s.solve();print(ok);out=dict(sat=ok,clauses=len(cs));
 if ok:out['positive_edge_variables']=[i for i in s.get_model() if 0<i<=63]
 (P/'ramsey_joint_gain_pair.json').write_text(json.dumps(out)+'\n')
