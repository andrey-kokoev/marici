"""Known Gr(1,5) dlog cell fixes delta vs target-chart normalization."""
from pathlib import Path
import itertools,json
import sympy as s
checks=0;rows=[]
for parameters in ((1,2,3,4,9),(1,2,7,16,37)):
 Z=s.Matrix([(1,t,t*t,t**3) for t in parameters])
 # C=(1,q1,q2,q3,q4), F=C Z; oriented coordinate order q1..q4.
 J=Z[1:,:].T;solution=-J.inv()*Z[0,:].T
 C=s.Matrix([[1,*solution]]);assert C*Z==s.zeros(1,4)
 rho=1/s.prod(solution);delta=s.factor(rho/J.det())
 minors=[Z[[(i+j)%5 for j in range(1,5)],:].det() for i in range(5)]
 five_prefactor=1/s.prod(minors)
 assert C==s.Matrix([minors])/minors[0]
 for flavor_indices in itertools.product(range(5),repeat=4):
  left=delta*s.prod(C[i] for i in flavor_indices)
  right=five_prefactor*s.prod(minors[i] for i in flavor_indices)
  assert s.factor(left-right)==0;checks+=1
 # Complete actual target-chart derivative at B0=0, for arbitrary regular h.
 q=s.symbols('q1:5');symbolic=s.Matrix([[1,*q]]);point=dict(zip(q,solution))
 for h in (s.Matrix([1,2,3,5,11]),s.Matrix([2,7,1,8,3])):
  M=(C*h)[0];assert M!=0
  target=(symbolic*Z)/(symbolic*h)[0]
  JB=s.Matrix.hstack(*[target.diff(x).subs(point).T for x in q])
  assert s.factor(JB.det()-J.det()/M**4)==0
  normalized=C/M
  for i in range(5):assert s.factor(rho/JB.det()*normalized[i]**4-delta*C[i]**4)==0
  rows.append({'parameters':parameters,'frame_M':str(M),'wrong_unnormalized_chart_factor':str(M**4)})
report={'passed':True,'full_four_flavor_coefficients_checked':checks,'target_chart_frames':rows,'conclusion':'The dlog delta coefficient equals the full five-bracket. Chart Jacobian inversion must be paired with normalized fermions C/(Ch); using raw C adds spurious (Ch)^4.','scope':'Exact Gr(1,5) calibration and chart derivative at two rational inputs, four frame choices. Does not certify relative orientations of the four n9 cells.'}
p=Path(__file__).resolve().parents[1]/'results/five-bracket-delta-frame.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
