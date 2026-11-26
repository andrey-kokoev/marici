"""Exact finite oracle plus restricted hitting-set bounds; do not scan all pairs of failure lists for dominance."""
import json,itertools,math,time
from pathlib import Path
import numpy as np
from ortools.sat.python import cp_model
P=Path(__file__).resolve().parents[1]/'results';rows=json.loads((P/'ramsey_core_capacity_36.json').read_text());out=[]
for idx,z in enumerate(rows[1:],1):
 a=z['core'];Q=[t for t in range(1,4096) if all(not(t>>i&1 and t&a[i]) for i in range(12))];S=[t for t in Q if not any(t!=u and u&t==t for u in Q)];M=np.array(list(itertools.combinations_with_replacement(range(len(S)),5)),dtype=np.uint8);F=np.column_stack([np.array([int(bool(s&q)) for s in S],dtype=np.uint8)[M].sum(axis=1,dtype=np.uint8)<q.bit_count() for q in Q]);cols=[int.from_bytes(b.tobytes(),'little') for b in np.packbits(F.T,axis=1,bitorder='little')];full=(1<<len(M))-1;assert all(F.any(axis=1));best=list(range(len(Q)));rng=np.random.default_rng(37)
 for trial in range(18):
  left=full;pick=[]
  while left:
   v=max(rng.permutation(len(Q)),key=lambda j:(left&cols[j]).bit_count());pick.append(int(v));left&=~cols[v]
  if len(pick)<len(best):best=pick
 model=cp_model.CpModel();x=[model.new_bool_var(str(q)) for q in Q];model.minimize(sum(x));fkeys=np.packbits(F,axis=1,bitorder='little');pool=sorted({int.from_bytes(r.tobytes(),'little') for r in fkeys},key=int.bit_count);added=set();
 def add(r):
  if r not in added:model.add_bool_or([v for i,v in enumerate(x) if r>>i&1]);added.add(r)
 for r in pool[:1500]:add(r)
 lower=1;start=time.monotonic()
 while time.monotonic()-start<11 and lower<len(best):
  sol=cp_model.CpSolver();sol.parameters.max_time_in_seconds=2.5;sol.parameters.num_search_workers=8;st=sol.solve(model);lower=max(lower,math.ceil(sol.best_objective_bound-1e-7));
  if st not in (cp_model.OPTIMAL,cp_model.FEASIBLE):continue
  ids=[i for i,v in enumerate(x) if sol.value(v)];mask=sum(1<<i for i in ids);miss=[r for r in pool if not r&mask];
  if not miss:
   if len(ids)<len(best):best=ids
  else:
   for r in miss[:250]:add(r)
   for r in rng.choice(len(miss),min(200,len(miss)),replace=False):add(miss[r])
 assert F[:,best].any(axis=1).all() and lower<=len(best);out.append(dict(core_index=idx,lower=lower,upper=len(best),demands=[Q[i] for i in best],multisets=len(M)));print(idx,lower,len(best),flush=True);(P/'ramsey_capacity_fixed_degree.json').write_text(json.dumps(out,indent=1)+'\n')
