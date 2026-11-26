"""Which constraints already exclude each remaining 33-edge core? Compare exact rational LP dual tests with unrestricted integer decisions. eta is minimum uniform slack for the blue-clique demands with exact regular margins."""
import itertools,json,collections
from fractions import Fraction as F
from scipy.optimize import linprog
import numpy as np
from ramsey_retention_slice import D
P=D.parent;rows=json.loads((P/'ramsey_37_edge_average.json').read_text())['remaining'];out=[]
for row in rows:
 g=row['core'];Q=[sum(1<<i for i in u) for k in range(1,6) for u in itertools.combinations(range(16),k) if all(not(g[i]>>j&1) for i,j in itertools.combinations(u,2))];S=[q for q in Q if q.bit_count()==5];B=np.array([[1]*len(S)]+[[int(s>>i&1) for s in S] for i in range(16)]);b=[6]+[6-v.bit_count() for v in g];A=np.array([[int(bool(q&s)) for s in S] for q in Q]);d=np.array([q.bit_count() for q in Q]);
 # Test a simpler obstruction: maximize the mass of five-vertex supports, subject only to at most one missed support per blue five-clique.
 J=1-A[d==5];simple=linprog([-1]*len(S),A_ub=J,b_ub=np.ones(len(S)));ub=None
 if simple.success:
  w=[F(float(-v)).limit_denominator(10**6) for v in simple.ineqlin.marginals];assert all(v>=0 for v in w) and all(sum(w[i] for i,h0 in enumerate(col) if h0)>=1 for col in J.T);ub=sum(w)
 # Uniform slack on every inequality, including both signs of equalities. Positive exact dual proves infeasibility even for fractions.
 U=np.vstack((B,-B,-A));h=np.array(b+[-x for x in b]+list(-d));lp=linprog([0]*len(S)+[1],A_ub=np.column_stack((U,-np.ones(len(h)))),b_ub=h);assert lp.success;y=[F(float(-w)).limit_denominator(10**6) for w in lp.ineqlin.marginals];val=-sum(w*int(v) for w,v in zip(y,h));idx=[i for i,w in enumerate(y) if w];assert all(w>=0 for w in y) and sum(y)<=1 and all(sum(y[i]*int(U[i,j]) for i in idx)>=0 for j in range(len(S)));x=[F(float(w)).limit_denominator(10**6) for w in lp.x[:-1]];assert all(w>=0 for w in x) and all(sum(x[j]*int(l) for j,l in enumerate(line) if l)<=int(t)+val for line,t in zip(U,h));out.append(dict(fives_only_upper=str(ub),fives_dual={s:str(v) for s,v in zip(S,w) if v} if ub is not None else None,slack=str(val),dual={i:str(y[i]) for i in idx},primal={s:str(w) for s,w in zip(S,x) if w},degree_hist=dict(collections.Counter(v.bit_count() for v in g))))
print(collections.Counter('fractional feasible' if r['slack']=='0' else 'fractional impossible' for r in out));print(collections.Counter(r['slack'] for r in out));(P/'ramsey_37_core_obstructions.json').write_text(json.dumps(out,indent=1)+'\n')
