"""Greedy global certificate, followed by deletion filtering. Inclusion-minimal is not minimum. Each family is known to have transversal number 2."""
import json
from pathlib import Path
from itertools import combinations
from pysat.solvers import Solver
from pysat.card import CardEnc
P=Path(__file__).resolve().parents[1]/'results';rows=json.loads((P/'ramsey_square_edge_families.json').read_text());F=[set(r[3]) for r in rows];Q=set.union(*F);n=35;cl={q:[i+1 for i in range(n) if q>>i&1] for q in Q};enc={k:CardEnc.atmost(list(range(1,n+1)),k).clauses for k in range(1,10)}
def cover(qs,k):
 with Solver(name='g4',bootstrap_with=[cl[q] for q in qs]+enc[k]) as s:
  if s.solve():return [i-1 for i in s.get_model() if 1<=i<=n]
 return None
def tau(qs):return next(k for k in range(1,10) if cover(qs,k) is not None)
def run(role):
 opts=[i for i,r in enumerate(rows) if r[0]==role];chosen=[];q=set();seq=[]
 while (t:=tau(q) if q else 0)<9:
  i=max(opts,key=lambda i:len(F[i]-q));chosen.append(i);q|=F[i];seq.append([rows[i][:3],len(q),tau(q)])
 for i in chosen.copy():
  trial=set().union(*(F[j] for j in chosen if j!=i))
  if cover(trial,8) is None:chosen.remove(i)
 out=dict(sequence=seq,certificate=[rows[i][:3] for i in chosen],cliques=len(set.union(*(F[i] for i in chosen))),removal_cuts=[cover(set().union(*(F[j] for j in chosen if j!=i)),8) for i in chosen]);print(role,len(chosen),out['cliques'],seq,flush=True);return out
result={r:run(r) for r in ('pole','equator')};(P/'ramsey_square_family_union.json').write_text(json.dumps(result,indent=1)+'\n')
