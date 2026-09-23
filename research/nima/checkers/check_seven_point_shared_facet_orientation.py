"""Compare two seven-point compiled cell images at a common codimension-three source face."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
compiler=json.loads((N/'results/seven-point-positroid-compiler.json').read_text());assert compiler['passed']
assert compiler['cells'][0]['vanishing_cyclic_minors']==['Delta_(2,3)','Delta_(5,6)']
assert compiler['cells'][1]['vanishing_cyclic_minors']==['Delta_(2,3)','Delta_(3,4)']
w=s.symbols('w2:8',positive=True);v,g,f=s.symbols('v g f');weights=(s.Integer(1),)+w
# Cell zero: g=t4-t3>0; cell one: f=t6-t5>0.
# On their shared source face both g and f vanish.
t=[0,1,1,1+g,2,2+f,v];C=s.Matrix([weights,[weights[i]*t[i] for i in range(7)]])
Z=s.Matrix([[s.Integer(j)**k for k in range(6)] for j in range(1,8)]);Y=C*Z
A=Y[:,[0,1]];B=A.inv()*Y[:,2:];face=(*w,v)
base={**{x:s.Integer(1) for x in w},v:s.Integer(3),g:s.Integer(0),f:s.Integer(0)}
F=B.reshape(8,1).jacobian(face).subs(base);normal0=B.reshape(8,1).diff(g).subs(base);normal1=B.reshape(8,1).diff(f).subs(base)
assert F.rank()==7
D0=s.factor(F.row_join(normal0).det());D1=s.factor(F.row_join(normal1).det());assert D0!=0 and D1==0
# First-order target variation of cell one is TANGENT to the shared image.
# Test whether an interior point restores eight-dimensional rank.
interior1={**base,f:s.Integer(1),v:s.Integer(4)}
J1=s.factor(B.reshape(8,1).jacobian((*face,f)).subs(interior1).det())
interior2={**{w[i]:s.Integer([2,3,2,1,3,2][i]) for i in range(6)},v:s.Integer(8),g:s.Integer(0),f:s.Integer(2)}
J2=s.factor(B.reshape(8,1).jacobian((*face,f)).subs(interior2).det())
# Verify the source minor directions select the advertised cells.
M=lambda i,j:s.factor(s.det(C[:,[i-1,j-1]]))
assert M(3,4).diff(g).subs(base)>0 and M(5,6).diff(f).subs(base)>0
assert M(2,3)==0
report={'schema':'marici.nima.seven-point-shared-facet-orientation.v1',
 'history_pair':[0,1],'shared_source_constraints':['Delta_(2,3)=0','Delta_(3,4)=0','Delta_(5,6)=0'],
 'face':'C columns w_i(1,t_i), t=(0,1,1,1,2,2,3), weights all one',
 'face_target_rank':F.rank(),'history_zero_inward_target_jacobian':str(D0),'history_one_inward_target_jacobian':str(D1),
 'history_one_interior_target_jacobians':[str(J1),str(J2)],
 'conclusion':'History one loses first-order transversality at this shared positive source face; opposite-side orientation cannot be inferred from positroid incidence alone.',
 'scope':'One common source-face point and fixed positive moment-curve external data; detects a degenerate inward direction, not a global cell-boundary identification.'}
(N/'results/seven-point-shared-facet-orientation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
