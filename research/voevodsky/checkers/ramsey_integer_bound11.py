"""Classify failures not excluded by the weighted blue-four test. Check whole maximal support multisets with repeats, separate demand sizes. Record one conflict witness for every near-solution on row 69."""
import json,itertools
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';refs=json.loads((P/'ramsey_support_bound11.json').read_text());data=[r for r in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if r['n']==11 and r['d']==4];out=[]
for ref in refs:
 if ref['actual'] or ref['num'] is not None and ref['num']<4*ref['den']:continue
 i=ref['row'];a=data[i]['core'];I=[0]
 for j,v in enumerate(a):I.extend([s|1<<j for s in I if not s&v])
 S=[s for s in I if all(s&(v|1<<j) for j,v in enumerate(a))];Q={k:[q for q in I if q.bit_count()==k] for k in (2,3,4)};miss={k:[sum(1<<j for j,q in enumerate(qs) if not s&q) for s in S] for k,qs in Q.items()};counts=[0,0,0];w=[];three_example=None
 for z in itertools.combinations_with_replacement(range(len(S)),3):
  if all(not(miss[4][u]&miss[4][v]) for u,v in itertools.combinations(z,2)):three_example=[S[u] for u in z];break
 for z in itertools.combinations_with_replacement(range(len(S)),4):
  if any(miss[4][u]&miss[4][v] for u,v in itertools.combinations(z,2)):continue
  counts[0]+=1
  for k in (3,2):
   bad=[q for q in Q[k] if sum(bool(q&S[j]) for j in z)<k-1]
   if bad:
    if i==69:w.append(dict(rows=[S[j] for j in z],failed=bad))
    break
   counts[4-k]+=1
 assert counts[-1]==0
 B=np.array([[int(not q&s) for s in S] for q in Q[4]]);lp=linprog(np.zeros(len(S)),A_ub=B,b_ub=np.ones(len(B)),A_eq=[np.ones(len(S))],b_eq=[4]);assert lp.success;x=[Fraction(float(t)).limit_denominator(100000) for t in lp.x];assert min(x)>=0 and sum(x)==4 and all(sum(t for t,s in zip(x,S) if not q&s)<=1 for q in Q[4]);out.append(dict(row=i,counts=counts,compatible_three=three_example,fractional={s:str(t) for s,t in zip(S,x) if t},conflicts=w));print(i,counts)
(P/'ramsey_integer_bound11.json').write_text(json.dumps(out)+'\n')
