"""Local target orientation and exact cyclic source residues on candidate edge 1/2."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
compiler=json.loads((N/'results/seven-point-positroid-compiler.json').read_text())['cells']
assert compiler[2]['vanishing_cyclic_minors']==['Delta_(3,4)','Delta_(7,1)']
w1,w4,w5,w6,w7,u,v,h,e,g=s.symbols('w1 w4 w5 w6 w7 u v h e g');face=(w1,w4,w5,w6,w7,u,v)
# Face C3=0, Delta71=0. Cell 2 opens with C3 parallel C4 (h>0),
# zero-column-3 cell 1 opens by splitting 71 (e>0).
C=s.Matrix([[-w1,1,h,w4,w5,w6,w7],[-w1*(v+e),0,h*(1+g),w4,2*w5,u*w6,v*w7]])
Z=s.Matrix([[s.Integer(j)**r for r in range(6)] for j in range(1,8)])
Y=C.subs(g,0)*Z;B=Y[:,[0,1]].inv()*Y[:,2:]
base={w1:1,w4:1,w5:1,w6:1,w7:1,u:3,v:4,h:0,e:0}
T=B.reshape(8,1).jacobian(face).subs(base);assert T.rank()==7
J2=s.factor(T.row_join(B.reshape(8,1).diff(h).subs(base)).det())
J1=s.factor(T.row_join(B.reshape(8,1).diff(e).subs(base)).det());assert J1!=0 and J2!=0
def minor(M,i,j):return s.det(M[:,[i,j]])
for parameter,expected in ((h,{(3,4),(1,7)}),(e,{tuple(sorted((i,3))) for i in range(1,8) if i!=3})):
 D=C.subs({**base,g:0,parameter:s.Rational(1,100)})
 zero={(i+1,j+1) for i in range(7) for j in range(i+1,7) if minor(D,i,j)==0}
 assert zero==expected
 assert all(minor(D,i,j)>0 for i in range(7) for j in range(i+1,7) if (i+1,j+1) not in zero)
def gauge(M,pivots):
 D=M[:,list(pivots)].inv()*M;assert D[:,list(pivots)]==s.eye(2);return D
def cyc(M):return s.prod(minor(M,i,(i+1)%M.cols) for i in range(M.cols))
# Paired seven-column cell: transverse e resolves 71; g resolves 34.
D=gauge(C,(1,4));coords=[D[i,j] for j in (0,2,3,5,6) for i in range(2)]
Jac=s.Matrix(coords).jacobian((*face,h,e,g));L=s.factor((cyc(D)/(e*g)).subs({e:0,g:0}));assert L!=0
J0=s.factor(Jac.subs({e:0,g:0}).det())
R2=s.factor((J0/L)*h).subs(h,0);R2=s.factor(R2);assert R2!=0
# Zero-column-3 carrier: surviving columns 1,2,4,5,6,7, e resolves 71.
E=gauge(C.subs({h:0,g:0})[:,[0,1,3,4,5,6]],(1,3))
coords6=[E[i,j] for j in (0,2,4,5) for i in range(2)]
J6=s.factor(s.Matrix(coords6).jacobian((*face,e)).subs(e,0).det());L6=s.factor((cyc(E)/e).subs(e,0));assert L6!=0
R1=s.factor(J6/L6);ratio=s.factor(R2/R1)
report={'schema':'marici.nima.seven-point-one-two-wall.v1',
 'pair':[1,2],'shared_source_face':['C3=0','Delta_(7,1)=0'],
 'face_target_rank':T.rank(),'cell_two_inward_jacobian':str(J2),'cell_one_inward_jacobian':str(J1),
 'inward_ratio':str(s.factor(J2/J1)),'inward_side':'OPPOSITE' if J2*J1<0 else 'SAME',
 'paired_source_residue':str(R2),'zero_column_source_residue':str(R1),'source_residue_ratio':str(ratio),
 'scope':'One positive rational wall point for target Jacobians and symbolic source cyclic residues; no global triangulation or physical history-form equality.'}
(N/'results/seven-point-one-two-wall.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
