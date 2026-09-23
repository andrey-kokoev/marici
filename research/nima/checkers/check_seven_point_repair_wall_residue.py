"""Compare exact source-form residues on shared zero-column / paired-minor wall."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
wall=json.loads((N/'results/seven-point-repair-shared-wall.json').read_text());assert wall['inward_side']=='OPPOSITE'
w2,w4,w5,w6,w7,u,v,f=s.symbols('w2 w4 w5 w6 w7 u v f')
# After column 3 is removed, six surviving columns form a top G(2,6).
C=s.Matrix([[1,w2,w4,w5,w6,w7],[0,w2,2*w4,w5*u,w6*(u+f),w7*v]])
D=C[:,[0,2]].inv()*C;assert D[:,[0,2]]==s.eye(2)
coords=[D[i,j] for j in (1,3,4,5) for i in range(2)]
params=(w2,w4,w5,w6,w7,u,v,f)
J=s.factor(s.Matrix(coords).jacobian(params).det())
prod=s.prod(s.det(D[:,[i,(i+1)%6]]) for i in range(6))
leading=s.factor((prod/f).subs(f,0));assert leading!=0
# Res_f Omega6, with df/f at end in declared coordinates.
residue=s.factor(J.subs(f,0)/leading)
# Earlier sourced cyclic double residue for paired-minor chart;
# Res_(w3=0) in the declared common-face coordinate order.
paired=s.Rational(2)/(v*w2*w4*w5*w6*w7*(u-2)*(v-u))
ratio=s.factor(residue/paired)
assert ratio!=0
point={w2:1,w4:1,w5:1,w6:1,w7:1,u:3,v:4}
report={'schema':'marici.nima.seven-point-repair-wall-residue.v1',
 'six_column_top_form':'Gauge surviving columns 1,4 to identity; d^8D_free / product of six ordered cyclic minors (1,2,4,5,6,7,1).',
 'common_face':'C3=0, Delta_(5,6)=0; coordinate order w2,w4,w5,w6,w7,u,v',
 'six_column_residue_coefficient':str(residue),'paired_minors_residue_coefficient':str(paired),
 'source_residue_ratio':str(ratio),'sample_ratio':str(ratio.subs(point)),
 'scope':'Source cyclic-form residue comparison only. Target pushforward orientation, on-shell history-form matching and global wall gluing remain separate.'}
(N/'results/seven-point-repair-wall-residue.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
