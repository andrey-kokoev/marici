"""All demand-size ablations and exact signatures. For each false 34 witness find nearest full labeled solution (not restricted to maximal supports); check protection of each whole support or each core column separately."""
from pathlib import Path
from itertools import combinations,combinations_with_replacement
from collections import Counter
import json,numpy as np
from pysat.solvers import Solver
from pysat.card import CardEnc
P=Path(__file__).resolve().parents[1]/'results';src=json.loads((P/'ramsey_test_coincidence.json').read_text())['rows'];parents=json.loads((P/'ramsey_core_capacity_36.json').read_text());stats={s:[] for s in range(16)};reports=[];repairs=[]
for i,row in enumerate(src):
 t=row['vertices'];g0=parents[row['parent']]['core'];a=[sum(1<<j for j,y in enumerate(t) if g0[x]>>y&1) for x in t];I=[q for q in range(1,2048) if all(not(q>>j&1 and q&v) for j,v in enumerate(a))];S=[s for s in I if not any(s!=u and s&u==s for u in I)];M=np.array(list(combinations_with_replacement(range(len(S)),5)));mask=np.full(len(M),15,dtype=np.uint8);var=lambda j,h:1+11*j+h;cs=[[-var(j,h),-var(j,k)] for j in range(5) for h,k in combinations(range(11),2) if a[h]>>k&1]
 for q in I:
  k=q.bit_count();passed=np.array([bool(s&q) for s in S])[M].sum(axis=1)>=k;mask[~passed]&=15^(1<<(k-1));cs.extend([[var(j,h) for j in js for h in range(11) if q>>h&1] for js in combinations(range(5),6-k)])
 hist=np.bincount(mask,minlength=16);reports.append(dict(core=i,parent=row['parent'],vertices=t,exact_pass_mask_counts=hist.tolist()));
 for s in stats:stats[s].append(int(hist[[m for m in range(16) if m&s==s]].sum()))
 for name,v in row['reject'].items():assert (stats[sum(1<<(int(k)-1) for k in name)][-1]==0)==v
 for m in M[((mask&12)==12)&(mask!=15)]:
  old=[S[j] for j in m];p=[var(j,h)*(1 if s>>h&1 else -1) for j,s in enumerate(old) for h in range(11)];
  with Solver(name='g4',bootstrap_with=cs) as sl:
   keep_row=[j for j in range(5) if sl.solve(assumptions=p[11*j:11*j+11])];keep_col=[h for h in range(11) if sl.solve(assumptions=p[h::11])]
  for cost in range(1,56):
   with Solver(name='g4',bootstrap_with=cs+CardEnc.atmost([-u for u in p],cost,top_id=55).clauses) as sl:
    if sl.solve():pos=set(sl.get_model());break
  new=[sum(1<<h for h in range(11) if var(j,h) in pos) for j in range(5)];assert sum((s^u).bit_count() for s,u in zip(old,new))==cost and all(sum(bool(s&q) for s in new)>=q.bit_count() for q in I) and all(s in I+[0] for s in new);repairs.append(dict(core=i,old=old,new=new,min_edge_changes=cost,individually_preservable_rows=keep_row,individually_preservable_columns=keep_col))
def mins(opts):return [s for s in opts if not any(z!=s and z&s==z for z in opts)]
V=mins([s for s,v in stats.items() if [bool(n) for n in v]==[bool(n) for n in stats[15]]]);W=mins([s for s,v in stats.items() if v==stats[15]]);print(V,W,[(r['core'],r['min_edge_changes'],len(r['individually_preservable_rows']),len(r['individually_preservable_columns'])) for r in repairs]);print({s:(sum(n==0 for n in v),sum(v)) for s,v in stats.items()});(P/'ramsey_test_distillation.json').write_text(json.dumps(dict(size_bit_encoding='bit k-1 means demands of size k',minimal_verdict_masks=V,minimal_maximal_witness_masks=W,counts=stats,cases=reports,repairs=repairs),indent=1)+'\n')
