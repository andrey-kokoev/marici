#!/usr/bin/env python3
"""Exact total antisymmetry of the NMHV momentum-twistor five-bracket."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
Z={i:s.Matrix([1,t,t*t,t**3]) for i,t in enumerate(map(s.Integer,(1,2,4,7,11)),1)}
def parity(q):return (-1)**sum(q[i]>q[j] for i in range(5) for j in range(i+1,5))
def coeffs(q):
 def br(r):return s.det(s.Matrix.hstack(*(Z[i] for i in r)))
 a,b,c,d,e=q;num={a:br((b,c,d,e)),b:br((c,d,e,a)),c:br((d,e,a,b)),d:br((e,a,b,c)),e:br((a,b,c,d))};den=br((a,b,c,d))*br((b,c,d,e))*br((c,d,e,a))*br((d,e,a,b))*br((e,a,b,c))
 return {m:s.factor(s.prod(num.get(i,0) for i in m)/den) for m in itertools.product(range(1,6),repeat=4)}
base=coeffs((1,2,3,4,5));fail=[];checked=0
for q in itertools.permutations(range(1,6)):
 got=coeffs(q);sign=parity(q)
 for mono,v in base.items():
  checked+=1
  if s.factor(got[mono]-sign*v)!=0:fail.append({'permutation':list(q),'monomial':list(mono)})
checks={'all_120_permutations':checked==120*5**4,'even_permutations_invariant_and_odd_change_sign':not fail}
report={'schema':'marici.nima.momentum-twistor-five-bracket-antisymmetry.v1','benchmark':{'result':'total antisymmetry and cyclic invariance of the momentum-twistor NMHV five-bracket','reference':'Arkani-Hamed et al., The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM','arxiv':'1008.2958'},'permutations_checked':120,'grassmann_coefficients_per_permutation':5**4,'total_exact_coefficient_checks':checked,'failure_count':len(fail),'failures':fail[:10],'checks':checks,'passed':all(checks.values()),'scope':'Exact rational check on one generic positive five-twistor configuration.'}
out=ROOT/'research/nima/results/momentum-twistor-five-bracket-antisymmetry.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'permutations':120,'coefficient_checks':checked,'failures':len(fail)},indent=2));raise SystemExit(0 if report['passed'] else 1)
