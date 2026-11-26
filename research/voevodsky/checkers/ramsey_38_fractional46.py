"""Verify a rational primal cover for the unique unresolved 46-edge core. Enumerate all blue five/six cliques for verification, not just tight demands."""
import json,math
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from ramsey_38_layer46_fresh import P,E
rows=[json.loads(s) for f in P.glob('ramsey_38_degree4_weights46_*.jsonl') for s in f.read_text().splitlines()];r,=[z for z in rows if z['num']<=7*z['den']];h=r['core'];a=[0]*20
for k,(i,j) in enumerate(E):
 if int(h,16)>>k&1:a[i]|=1<<j;a[j]|=1<<i
I=[0]
for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];Q=[q for q in I if q.bit_count() in (5,6)];A=np.array([[int(bool(s&q)) for s in S] for q in Q]);d=[q.bit_count() for q in Q];lp=linprog(np.ones(len(S)),A_ub=-A,b_ub=-np.array(d));assert lp.success;x=[Fraction(float(v)).limit_denominator(100000) for v in lp.x];assert min(x)>=0 and sum(x)<=7 and all(sum(w for s,w in zip(S,x) if s&q)>=q.bit_count() for q in Q);print(h,sum(x),len(Q));(P/'ramsey_38_fractional46.json').write_text(json.dumps(dict(core=h,total=str(sum(x)),weights={s:str(w) for s,w in zip(S,x) if w},demands=len(Q)))+'\n')
