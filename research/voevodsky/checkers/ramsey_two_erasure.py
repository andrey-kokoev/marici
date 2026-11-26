"""Hide each pair of marked cross-edges while the other eight stay blue. Test the fixed minimum one-erasure panel and both complete tables. Store directly verified counterassignments and exact counts."""
import itertools,json
from pysat.solvers import Solver

def run(idx,E,V,cs,spec,inputs,P,source):
 p=next(z['panel'] for z in json.loads((P/'ramsey_minimum_panel.json').read_text()) if z['core']==idx);sel=[t for t in spec if spec[t] in p];assert len(sel)==len(p);out={}
 with Solver(name='g4',bootstrap_with=cs) as sl:
  for name,gs in [('minimum_one',sel),('full',list(spec))]:
   fail=[]
   for pair in itertools.combinations(E,2):
    # One-red alternatives excluded by the already verified one-erasure property, check again.
    for e in pair:assert not sl.solve(assumptions=gs+[V[e]]+[-V[f] for f in E if f!=e])
    if sl.solve(assumptions=gs+[V[e] for e in pair]+[-V[f] for f in E if f not in pair]):
     pos=set(sl.get_model());edges=[e for e,v in V.items() if v in pos];assert {e for e in E if e in edges}==set(pair)
     for gate in gs:
      side,i,j,k=spec[gate];assert sum((i,h) in edges and (j,h) in edges for h in range(6))==k if side=='C' else sum((h,i) in edges and (h,j) in edges for h in range(16))==k
     fail.append(dict(hidden=pair,red_edges=edges))
   out[name]=dict(recovered=45-len(fail),failed=fail)
 print(idx,[(k,r['recovered']) for k,r in out.items()],flush=True);return dict(core=idx,tests=out)
