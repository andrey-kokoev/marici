"""Local target-side orientation for separated-pair and zero-column images."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
repair=json.loads((N/'results/seven-point-zero-column-repair.json').read_text());assert repair['rows'][0]['zero_column']==3
Z=s.Matrix([[s.Integer(j)**k for k in range(6)] for j in range(1,8)])
w2,w4,w5,w6,w7,u,v,h,f=s.symbols('w2 w4 w5 w6 w7 u v h f')
# Common face: C3=0 and C5 || C6.  h>0 opens the history-zero
# (23=0,56=0) source; f>0 opens the zero-column-3 source.
C=s.Matrix([[1,w2,h,w4,w5,w6,w7],
 [0,w2,h,w4*2,w5*u,w6*(u+f),w7*v]])
Y=C*Z;B=Y[:,[0,1]].inv()*Y[:,2:];face=(w2,w4,w5,w6,w7,u,v)
base={w2:1,w4:1,w5:1,w6:1,w7:1,u:3,v:4,h:0,f:0}
F=B.reshape(8,1).jacobian(face).subs(base);assert F.rank()==7
H=B.reshape(8,1).diff(h).subs(base);T=B.reshape(8,1).diff(f).subs(base)
JH=s.factor(F.row_join(H).det());JT=s.factor(F.row_join(T).det());assert JH!=0 and JT!=0
# Check all unconstrained source ordered minors are positive on both inward rays.
def minor(M,i,j):return s.det(M[:,[i,j]])
for variable in (h,f):
 values={**base,variable:s.Rational(1,100)};D=C.subs(values)
 zero={(i+1,j+1) for i in range(7) for j in range(i+1,7) if minor(D,i,j)==0}
 expected={(2,3),(5,6)} if variable==h else {(1,3),(2,3),(3,4),(3,5),(3,6),(3,7)}
 assert zero==expected
 assert all(minor(D,i,j)>0 for i in range(7) for j in range(i+1,7) if (i+1,j+1) not in zero)
report={'schema':'marici.nima.seven-point-repair-shared-wall.v1',
 'history_pair':[0,1],'positive_Z':'moment curve j=1..7 powers 0..5',
 'shared_source_face':['C3=0','Delta_(5,6)=0'],
 'shared_image_tangent_rank':F.rank(),
 'history_zero_inward_target_jacobian':str(JH),'zero_column_repair_inward_target_jacobian':str(JT),
 'inward_ratio':str(s.factor(JH/JT)),
 'inward_side':'OPPOSITE' if JH*JT<0 else 'SAME',
 'scope':'One exact rational shared-face point. Opposite local sides do not prove entire face matching, residue cancellation or global coverage.'}
(N/'results/seven-point-repair-shared-wall.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
