#!/usr/bin/env python3
"""Eight-point NMHV cyclic invariance on generic exact twistor data."""
import itertools,json,random,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
N=8;bcfw=tuple((N,i-1,i,j-1,j) for i in range(2,N-1) for j in range(i+2,N));cyclic=tuple(tuple(i%N+1 for i in q) for q in bcfw)
rng=random.Random(10082958);configs=[]
while len(configs)<3:
 M=s.Matrix(4,N,[rng.randint(-9,9) for _ in range(4*N)])
 if all(M[:,q].det()!=0 for q in itertools.combinations(range(N),4)):configs.append(M)
def run(M):
 Z={i:M[:,i-1] for i in range(1,N+1)}
 def br(q):return s.det(s.Matrix.hstack(*(Z[i] for i in q)))
 def five(q):
  num={q[p]:br(q[p+1:]+q[:p]) for p in range(5)};den=s.prod(br(q[p+1:]+q[:p]) for p in range(5));return num,den
 data={q:five(q) for q in set(bcfw+cyclic)};fails=0
 for mono in itertools.product(range(1,N+1),repeat=4):
  def coefficient(q):num,den=data[q];return s.prod(num.get(i,0) for i in mono)/den
  fails += s.factor(sum(coefficient(q) for q in bcfw)-sum(coefficient(q) for q in cyclic))!=0
 return {'twistor_matrix':[[int(M[i,j]) for j in range(N)] for i in range(4)],'nonzero_ordered_minors':70,'coefficients_checked':N**4,'failure_count':fails,'passed':fails==0}
runs=[run(M) for M in configs];checks={'three_generic_configurations':len(runs)==3,'all_210_ordered_minors_nonzero':sum(r['nonzero_ordered_minors'] for r in runs)==210,'cyclic_invariance':all(r['passed'] for r in runs)}
report={'schema':'marici.nima.eight-point-nmhv-cyclic-generic-kinematics.v1','benchmark':{'result':'cyclic invariance of the eight-point NMHV BCFW ratio function','reference':'Arkani-Hamed et al., The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM','arxiv':'1008.2958'},'runs':runs,'total_exact_coefficient_checks':sum(r['coefficients_checked'] for r in runs),'checks':checks,'passed':all(checks.values()),'scope':'Three generic rational configurations outside the moment-curve family; finite exact verification.'}
out=ROOT/'research/nima/results/eight-point-nmhv-cyclic-generic-kinematics.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'configurations':len(runs),'coefficient_checks':report['total_exact_coefficient_checks'],'failures':sum(r['failure_count'] for r in runs)},indent=2));raise SystemExit(0 if report['passed'] else 1)
