#!/usr/bin/env python3
"""Six-term R-invariant identity on generic exact momentum-twistor data."""
import itertools,json,random,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
rng=random.Random(171109102);configs=[]
while len(configs)<5:
 M=s.Matrix(4,6,[rng.randint(-7,7) for _ in range(24)])
 minors=[M[:,q].det() for q in itertools.combinations(range(6),4)]
 if all(v!=0 for v in minors):configs.append(M)
def run(M):
 Z={i:M[:,i-1] for i in range(1,7)}
 def br(q):return s.det(s.Matrix.hstack(*(Z[i] for i in q)))
 def five(q):
  num={q[p]:br(q[p+1:]+q[:p]) for p in range(5)};den=s.prod(br(q[p+1:]+q[:p]) for p in range(5));return num,den
 terms=[]
 for omit in range(1,7):
  q=tuple(i for i in range(1,7) if i!=omit);terms.append(((-1)**(omit-1),five(q)))
 fail=[]
 for mono in itertools.product(range(1,7),repeat=4):
  v=s.factor(sum(sign*s.prod(num.get(i,0) for i in mono)/den for sign,(num,den) in terms))
  if v!=0:fail.append({'monomial':list(mono),'value':str(v)})
 return {'twistor_matrix':[[int(M[i,j]) for j in range(6)] for i in range(4)],'nonzero_ordered_minors':15,'coefficients_checked':6**4,'failure_count':len(fail),'passed':not fail}
runs=[run(M) for M in configs]
checks={'five_generic_configurations':len(runs)==5,'all_75_ordered_minors_nonzero':sum(r['nonzero_ordered_minors'] for r in runs)==75,'six_term_identity_everywhere_tested':all(r['passed'] for r in runs)}
report={'schema':'marici.nima.six-term-r-invariant-identity-generic-kinematics.v1','benchmark':{'result':'six-term NMHV momentum-twistor five-bracket identity','reference':'Arkani-Hamed et al., The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM','arxiv':'1008.2958'},'runs':runs,'total_exact_coefficient_checks':sum(r['coefficients_checked'] for r in runs),'checks':checks,'passed':all(checks.values()),'scope':'Five deterministic generic rational configurations, not restricted to moment-curve positive data; still a finite exact test rather than a symbolic proof.'}
out=ROOT/'research/nima/results/six-term-r-invariant-identity-generic-kinematics.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'configurations':len(runs),'coefficient_checks':report['total_exact_coefficient_checks'],'failures':sum(r['failure_count'] for r in runs)},indent=2));raise SystemExit(0 if report['passed'] else 1)
