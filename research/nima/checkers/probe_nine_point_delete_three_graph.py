"""Numerical only: search the graph-realizable eight-label lift with column 3 deleted."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json
import numpy as np
import sympy as s
from scipy.optimize import minimize
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
frozen=json.loads((OUT/'nine-point-support-stress.json').read_text())['first_no_seven_support_target'];neg=frozen['negative_initial_columns'];w=list(map(Q,frozen['weights']));t=list(map(Q,frozen['slopes']))
x=[(-w[i] if i<neg else w[i]) for i in range(9)];y=[x[i]*t[i] for i in range(9)]
K=s.Matrix([[(-1)**(j-p)*__import__('math').comb(6,j-p) if 0<=j-p<=6 else 0 for j in range(9)] for p in range(3)])
deleted=2;pivot=next(p for p in reversed(range(3)) if K[p,deleted]);free=[p for p in range(3) if p!=pivot]
a,b,c,d=s.symbols('a b c d');A={free[0]:a,free[1]:b};B={free[0]:c,free[1]:d}
A[pivot]=(-x[deleted]-sum(A[p]*K[p,deleted] for p in free))/K[pivot,deleted]
B[pivot]=(-y[deleted]-sum(B[p]*K[p,deleted] for p in free))/K[pivot,deleted]
X=[x[j]+sum(A[p]*K[p,j] for p in range(3)) for j in range(9)];V=[y[j]+sum(B[p]*K[p,j] for p in range(3)) for j in range(9)]
expr=[s.expand(X[i]*V[j]-X[j]*V[i]) for i,j in combinations([i for i in range(9) if i!=deleted],2)]
fn=s.lambdify((a,b,c,d),expr,'numpy');constant=np.array([float(e.subs({a:0,b:0,c:0,d:0})) for e in expr]);scale=np.maximum(1,np.abs(constant))
def values(v):return np.asarray(fn(*v),dtype=float).reshape(-1)/scale
def objective(v):return -v[4]
def inequality(v):return values(v[:4])-v[4]
seed=json.loads((OUT/'nine-point-eight-support-relaxation-probe.json').read_text())['rows'][2]['relaxed_point']
starts=[seed[:4], [0]*4]+[np.array(seed[:4])+np.random.default_rng(j).normal(0,.01,4) for j in range(12)]
results=[]
for start in starts:
 start=np.asarray(start,dtype=float)
 initial=np.r_[start,float(np.min(values(start)))]
 sol=minimize(objective,initial,method='SLSQP',constraints=[{'type':'ineq','fun':inequality}],
              bounds=[(-1,1)]*4+[(None,None)],options={'maxiter':2500,'ftol':1e-13})
 results.append({'success':bool(sol.success),'minimum_normalized_minor':float(np.min(values(sol.x[:4]))),
  'claimed_margin':float(sol.x[4]),'free_coefficients':[float(v) for v in sol.x[:4]]})
results.sort(key=lambda r:r['minimum_normalized_minor'],reverse=True)
report={'schema':'marici.nima.nine-point-delete-three-graph-probe.v1','best':results[0],
 'runs':len(results),'scope':'Floating-point nonlinear search only. Positive candidate must be rationalized and checked exactly; negative optimum is not an impossibility certificate.'}
(OUT/'nine-point-delete-three-graph-probe.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
