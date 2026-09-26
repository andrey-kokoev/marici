"""Explicit eight-parameter positive cell for R(9;2,4) R(9;6,8)."""
from pathlib import Path
import json
import sympy as s
from nine_point_source_r import Kinematics
root=Path(__file__).resolve().parents[1];prior=json.loads((root/'results/nine-point-missing-support-histories.json').read_text());out=[]
q=s.symbols('a1:5')+s.symbols('b5:9')
C=s.zeros(2,9)
for i in range(4):C[0,i]=q[i];C[1,i+4]=q[i+4]
C[0,8]=-1;C[1,8]=1
# Each ordered maximal minor is zero or a positive monomial in q.
minors=[s.expand(C[:,[i,j]].det()) for i in range(9) for j in range(i+1,9)]
assert all(m==0 or all(c>0 for c in s.Poly(m,*q).coeffs()) for m in minors)
for witness in prior['witnesses']:
 z=s.Matrix([[s.Rational(x) for x in row] for row in witness['quotient_twistors']]);kin=Kinematics(z.tolist())
 av=z[:4,:].T.inv()*z[8,:].T;bv=-z[4:8,:].T.inv()*z[8,:].T
 values=list(av)+list(bv);point=dict(zip(q,values));assert C.subs(point)*z==s.zeros(2,4)
 J=s.Matrix.hstack(*[s.Matrix(list(C.diff(v)*z)) for v in q]).det()
 density=1/(s.prod(values)*J)
 A,f=kin.ordinary(2,4);B,g=kin.ordinary(6,8)
 # Compare all36 pair wedges up to scale, then prefactors.
 pairs=[(i,j) for i in range(1,10) for j in range(i+1,10)]
 w=[s.factor(A[i]*B[j]-A[j]*B[i]) for i,j in pairs]
 v=[C[:,[i-1,j-1]].det().subs(point) for i,j in pairs]
 pivot=next(i for i,x in enumerate(v) if x);scale=s.factor(w[pivot]/v[pivot])
 assert all(s.factor(x-scale*y)==0 for x,y in zip(w,v))
 assert s.factor(f*g*scale**4-density)==0
 mixed=s.factor(density*s.prod(C[:,[i-1,j-1]].det().subs(point) for i,j in prior['flavor_pairs']))
 assert mixed==s.Rational(witness['sum'])
 out.append({'e':witness['e'],'source_parameters':list(map(str,values)),'positive_preimage':all(x>0 for x in values),'mixed_coefficient':str(mixed)})
report={'passed':True,'cell_matrix':[[str(x) for x in row] for row in C.tolist()],'positive_minor_check':True,'witnesses':out,'scope':'One explicit positive eight-parameter cell; exact localized dlog supercoefficient equals the missing authored history at both targets. Not a complete contour or proof that appending it suffices.'}
(root/'results/nine-point-missing-cell.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
