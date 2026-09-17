#!/usr/bin/env python3
"""Exact equality of two six-point NMHV BCFW representations."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
configs=[(1,2,4,7,11,16),(0,1,3,8,14,23),(-3,-1,2,6,13,21)]
left=((2,3,4,5,6),(1,2,4,5,6),(1,2,3,4,6))
right=((1,3,4,5,6),(1,2,3,5,6),(1,2,3,4,5))
def evaluate(ts):
 Z={i:s.Matrix([1,s.Integer(t),s.Integer(t)**2,s.Integer(t)**3]) for i,t in enumerate(ts,1)}
 def br(q):return s.det(s.Matrix.hstack(*(Z[i] for i in q)))
 def five(labels):
  a,b,c,d,e=labels
  num={a:br((b,c,d,e)),b:br((c,d,e,a)),c:br((d,e,a,b)),d:br((e,a,b,c)),e:br((a,b,c,d))}
  den=br((a,b,c,d))*br((b,c,d,e))*br((c,d,e,a))*br((d,e,a,b))*br((e,a,b,c))
  return num,den
 data={q:five(q) for q in left+right};fail=[]
 for mono in itertools.product(range(1,7),repeat=4):
  def coeff(q):
   num,den=data[q];return s.prod(num.get(i,0) for i in mono)/den
  delta=s.factor(sum(coeff(q) for q in left)-sum(coeff(q) for q in right))
  if delta!=0:fail.append({'monomial':list(mono),'difference':str(delta)})
 minors=[br(q) for q in itertools.combinations(range(1,7),4)]
 return {'parameters':list(ts),'positive_ordered_minors':all(v>0 for v in minors),'coefficients_checked':6**4,'failure_count':len(fail),'failures':fail[:10],'passed':all(v>0 for v in minors) and not fail}
runs=[evaluate(q) for q in configs]
report={'schema':'marici.nima.six-point-nmhv-bcfw-triangulation-independence.v1','benchmark':{'result':'equality of two three-term BCFW representations of the six-point NMHV tree ratio function','reference':'Arkani-Hamed et al., The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM','arxiv':'1008.2958'},'left_representation':['[23456]','[12456]','[12346]'],'right_representation':['[13456]','[12356]','[12345]'],'exact_positive_configurations':runs,'total_grassmann_coefficients_checked':sum(r['coefficients_checked'] for r in runs),'passed':all(r['passed'] for r in runs),'scope':'Exact rational checks on three positive momentum-twistor configurations; equality follows generally from the six-term five-bracket identity.'}
out=ROOT/'research/nima/results/six-point-nmhv-bcfw-triangulation-independence.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'configurations':len(runs),'coefficients_checked':report['total_grassmann_coefficients_checked'],'failures':sum(r['failure_count'] for r in runs)},indent=2));raise SystemExit(0 if report['passed'] else 1)
