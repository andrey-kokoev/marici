"""Compare minimum local obstructions at k=6. Drop dominated failure lists; optimize exactly when the time budget permits."""
import itertools,json,math
from pathlib import Path
import numpy as np
from ortools.sat.python import cp_model
P=Path(__file__).resolve().parents[1]/'results';rows=json.loads((P/'ramsey_core_capacity_36.json').read_text());out=[]
for idx,d in [(0,3),(0,4),(1,5)]+[(i,5) for i in range(2,len(rows))]:
 a=rows[idx]['core'];n=len(a);I=[t for t in range(1<<n) if all(not(t>>i&1 and a[i]&t) for i in range(n))];S=[t for t in I if not any(u!=t and u&t==t for u in I)];Q=[t for t in I if d+t.bit_count()>5];M=np.array(list(itertools.combinations_with_replacement(range(len(S)),d)),dtype=np.uint8);F=np.column_stack([np.array([bool(u&q) for u in S])[M].sum(axis=1)<d+q.bit_count()-5 for q in Q]);masks=sorted({int.from_bytes(r.tobytes(),'little') for r in np.packbits(F,axis=1,bitorder='little')},key=int.bit_count);minimal=[]
 if masks[0]==0:print(idx,d,'feasible');continue
 model=cp_model.CpModel();x=[model.new_bool_var(str(q)) for q in Q];
 for r in masks:
  if any(v&r==v for v in minimal):continue
  minimal.append(r);model.add_bool_or([v for i,v in enumerate(x) if r>>i&1]);
 model.minimize(sum(x));solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=8;solver.parameters.num_search_workers=8;st=solver.solve(model);best=Q if st not in (cp_model.OPTIMAL,cp_model.FEASIBLE) else [q for q,v in zip(Q,x) if solver.value(v)];assert F[:,[Q.index(q) for q in best]].any(axis=1).all();r=dict(core_index=idx,n=n,d=d,lower=math.ceil(solver.best_objective_bound-1e-7),upper=len(best),demands=best,status=solver.status_name(st));out.append(r);print(idx,n,d,r['lower'],r['upper'],flush=True);(P/'ramsey_capacity_compare.json').write_text(json.dumps(out,indent=1)+'\n')
