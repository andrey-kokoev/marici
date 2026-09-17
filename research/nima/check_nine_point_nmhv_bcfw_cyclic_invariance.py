#!/usr/bin/env python3
"""Exact cyclic invariance of the nine-point NMHV BCFW representation."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
N=9
# R_{n;ij}=[n,i-1,i,j-1,j], 1<i<j<n and j>=i+2.
bcfw=tuple((N,i-1,i,j-1,j) for i in range(2,N-1) for j in range(i+2,N))
def shift(q):return tuple(i%N+1 for i in q)
cyclic=tuple(shift(q) for q in bcfw)
configs=[(1,2,4,7,11,16,22,29,37),(0,1,3,8,14,23,35,50,68),(-4,-2,1,5,12,20,31,45,62)]
def evaluate(ts):
 Z={i:s.Matrix([1,s.Integer(t),s.Integer(t)**2,s.Integer(t)**3]) for i,t in enumerate(ts,1)}
 def br(q):return s.det(s.Matrix.hstack(*(Z[i] for i in q)))
 def five(q):
  a,b,c,d,e=q; num={a:br((b,c,d,e)),b:br((c,d,e,a)),c:br((d,e,a,b)),d:br((e,a,b,c)),e:br((a,b,c,d))}
  den=br((a,b,c,d))*br((b,c,d,e))*br((c,d,e,a))*br((d,e,a,b))*br((e,a,b,c));return num,den
 data={q:five(q) for q in set(bcfw+cyclic)};fails=[]
 for mono in itertools.product(range(1,N+1),repeat=4):
  def coeff(q):
   num,den=data[q];return s.prod(num.get(i,0) for i in mono)/den
  delta=s.factor(sum(coeff(q) for q in bcfw)-sum(coeff(q) for q in cyclic))
  if delta!=0:fails.append({'monomial':list(mono),'difference':str(delta)})
 minors=[br(q) for q in itertools.combinations(range(1,N+1),4)]
 return {'parameters':list(ts),'positive_ordered_minors':all(v>0 for v in minors),'coefficients_checked':N**4,'failure_count':len(fails),'failures':fails[:10],'passed':all(v>0 for v in minors) and not fails}
runs=[evaluate(q) for q in configs]
report={'schema':'marici.nima.nine-point-nmhv-bcfw-cyclic-invariance.v1','benchmark':{'result':'cyclic invariance of the nine-point NMHV tree ratio function in momentum-twistor BCFW form','reference':'Arkani-Hamed et al., The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM','arxiv':'1008.2958'},'bcfw_terms':['['+''.join(map(str,q))+']' for q in bcfw],'cyclic_image_terms':['['+''.join(map(str,q))+']' for q in cyclic],'term_count':len(bcfw),'exact_positive_configurations':runs,'total_grassmann_coefficients_checked':sum(r['coefficients_checked'] for r in runs),'passed':all(r['passed'] for r in runs),'scope':'Exact rational verification on three positive nine-twistor configurations.'}
out=ROOT/'research/nima/results/nine-point-nmhv-bcfw-cyclic-invariance.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'terms':len(bcfw),'configurations':len(runs),'coefficients_checked':report['total_grassmann_coefficients_checked'],'failures':sum(r['failure_count'] for r in runs)},indent=2));raise SystemExit(0 if report['passed'] else 1)
