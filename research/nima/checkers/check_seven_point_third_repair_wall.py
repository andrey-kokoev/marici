"""Third candidate common-wall test: zero column 1 vs separated 34/71 cell."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
cells=json.loads((N/'results/seven-point-positroid-compiler.json').read_text())['cells'];assert cells[2]['vanishing_cyclic_minors']==['Delta_(3,4)','Delta_(7,1)']
Z=s.Matrix([[s.Integer(j)**k for k in range(6)] for j in range(1,8)])
w3,w4,w5,w6,w7,u,v,h,f=s.symbols('w3 w4 w5 w6 w7 u v h f');face=(w3,w4,w5,w6,w7,u,v)
C=s.Matrix([[-h,1,w3,w4,w5,w6,w7],[-h*v,0,w3,w4*(1+f),2*w5,u*w6,v*w7]])
Y=C*Z;B=Y[:,[0,1]].inv()*Y[:,2:]
base={w3:1,w4:1,w5:1,w6:1,w7:1,u:3,v:4,h:0,f:0}
T=B.reshape(8,1).jacobian(face).subs(base);assert T.rank()==7
JH=s.factor(T.row_join(B.reshape(8,1).diff(h).subs(base)).det())
JF=s.factor(T.row_join(B.reshape(8,1).diff(f).subs(base)).det());assert JH!=0 and JF!=0
def minor(M,i,j):return s.det(M[:,[i,j]])
for parameter,expected in ((h,{(3,4),(1,7)}),(f,{(1,j) for j in range(2,8)})):
 D=C.subs({**base,parameter:s.Rational(1,100)})
 zeros={(i+1,j+1) for i in range(7) for j in range(i+1,7) if minor(D,i,j)==0}
 assert zeros==expected
 assert all(minor(D,i,j)>0 for i in range(7) for j in range(i+1,7) if (i+1,j+1) not in zeros)
report={'schema':'marici.nima.seven-point-third-repair-wall.v1','history_pair':[2,3],
 'face':['C1=0','Delta_(3,4)=0'],'face_target_rank':T.rank(),
 'paired_cell_inward_jacobian':str(JH),'zero_column_inward_jacobian':str(JF),
 'inward_ratio':str(s.factor(JH/JF)),'inward_side':'OPPOSITE' if JH*JF<0 else 'SAME',
 'scope':'One rational positive wall point; no source-form residue comparison here.'}
(N/'results/seven-point-third-repair-wall.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
