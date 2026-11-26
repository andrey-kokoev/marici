"""Separate weighted counting obstructions from integer-only obstructions. Verify rational primal and dual certificates, both for the saved minimum demand set and for the full set."""
from pathlib import Path
import json,numpy as np
from fractions import Fraction as F
from scipy.optimize import linprog
P=Path(__file__).resolve().parents[1]/'results';cores=json.loads((P/'ramsey_core_capacity_36.json').read_text());mins=json.loads((P/'ramsey_capacity_fixed_degree.json').read_text());out=[]
for z in mins:
 i=z['core_index'];a=cores[i]['core'];allq=[t for t in range(1,4096) if not any(t>>j&1 and t&v for j,v in enumerate(a))];S=[t for t in allq if not any(u!=t and t&u==t for u in allq)];row=dict(index=i,minimum=z['upper']);out.append(row)
 for name,Q in [('certificate',z['demands']),('all',allq)]:
  A=[[int(bool(t&u)) for u in S] for t in Q];r=[q.bit_count() for q in Q];lp=linprog([1]*len(S),A_ub=-np.array(A),b_ub=-np.array(r),method='highs');assert lp.success;x=[F(float(v)).limit_denominator(10**7) for v in lp.x];y=[F(float(-v)).limit_denominator(10**7) for v in lp.ineqlin.marginals];assert min(x+y)>=0 and all(sum(b*v for b,v in zip(line,x))>=req for line,req in zip(A,r)) and all(sum(b*v for b,v in zip(line,y))<=1 for line in zip(*A));val=sum(x);assert val==sum(w*b for w,b in zip(y,r));row[name]=dict(mass=str(val),primal={k:str(v) for k,v in zip(S,x) if v},dual={k:str(v) for k,v in zip(Q,y) if v},unweighted_hits=sum(r),max_per_support=max(map(sum,zip(*A))));
 print(i,row['minimum'],[(row[n]['mass'],row[n]['unweighted_hits'],row[n]['max_per_support']) for n in ('certificate','all')])
(P/'ramsey_capacity_counting_test.json').write_text(json.dumps(out,indent=1)+'\n')
