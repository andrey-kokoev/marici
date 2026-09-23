"""Fourfold cyclic residue of the intrinsic eight-label paired source cell."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
prior=json.loads((OUT/'nine-point-paired-cell-verification.json').read_text());assert prior['passed']
w2,w4,w5,w6,w7,w8,t,u,e1,e2,e3,e4=s.symbols('w2 w4 w5 w6 w7 w8 t u e1 e2 e3 e4')
weights=(w2,w4,w5,w6,w7,w8);variables=(*weights,t,u)
# GL(2) gauge C1=(1,0), C3=(0,1); columns are retained physical
# labels (1,2,4,5,6,7,8,9), so the four pairs are consecutive.
C=s.Matrix([[1,w2,0,-w4*e2,-w5,-w6,-w7,-w8],
            [0,w2*e1,1,w4,w5*t,w6*(t-e3),w7*u,w8*(u-e4)]])
assert C[:,[0,2]]==s.eye(2)
def det(i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
assert [s.factor(det(i,j)) for i,j in ((0,1),(2,3),(4,5),(6,7))]==[w2*e1,w4*e2,w5*w6*e3,w7*w8*e4]
free=[C[i,j] for j in (1,3,4,5,6,7) for i in range(2)]
J=s.factor(s.Matrix(free).jacobian((*variables,e1,e2,e3,e4)).subs({e1:0,e2:0,e3:0,e4:0}).det())
cyclic=s.prod(det(i,(i+1)%8) for i in range(8))
leading=s.factor((cyclic/(e1*e2*e3*e4)).subs({e1:0,e2:0,e3:0,e4:0}))
assert J!=0 and leading!=0
form=s.factor(J/leading)
# Normalization is independent of the chart's positive weights only after
# division by their six dlog factors; angular factor is exact.
angular=s.factor(form*s.prod(weights))
assert not any(angular.has(w) for w in weights)
# Direct admissible rational chart samples plus one near-boundary point.
for point in ({w2:1,w4:1,w5:1,w6:1,w7:1,w8:1,t:3,u:2},
              {w2:2,w4:3,w5:1,w6:4,w7:2,w8:5,t:s.Rational(7,2),u:s.Rational(3,2)}):
 assert point[t]>point[u]>0
 D=C.subs({**point,e1:0,e2:0,e3:0,e4:0})
 assert all(D[0,i]*D[1,j]-D[0,j]*D[1,i]>0 for i in range(8) for j in range(i+1,8)
            if (i,j) not in ((0,1),(2,3),(4,5),(6,7)))
report={'schema':'marici.nima.nine-point-paired-source-form.v1','passed':True,
 'retained_labels':[1,2,4,5,6,7,8,9],
 'source_cell':'four disjoint paired columns, ordered weights w2,w4,w5,w6,w7,w8>0 and t>u>0',
 'top_cyclic_form':'d^12C_free / product of eight cyclic minors in gauge C1,C3=identity',
 'fourfold_residue_orientation':'parameters (w2,w4,w5,w6,w7,w8,t,u,e1,e2,e3,e4), residues e1,e2,e3,e4',
 'source_residue_coefficient':str(form),'angular_factor_after_six_weight_dlogs':str(angular),
 'scope':'Intrinsic source Grassmannian canonical form of one eight-label paired cell. No pushforward to CZ, identification with a sourced n=9 history, or external source normalization for zero-column embedding.'}
(OUT/'nine-point-paired-source-form.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'form':str(form),'angular_factor':str(angular)},indent=2))
