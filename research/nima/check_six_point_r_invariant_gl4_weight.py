#!/usr/bin/env python3
"""Exact GL(4) determinant weight of momentum-twistor five-brackets."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
base={i:s.Matrix([1,t,t*t,t**3]) for i,t in enumerate(map(s.Integer,(1,2,4,7,11,16)),1)};labels=tuple(tuple(i for i in range(1,7) if i!=o) for o in range(1,7))
matrices=[s.diag(2,1,1,1),s.Matrix([[1,2,0,0],[0,3,1,0],[0,0,1,1],[0,0,0,1]]),s.Matrix([[0,2,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])]
def coeffs(Z,q):
 def br(r):return s.det(s.Matrix.hstack(*(Z[i] for i in r)))
 a,b,c,d,e=q;num={a:br((b,c,d,e)),b:br((c,d,e,a)),c:br((d,e,a,b)),d:br((e,a,b,c)),e:br((a,b,c,d))};den=s.prod((br((a,b,c,d)),br((b,c,d,e)),br((c,d,e,a)),br((d,e,a,b)),br((e,a,b,c))))
 return {m:s.factor(s.prod(num.get(i,0) for i in m)/den) for m in itertools.product(range(1,7),repeat=4)}
ref={q:coeffs(base,q) for q in labels};runs=[]
for M in matrices:
 determinant=M.det();got={q:coeffs({i:M*base[i] for i in base},q) for q in labels};fails=0
 for q in labels:
  for mono,v in ref[q].items():fails += s.factor(got[q][mono]-v/determinant)!=0
 runs.append({'determinant':int(determinant),'expected_weight':'det(M)^-1','coefficients_checked':6*6**4,'failure_count':fails,'passed':fails==0})
checks={'three_nonunimodular_transformations':len(runs)==3 and all(abs(r['determinant'])!=1 for r in runs),'determinant_weight_minus_one':all(r['passed'] for r in runs)}
report={'schema':'marici.nima.six-point-r-invariant-gl4-weight.v1','benchmark':{'result':'GL(4) determinant weight -1 of bosonically transformed momentum-twistor five-brackets','context':'momentum-twistor covariance of NMHV R-invariants'},'runs':runs,'total_exact_coefficient_checks':sum(r['coefficients_checked'] for r in runs),'checks':checks,'passed':all(checks.values()),'scope':'Bosonic Z transforms with chi coordinates held fixed; SL(4) invariance is the determinant-one specialization.'}
out=ROOT/'research/nima/results/six-point-r-invariant-gl4-weight.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'checks':checks,'coefficient_checks':report['total_exact_coefficient_checks']},indent=2));raise SystemExit(0 if report['passed'] else 1)
