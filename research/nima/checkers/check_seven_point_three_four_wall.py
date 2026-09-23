"""Local target orientation and source cyclic residues on candidate edge 3/4."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
compiler=json.loads((N/'results/seven-point-positroid-compiler.json').read_text())['cells']
assert compiler[4]['vanishing_cyclic_minors']==['Delta_(5,6)','Delta_(7,1)']
w3,w4,w5,w6,w7,u,v,h,e,g=s.symbols('w3 w4 w5 w6 w7 u v h e g');face=(w3,w4,w5,w6,w7,u,v)
C=s.Matrix([[-h,1,w3,w4,w5,w6,w7],[-h*(v+e),0,w3,2*w4,u*w5,(u+g)*w6,v*w7]])
Z=s.Matrix([[s.Integer(j)**r for r in range(6)] for j in range(1,8)])
Y=C.subs(e,0)*Z;B=Y[:,[0,1]].inv()*Y[:,2:]
base={w3:1,w4:1,w5:1,w6:1,w7:1,u:3,v:4,h:0,g:0}
T=B.reshape(8,1).jacobian(face).subs(base);assert T.rank()==7
J4=s.factor(T.row_join(B.reshape(8,1).diff(h).subs(base)).det())
J3=s.factor(T.row_join(B.reshape(8,1).diff(g).subs(base)).det());assert J4!=0 and J3!=0
def minor(M,i,j):return s.det(M[:,[i,j]])
for parameter,expected in ((h,{(5,6),(1,7)}),(g,{(1,i) for i in range(2,8)})):
 D=C.subs({**base,e:0,parameter:s.Rational(1,100)})
 zero={(i+1,j+1) for i in range(7) for j in range(i+1,7) if minor(D,i,j)==0}
 assert zero==expected
 assert all(minor(D,i,j)>0 for i in range(7) for j in range(i+1,7) if (i+1,j+1) not in zero)
def gauge(M,pivots):
 D=M[:,list(pivots)].inv()*M;assert D[:,list(pivots)]==s.eye(2);return D
def cyc(M):return s.prod(minor(M,i,(i+1)%M.cols) for i in range(M.cols))
D=gauge(C,(1,3));coords=[D[i,j] for j in (0,2,4,5,6) for i in range(2)]
Jac=s.Matrix(coords).jacobian((*face,h,e,g));L=s.factor((cyc(D)/(e*g)).subs({e:0,g:0}));assert L!=0
J0=s.factor(Jac.subs({e:0,g:0}).det());R4=s.factor((J0/L)*h).subs(h,0);R4=s.factor(R4);assert R4!=0
E=gauge(C.subs({h:0,e:0})[:,list(range(1,7))],(0,2))
coords6=[E[i,j] for j in (1,3,4,5) for i in range(2)]
J6=s.factor(s.Matrix(coords6).jacobian((*face,g)).subs(g,0).det());L6=s.factor((cyc(E)/g).subs(g,0));assert L6!=0
R3=s.factor(J6/L6);ratio=s.factor(R4/R3)
report={'schema':'marici.nima.seven-point-three-four-wall.v1','pair':[3,4],
 'shared_source_face':['C1=0','Delta_(5,6)=0'],'face_target_rank':T.rank(),
 'cell_four_inward_jacobian':str(J4),'cell_three_inward_jacobian':str(J3),
 'inward_ratio':str(s.factor(J4/J3)),'inward_side':'OPPOSITE' if J4*J3<0 else 'SAME',
 'paired_source_residue':str(R4),'zero_column_source_residue':str(R3),'source_residue_ratio':str(ratio),
 'scope':'One positive rational wall point for target Jacobians and symbolic source cyclic residues; no global triangulation or physical history-form equality.'}
(N/'results/seven-point-three-four-wall.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
