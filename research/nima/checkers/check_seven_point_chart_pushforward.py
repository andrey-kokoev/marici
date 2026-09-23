"""Birational fibre inverse and local canonical-form pushforward for one n=7 cell."""
import json,itertools
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
compiled=json.loads((N/'results/seven-point-positroid-compiler.json').read_text());assert compiled['passed']
cell=compiled['cells'][0];assert cell['vanishing_cyclic_minors']==['Delta_(2,3)','Delta_(5,6)']
Z=s.Matrix([[s.Integer(j)**k for k in range(6)] for j in range(1,8)]);k=Z.T.nullspace()[0];assert list(k)==[1,-6,15,-20,15,-6,1]
w=s.symbols('w2:8',positive=True);u,v=s.symbols('u v',positive=True);weights=(s.Integer(1),)+w;t=(0,1,1,2,u,u,v)
C=s.Matrix([weights,[weights[i]*t[i] for i in range(7)]])
Y=C*Z;A=Y[:,[0,1]];B=A.inv()*Y[:,2:];parameters=(*w,u,v)
J=B.reshape(8,1).jacobian(parameters)
# R is a rational section of the source-to-target linear map.
R=Z.T*(Z*Z.T).inv();assert Z*R==s.eye(6)
a,b=s.symbols('a b')
def delta(M,i,j):return s.det(M[:,[i,j]])
def invert(Yvalue):
 D0=Yvalue*R;D=D0+s.Matrix([[a*x for x in k],[b*x for x in k]])
 eq=[delta(D,1,2),delta(D,4,5)]
 # Both equations are LINEAR in the two kernel shifts (ab cancels).
 assert all(s.diff(e,a,b)==0 for e in eq)
 linear=s.Matrix([[s.diff(e,z) for z in (a,b)] for e in eq]);rhs=-s.Matrix([e.subs({a:0,b:0}) for e in eq]);det=s.factor(linear.det())
 assert det!=0
 ab=linear.inv()*rhs;recovered=D.subs({a:ab[0],b:ab[1]})
 assert recovered*Z==Yvalue and delta(recovered,1,2)==0 and delta(recovered,4,5)==0
 return recovered,det,[s.factor(x) for x in ab]
def canonical_density(values):
 # Product of six positive weight dlogs and the ordered M_0,5 form
 # du/(u-2) ^ dv/(v-u), expressed in target affine B coordinates.
 j=s.factor(J.subs(values).det());weight=s.prod(values[q] for q in w)*(values[u]-2)*(values[v]-values[u]);assert j!=0 and weight>0
 return {'target_jacobian':str(j),'candidate_form_coefficient':str(s.factor(1/(weight*j)))}
samples=[([1]*7,3,4),([1,2,3,2,1,3,2],4,6)];rows=[]
for ws,uu,vv in samples:
 values={**{w[i]:ws[i+1] for i in range(6)},u:uu,v:vv};source=C.subs(values);target=source*Z
 recovered,det,ab=invert(target)
 assert recovered==source
 assert all(delta(recovered,i,j)>0 for i,j in itertools.combinations(range(7),2) if (i,j) not in ((1,2),(4,5)))
 rows.append({'weights':ws,'u':uu,'v':vv,'fibre_constraint_determinant':str(det),
              'kernel_coefficients':list(map(str,ab)),'inverse_recovers_source':True,**canonical_density(values)})
assert rows[0]['target_jacobian']=='102400/194481'
report={'schema':'marici.nima.seven-point-chart-pushforward.v1',
 'inverse':'Given a target representative Y, R=Z^T(ZZ^T)^-1, D0=YR. Every source representative mapping to Y is D0+[a,b]^T k, k spans ker(Z^T). The two prescribed minors (23),(56) are linear equations in a,b; nonzero constraint determinant gives a unique rational inverse.',
 'canonical_density_assumption':'Product dlog w2..w7 times du/(u-2) wedge dv/(v-u), with coordinate orientation [w2..w7,u,v]. This is a candidate positive-chart canonical form; equality to the physical history has not been checked.',
 'target_coordinates':'B=(Y[:,0:2])^-1 Y[:,2:6], flattened row-major',
 'samples':rows,'scope':'Exact rational local inverse and candidate eight-form coefficients on a fixed moment-curve external Z; no equality with generalized-R or global triangulation.'}
p=N/'results/seven-point-chart-pushforward.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'samples':rows},indent=2))
