#!/usr/bin/env python3
"""Symbolic Tate-twisted endpoint quotient/contraquotient C4 algebra."""
import json
from pathlib import Path
import sympy as s

g=s.symbols('gamma', nonzero=True)
R=s.Matrix([[0,1/g],[g,0]])
Z=s.diag(1,-1)
F=Z*R
I=s.eye(2)
Pp=(I+R)/2; Pm=(I-R)/2
# Eigenline columns, valid for every nonzero gamma.
ep=s.Matrix([1,g]); em=s.Matrix([1,-g])
checks={
 'R_involution':s.simplify(R*R)==I,
 'Z_involution':Z*Z==I,
 'anticommute':s.simplify(Z*R+R*Z)==s.zeros(2),
 'F_square_minus_I':s.simplify(F*F)==-I,
 'F_fourth_I':s.simplify(F**4)==I,
 'plus_line':s.simplify(R*ep-ep)==s.zeros(2,1),
 'minus_line':s.simplify(R*em+em)==s.zeros(2,1),
 'F_plus_to_minus':s.simplify(F*ep-em)==s.zeros(2,1),
 'F_minus_to_minus_plus':s.simplify(F*em+ep)==s.zeros(2,1),
 'projectors_complementary':s.simplify(Pp*Pm)==s.zeros(2),
}
out={'schema':'marici.voevodsky.tate-twisted-endpoint-quotient-contraquotient-C4.v1','status':'passed' if all(checks.values()) else 'failed','R_infinity':[['0','gamma^-1'],['gamma','0']],'sheet_sign_Z':[['1','0'],['0','-1']],'quarter_turn_F=Z_R':[['0','gamma^-1'],['-gamma','0']],'positive_line':['1','gamma'],'negative_line':['1','-gamma'],'checks':checks,'unitary_qualification':'For |gamma|=1, R is self-adjoint unitary and the two lines are orthogonal. Algebraic order-four identities require only gamma nonzero.','interpretation':'The Tate cocycle rotates the two endpoint polarity quotients projectively, while Z exchanges quotient and contraquotient. Their product is the coherent C4 lift at every parameter.','claim_boundary':'Endpoint rank-two boundary algebra only; no bulk Green balance or Evans confinement.'}
root=Path(__file__).resolve().parents[3];p=root/'research/voevodsky/results/tate_twisted_endpoint_quotient_contraquotient_c4.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(out['status']!='passed')
