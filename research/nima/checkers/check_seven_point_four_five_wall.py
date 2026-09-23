"""Exact local image sides and source-form residues for repaired cells 4/5."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
prior=json.loads((N/'results/seven-point-multichamber-stress.json').read_text());assert any(r['closed_members']==[4,5] for r in prior['shared_wall_witnesses'])
w1,w3,w4,w6,w7,u,v,h,f,e=s.symbols('w1 w3 w4 w6 w7 u v h f e');face=(w1,w3,w4,w6,w7,u,v)
# Common face C5=0, Delta71=0. Cell 4 opens by a column 5
# parallel to column 6; cell 5 opens by splitting 71.
C=s.Matrix([[-w1,1,w3,w4,h,w6,w7],[-w1*(v+f+e),0,w3,2*w4,h*u,w6*u,w7*v]])
Z=s.Matrix([[s.Integer(j)**k for k in range(6)] for j in range(1,8)]);Y=C.subs(e,0)*Z
B=Y[:,[0,1]].inv()*Y[:,2:]
base={w1:1,w3:1,w4:1,w6:1,w7:1,u:3,v:4,h:0,f:0}
T=B.reshape(8,1).jacobian(face).subs(base);assert T.rank()==7
J4=s.factor(T.row_join(B.reshape(8,1).diff(h).subs(base)).det())
J5=s.factor(T.row_join(B.reshape(8,1).diff(f).subs(base)).det());assert J4!=0 and J5!=0
def minor(M,i,j):return s.det(M[:,[i,j]])
for parameter,expected in ((h,{(5,6),(1,7)}),(f,{tuple(sorted((i,5))) for i in range(1,8) if i!=5})):
 D=C.subs({**base,e:0,parameter:s.Rational(1,100)})
 zero={(i+1,j+1) for i in range(7) for j in range(i+1,7) if minor(D,i,j)==0}
 assert zero==expected
 assert all(minor(D,i,j)>0 for i in range(7) for j in range(i+1,7) if (i+1,j+1) not in zero)
# Cell 4 cyclic double residue: Delta56=0 by setting t5=u,
# Delta71=0 by e=0; transverse variables e and g splitting t5.
g=s.symbols('g');C4=C.subs({h:s.symbols('w5'),f:0,e:e});w5=s.symbols('w5')
# Reconstruct explicitly to avoid accidental symbolic substitution of h.
C4=s.Matrix([[-w1,1,w3,w4,w5,w6,w7],[-w1*(v+e),0,w3,2*w4,w5*(u-g),w6*u,w7*v]])
def gauge(M,pivots):
 D=M[:,list(pivots)].inv()*M;assert D[:,list(pivots)]==s.eye(2);return D
def cyc(M):return s.prod(minor(M,i,(i+1)%M.cols) for i in range(M.cols))
D=gauge(C4,(1,3));coords=[D[i,j] for j in (0,2,4,5,6) for i in range(2)]
# [face,w5,e,g], then residue e,g and w5 -> face.
J=s.Matrix(coords).jacobian((*face,w5,e,g));L=s.factor((cyc(D)/(e*g)).subs({e:0,g:0}));assert L!=0
J0=s.factor(J.subs({e:0,g:0}).det());R4=s.factor((J0/L)*w5).subs(w5,0);R4=s.factor(R4);assert R4!=0
# Cell 5 six-column top cyclic form after deletion of column 5;
# its Delta71 residue is f=0.
E=gauge(C.subs({h:0,e:0})[:,[0,1,2,3,5,6]],(1,3))
coords6=[E[i,j] for j in (0,2,4,5) for i in range(2)]
J6=s.factor(s.Matrix(coords6).jacobian((*face,f)).subs(f,0).det());L6=s.factor((cyc(E)/f).subs(f,0));assert L6!=0
R5=s.factor(J6/L6);ratio=s.factor(R4/R5)
report={'schema':'marici.nima.seven-point-four-five-wall.v1','pair':[4,5],
 'shared_source_face':['C5=0','Delta_(7,1)=0'],'face_image_tangent_rank':T.rank(),
 'cell_four_inward_target_jacobian':str(J4),'cell_five_inward_target_jacobian':str(J5),
 'inward_ratio':str(s.factor(J4/J5)),'inward_side':'OPPOSITE' if J4*J5<0 else 'SAME',
 'cell_four_source_residue':str(R4),'cell_five_source_residue':str(R5),'source_residue_ratio':str(ratio),
 'scope':'One rational local wall point for target orientation; symbolic source cyclic residues in declared gauges. Not global image gluing or physical history identification.'}
(N/'results/seven-point-four-five-wall.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
