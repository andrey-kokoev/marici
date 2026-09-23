"""Second exact common-wall orientation and source residue: paired cell vs zero column 5."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
repair=json.loads((N/'results/seven-point-zero-column-repair.json').read_text());assert repair['rows'][2]['zero_column']==5
Z=s.Matrix([[s.Integer(j)**k for k in range(6)] for j in range(1,8)])
w2,w3,w4,w6,w7,u,v,h,f=s.symbols('w2 w3 w4 w6 w7 u v h f');face=(w2,w3,w4,w6,w7,u,v)
# Common face C5=0 and 23 parallel. Inward h>0 opens 56-parallel
# on original cell 0; inward f>0 splits 23 on zero-column-5 carrier.
C=s.Matrix([[1,w2,w3,w4,h,w6,w7],
 [0,w2,w3*(1+f),2*w4,h*u,w6*u,w7*v]])
Y=C*Z;B=Y[:,[0,1]].inv()*Y[:,2:]
base={w2:1,w3:1,w4:1,w6:1,w7:1,u:3,v:4,h:0,f:0}
T=B.reshape(8,1).jacobian(face).subs(base);assert T.rank()==7
JH=s.factor(T.row_join(B.reshape(8,1).diff(h).subs(base)).det())
JF=s.factor(T.row_join(B.reshape(8,1).diff(f).subs(base)).det());assert JH!=0 and JF!=0
# Verify both inward rays are precisely inside their source strata.
def minor(M,i,j):return s.det(M[:,[i,j]])
for parameter,expected in ((h,{(2,3),(5,6)}),(f,{(1,5),(2,5),(3,5),(4,5),(5,6),(5,7)})):
 D=C.subs({**base,parameter:s.Rational(1,100)})
 zeros={(i+1,j+1) for i in range(7) for j in range(i+1,7) if minor(D,i,j)==0}
 assert zeros==expected
 assert all(minor(D,i,j)>0 for i in range(7) for j in range(i+1,7) if (i+1,j+1) not in zeros)
# Top form of surviving six columns (1,2,3,4,6,7) and residue f=0.
D=C[:,[0,1,2,3,5,6]];gauge=D[:,[0,3]].inv()*D
coords=[gauge[i,j] for j in (1,2,4,5) for i in range(2)]
free=(w2,w3,w4,w6,w7,u,v,f)
J=s.factor(s.Matrix(coords).jacobian(free).subs(h,0).det())
prod=s.prod(s.det(gauge[:,[i,(i+1)%6]]) for i in range(6))
leading=s.factor((prod/f).subs({h:0,f:0}));assert leading!=0
residue=s.factor(J.subs(f,0)/leading)
# Pullback of corrected cell-zero double residue to C5=0.
# Initial order w2,w3,w4,w5,w6,w7,u,v; moving dw5 to end
# crosses three variables (w6,w7,u,v = four), hence sign +.
paired=s.Rational(2)/(v*w2*w3*w4*w6*w7*(u-2)*(v-u))
ratio=s.factor(residue/paired)
report={'schema':'marici.nima.seven-point-second-repair-wall.v1',
 'history_pair':[0,5],'face':['C5=0','Delta_(2,3)=0'],
 'face_target_rank':T.rank(),'original_inward_jacobian':str(JH),'repair_inward_jacobian':str(JF),
 'inward_ratio':str(s.factor(JH/JF)),'inward_side':'OPPOSITE' if JH*JF<0 else 'SAME',
 'source_residue_ratio':str(ratio),'source_residue_ratio_at_sample':str(ratio.subs(base)),
 'scope':'One shared image point and symbolic source residue, not global image coverage or physical history-form equality.'}
(N/'results/seven-point-second-repair-wall.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
