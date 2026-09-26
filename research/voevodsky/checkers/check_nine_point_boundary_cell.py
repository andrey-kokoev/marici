"""Audit the explicit right-boundary cell for outer(2,4), inner(4,6)."""
from pathlib import Path
import json
import sympy as s
from nine_point_source_r import Kinematics
root=Path(__file__).resolve().parents[1]
inputs=json.loads((root/'results/nine-point-missing-support-histories.json').read_text())['witnesses']
a1,a2,a3,a4,b3,b4,b5,b6=q=s.symbols('a1 a2 a3 a4 b3 b4 b5 b6')
C=s.Matrix([[a1,a2,a3,a4,0,0,0,0,-1],[0,0,b3*a3,b3*a4+b4,b5,b6,0,0,1]])
minors={(i,j):s.expand(C[:,[i-1,j-1]].det()) for i in range(1,10) for j in range(i+1,10)}
assert all(m==0 or all(c>0 for c in s.Poly(m,*q).coeffs()) for m in minors.values())
assert minors[2,3]==a2*b3*a3
fixtures=[(w['e'],s.Matrix([[s.Rational(x) for x in row] for row in w['quotient_twistors']])) for w in inputs]
fixtures.append(('moment_curve',s.Matrix([(1,t,t*t,t**3) for t in range(1,10)])))
Z6=s.Matrix([[t**j for j in range(6)] for t in range(1,10)])
positive_point=dict(zip(q,(1,2,3,4,2,3,4,5)))
Y=C.subs(positive_point)*Z6;chart=Y[:,:2].inv()*Y[:,2:]
fixtures.append(('constructed_positive_image',Z6[:,2:]-Z6[:,:2]*chart))
rows=[]
for label,z in fixtures:
 kin=Kinematics(z.tolist());av=z[:4,:].T.inv()*z[8,:].T
 boundary=av[2]*z[2,:]+av[3]*z[3,:]
 bv=-s.Matrix.vstack(boundary,z[3,:],z[4,:],z[5,:]).T.inv()*z[8,:].T
 values=list(av)+list(bv);point=dict(zip(q,values));assert C.subs(point)*z==s.zeros(2,4)
 if label=='constructed_positive_image':assert point==positive_point
 J=s.Matrix.hstack(*[s.Matrix(list(C.diff(v).subs(point)*z)) for v in q]).det(method='domain-ge')
 density=s.factor(1/(s.prod(values)*J));A,f=kin.ordinary(2,4);B,g=kin.inner(2,4,4,6,'right-nested')
 wedges={pair:s.factor(A[pair[0]]*B[pair[1]]-A[pair[1]]*B[pair[0]]) for pair in minors}
 pivot=next(pair for pair,m in minors.items() if m.subs(point)!=0)
 scale=s.factor(wedges[pivot]/minors[pivot].subs(point))
 assert all(s.factor(wedges[pair]-scale*m.subs(point))==0 for pair,m in minors.items())
 ratio=s.factor(f*g*scale**4/density)
 assert ratio==1,('normalization',label,ratio)
 component=s.factor(density*minors[2,3].subs(point)**4)
 assert component!=0
 rows.append({'input':label,'source_parameters':list(map(str,values)),'positive_preimage':all(x>0 for x in values),'jacobian':str(J),'source_to_dlog_ratio':str(ratio),'chi2_power4_chi3_power4':str(component)})
report={'passed':True,'history':{'outer':[2,4],'inner':[4,6],'branch':'right-nested','lower_boundary_update':True},'cell_matrix':[[str(x) for x in row] for row in C.tolist()],'ordered_minors_subtraction_free':True,'minor23':str(minors[2,3]),'witnesses':rows,'scope':'Exact full wedge and prefactor calibration at four inputs, including an independently constructed positive image, plus symbolic ordered-minor positivity. One boundary cell, not a full positive contour or amplitude completion.'}
(root/'results/nine-point-boundary-cell.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
