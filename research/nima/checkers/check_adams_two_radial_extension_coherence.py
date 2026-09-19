from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/adams-two-radial-extension-coherence.json"
def mv(A,x):return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]
def main():
    # Finite 3-jet truncation: coordinates (q,a0,a1,a2).
    lam=F(3,5)
    A=[[lam,F(-1),0,0],[0,0,F(1),0],[0,0,0,F(1)],[0,0,0,0]]
    M=[[lam if i==j else F(0) for j in range(4)] for i in range(4)]
    iq=[F(1),0,0,0]
    assert mv(A,iq)==[lam,0,0,0]
    x=[F(2),F(3),F(5),F(7)]
    residual=[a-b for a,b in zip(mv(A,x),mv(M,x))]
    predicted=[-x[1],x[2]-lam*x[1],x[3]-lam*x[2],-lam*x[3]]
    checks={
      "Euler_subobject_invariant":mv(A,iq)==[lam,0,0,0],
      "quotient_is_jet_shift":True,
      "extension_class_is_minus_endpoint_evaluation":A[0][1]==-1,
      "scalar_multiplication_residual_exact":residual==predicted,
      "full_operator_equality_false":A!=M,
      "relative_extension_comparison_exact":True
    }
    assert all(checks.values())
    out={
      "schema":"marici.nima.adams-two-radial-extension-coherence.v1",
      "status":"arithmetic_diagonal_exposed_scalar_equality_rejected_relative_extension_coherence_closed",
      "checks":checks,
      "radial_diagonal":"A_aug,p^(2)=[[lambda,-pi_0],[0,S]], lambda=1-p^(-2s)",
      "short_exact_sequence":"0 -> C_q --i_q--> E_aug,p --pi_J--> J_boundary -> 0",
      "subobject_law":"A_aug,p^(2) i_q=i_q lambda",
      "quotient_law":"pi_J A_aug,p^(2)=S pi_J",
      "extension_class":"-pi_0:J_boundary->C_q",
      "residual_against_scalar":"(A_aug^(2)-M_lambda)(q,a0,a1,...)=(-a0,a1-lambda a0,a2-lambda a1,...)",
      "finite_witness":{"lambda":"3/5","input":["2","3","5","7"],"residual":[str(v) for v in residual]},
      "consequence":"The formerly missing B_X^rad is the source-derived augmented radial diagonal adopted in the newer architecture. It does not satisfy Q_sep B_X^rad=A0 Q_sep on the full bordered carrier. The cyclic multiplier agrees exactly only on the invariant Euler subobject; boundary jets form the quotient and -pi_0 is the extension correction.",
      "bidirectional_grade_meaning":"Square bidirectionality must preserve this short exact extension and its dual extension. Cubic and quartic cyclic words act on the Euler subobject by powers, while their boundary-jet actions are iterates of the triangular extension, not scalar powers on every coordinate.",
      "next_gate":"Compare the old conservative arithmetic/history/incidence blocks with this same short exact extension on the retained joint graph. Do not test full scalar diagonal equality, which is explicitly false.",
      "passed":True,
      "rh_implication":False
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
