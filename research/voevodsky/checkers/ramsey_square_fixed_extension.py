"""Exactly decide if one more vertex fits each saved 36-vertex graph without recoloring."""
import json
from itertools import combinations
from pysat.solvers import Solver
from ramsey_retention_slice import D,check
P=D.parent;rows=[]
for src in sorted(P.glob('ramsey_four_square_endpoint_36_*.json')):
 a=json.loads(src.read_text())['red_masks'];clauses=[]
 for q in combinations(range(36),4):
  c={a[i]>>j&1 for i,j in combinations(q,2)}
  if len(c)==1:clauses.append([(-1 if 1 in c else 1)*(i+1) for i in q])
 with Solver(name='g4',bootstrap_with=clauses) as s:
  ok=s.solve();r=dict(source=src.name,sat=ok,clauses=len(clauses))
  if ok:r['new_red_neighbors']=[x-1 for x in s.get_model() if x>0]
 rows.append(r)
print(rows);(P/'ramsey_square_fixed_extension.json').write_text(json.dumps(rows,indent=1)+'\n')
