#!/usr/bin/env python3
"""Exact independent supertwistor projectivity of six-point R-invariants."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
ts=(1,2,4,7,11,16);base={i:s.Matrix([1,t,t*t,t**3]) for i,t in enumerate(map(s.Integer,ts),1)}
labels=tuple(tuple(i for i in range(1,7) if i!=omit) for omit in range(1,7))
scalings=[(2,3,5,7,11,13),(1,-2,3,-5,7,-11),(3,1,4,1,5,9)]
def coefficients(Z,chi_scale,q):
 def br(r):return s.det(s.Matrix.hstack(*(Z[i] for i in r)))
 a,b,c,d,e=q;num={a:chi_scale[a]*br((b,c,d,e)),b:chi_scale[b]*br((c,d,e,a)),c:chi_scale[c]*br((d,e,a,b)),d:chi_scale[d]*br((e,a,b,c)),e:chi_scale[e]*br((a,b,c,d))}
 den=br((a,b,c,d))*br((b,c,d,e))*br((c,d,e,a))*br((d,e,a,b))*br((e,a,b,c))
 return {mono:s.factor(s.prod(num.get(i,0) for i in mono)/den) for mono in itertools.product(range(1,7),repeat=4)}
reference={q:coefficients(base,{i:s.Integer(1) for i in base},q) for q in labels};runs=[]
for scales in scalings:
 scale={i:s.Integer(v) for i,v in enumerate(scales,1)};Z={i:scale[i]*base[i] for i in base};fail=[]
 for q in labels:
  got=coefficients(Z,scale,q)
  for mono,v in reference[q].items():
   if s.factor(got[mono]-v)!=0:fail.append({'five_bracket':list(q),'monomial':list(mono)})
 runs.append({'scales':list(scales),'five_brackets_checked':6,'grassmann_coefficients_checked':6*6**4,'failure_count':len(fail),'failures':fail[:10],'passed':not fail})
checks={'six_five_brackets':len(labels)==6,'three_independent_rescalings':len(runs)==3,'all_five_brackets_projective':all(r['passed'] for r in runs)}
report={'schema':'marici.nima.six-point-r-invariant-projectivity.v1','benchmark':{'result':'independent projectivity of momentum-twistor NMHV five-brackets','reference':'Arkani-Hamed et al., The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM','arxiv':'1008.2958'},'transformation':'(Z_i, chi_i) -> t_i (Z_i, chi_i), independently for each i','runs':runs,'total_exact_coefficient_checks':sum(r['grassmann_coefficients_checked'] for r in runs),'checks':checks,'passed':all(checks.values()),'scope':'Exact rational checks of all six five-brackets under three nonuniform supertwistor rescalings.'}
out=ROOT/'research/nima/results/six-point-r-invariant-projectivity.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'checks':checks,'coefficient_checks':report['total_exact_coefficient_checks']},indent=2));raise SystemExit(0 if report['passed'] else 1)
