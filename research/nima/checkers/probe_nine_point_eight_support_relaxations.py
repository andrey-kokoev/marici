"""Numerical discovery only: 5D affine lifts for each eight-label n=9 fibre."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json
import numpy as np
import sympy as s
from scipy.optimize import linprog
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
frozen=json.loads((OUT/'nine-point-support-stress.json').read_text())['first_no_seven_support_target'];neg=frozen['negative_initial_columns'];w=list(map(Q,frozen['weights']));t=list(map(Q,frozen['slopes']))
x=[(-w[i] if i<neg else w[i]) for i in range(9)];y=[x[i]*t[i] for i in range(9)]
K=s.Matrix([[(-1)**(j-p)*__import__('math').comb(6,j-p) if 0<=j-p<=6 else 0 for j in range(9)] for p in range(3)])
rows=[]
for deleted in range(9):
 pivot=next(p for p in reversed(range(3)) if K[p,deleted])
 free=[p for p in range(3) if p!=pivot]
 a,b,c,d,z=s.symbols('a b c d z');A={free[0]:a,free[1]:b};B={free[0]:c,free[1]:d}
 A[pivot]=(-x[deleted]-sum(A[p]*K[p,deleted] for p in free))/K[pivot,deleted]
 B[pivot]=(-y[deleted]-sum(B[p]*K[p,deleted] for p in free))/K[pivot,deleted]
 X=[x[j]+sum(A[p]*K[p,j] for p in range(3)) for j in range(9)]
 V=[y[j]+sum(B[p]*K[p,j] for p in range(3)) for j in range(9)]
 assert s.expand(X[deleted])==s.expand(V[deleted])==0
 coeff=[]
 for i,j in combinations([h for h in range(9) if h!=deleted],2):
  polynomial=s.Poly(s.expand(X[i]*V[j]-X[j]*V[i]),a,b,c,d)
  cross=polynomial.coeff_monomial(a*d);assert cross==-polynomial.coeff_monomial(b*c)
  allowed={(0,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,0,0,1),(0,1,1,0)}
  assert all(mon in allowed for mon,value in polynomial.terms())
  coeff.append([polynomial.coeff_monomial(1),*[polynomial.coeff_monomial(q) for q in (a,b,c,d)],cross])
 numeric=np.array([[float(v) for v in line] for line in coeff]);scale=np.max(np.abs(numeric),axis=1)
 assert np.all(scale>0);normalized=numeric/scale[:,None]
 solve=linprog(np.zeros(5),A_ub=-normalized[:,1:],b_ub=normalized[:,0],bounds=[(None,None)]*5,method='highs')
 row={'deleted_label':deleted+1,'linear_relaxation_status':solve.message,'relaxation_feasible':bool(solve.success)}
 if solve.success:
  row['relaxed_point']=[float(v) for v in solve.x]
  row['determinant_graph_defect']=float(solve.x[4]-(solve.x[0]*solve.x[3]-solve.x[1]*solve.x[2]))
 rows.append(row)
result={'schema':'marici.nima.nine-point-eight-support-relaxation-probe.v1','rows':rows,
 'scope':'Floating-point LP discovery only; no eight-label membership or impossibility claim without exact graph-realizable witness or exact Farkas exclusion.'}
(OUT/'nine-point-eight-support-relaxation-probe.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
