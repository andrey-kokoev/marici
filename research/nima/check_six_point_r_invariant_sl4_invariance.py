#!/usr/bin/env python3
"""Exact SL(4) invariance of all six-point momentum-twistor five-brackets."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
ts=map(s.Integer,(1,2,4,7,11,16));base={i:s.Matrix([1,t,t*t,t**3]) for i,t in enumerate(ts,1)}
labels=tuple(tuple(i for i in range(1,7) if i!=o) for o in range(1,7))
matrices=[s.Matrix([[1,2,0,0],[0,1,3,0],[0,0,1,4],[0,0,0,1]]),s.Matrix([[1,0,0,0],[-2,1,0,0],[3,0,1,0],[1,-4,2,1]]),s.Matrix([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]])]
def coeffs(Z,q):
 def br(r):return s.det(s.Matrix.hstack(*(Z[i] for i in r)))
 a,b,c,d,e=q;num={a:br((b,c,d,e)),b:br((c,d,e,a)),c:br((d,e,a,b)),d:br((e,a,b,c)),e:br((a,b,c,d))};den=br((a,b,c,d))*br((b,c,d,e))*br((c,d,e,a))*br((d,e,a,b))*br((e,a,b,c))
 return {m:s.factor(s.prod(num.get(i,0) for i in m)/den) for m in itertools.product(range(1,7),repeat=4)}
ref={q:coeffs(base,q) for q in labels};runs=[]
for M in matrices:
 Z={i:M*base[i] for i in base};fail=[]
 for q in labels:
  got=coeffs(Z,q)
  for mono,v in ref[q].items():
   if s.factor(got[mono]-v)!=0:fail.append({'five_bracket':list(q),'monomial':list(mono)})
 runs.append({'matrix':[[int(v) for v in M.row(i)] for i in range(4)],'determinant':int(M.det()),'coefficients_checked':6*6**4,'failure_count':len(fail),'passed':M.det()==1 and not fail})
checks={'three_unimodular_transformations':len(runs)==3 and all(r['determinant']==1 for r in runs),'all_six_five_brackets_invariant':all(r['passed'] for r in runs)}
report={'schema':'marici.nima.six-point-r-invariant-sl4-invariance.v1','benchmark':{'result':'SL(4) momentum-twistor covariance of NMHV five-brackets','reference':'Arkani-Hamed et al., The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM','arxiv':'1008.2958'},'runs':runs,'total_exact_coefficient_checks':sum(r['coefficients_checked'] for r in runs),'checks':checks,'passed':all(checks.values()),'scope':'Exact rational verification under three nontrivial determinant-one transformations.'}
out=ROOT/'research/nima/results/six-point-r-invariant-sl4-invariance.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'checks':checks,'coefficient_checks':report['total_exact_coefficient_checks']},indent=2));raise SystemExit(0 if report['passed'] else 1)
