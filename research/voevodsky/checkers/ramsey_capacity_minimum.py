"""Minimum obstruction search as hitting set over surviving four-support assignments. Bounded CP-SAT; only report certified solver bounds. Keep existing upper bound on timeout."""
import json,itertools,math
from pathlib import Path
import numpy as np
from ortools.sat.python import cp_model
P=Path(__file__).resolve().parents[1]/'results';z=json.loads((P/'ramsey_capacity_obstruction.json').read_text());S=z['supports'];Q=[q for q in range(4096) if q.bit_count()>=2 and any(q&s==q for s in S)];M=np.array(list(itertools.combinations_with_replacement(range(len(S)),4)));bad=np.column_stack([(np.array([bool(q&s) for s in S])[M].sum(axis=1)<q.bit_count()-1) for q in Q]);masks=sorted({int.from_bytes(row.tobytes(),'little') for row in np.packbits(bad,axis=1,bitorder='little')},key=int.bit_count);minimal=[]
for row in masks:
 if not any(m&row==m for m in minimal):minimal.append(row)
model=cp_model.CpModel();x=[model.new_bool_var(str(q)) for q in Q];
for row in minimal:model.add_bool_or([x[i] for i in range(len(Q)) if row>>i&1]);
model.minimize(sum(x));
for q,v in zip(Q,x):model.add_hint(v,int(q in z['demands']))
s=cp_model.CpSolver();s.parameters.num_search_workers=8;s.parameters.max_time_in_seconds=40;status=s.solve(model);best=z['demands'];
if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):best=[q for q,v in zip(Q,x) if s.value(v)]
assert bad[:,[Q.index(q) for q in best]].any(axis=1).all();out=dict(lower=math.ceil(s.best_objective_bound-1e-7),upper=len(best),demands=best,n_demands=len(Q),distinct_rows=len(masks),minimal_rows=len(minimal),status=s.status_name(status));packing=cp_model.CpModel();y=[packing.new_bool_var(str(i)) for i in range(len(minimal))];
for i in range(len(Q)):packing.add_at_most_one([v for m,v in zip(minimal,y) if m>>i&1]);
packing.maximize(sum(y));ps=cp_model.CpSolver();ps.parameters.max_time_in_seconds=10;ps.parameters.num_search_workers=4;st=ps.solve(packing)
if st in (cp_model.OPTIMAL,cp_model.FEASIBLE):
 chosen=[m for m,v in zip(minimal,y) if ps.value(v)];out['packing']=[[Q[i] for i in range(len(Q)) if m>>i&1] for m in chosen];print('disjoint groups',len(chosen))
print({k:v for k,v in out.items() if k!='packing'});(P/'ramsey_capacity_minimum.json').write_text(json.dumps(out,indent=1)+'\n')
