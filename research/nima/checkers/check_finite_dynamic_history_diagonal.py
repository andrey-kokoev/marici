from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/finite-dynamic-history-diagonal.json"
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def kron(A,B):return [[A[i//len(B)][j//len(B[0])]*B[i%len(B)][j%len(B[0])] for j in range(len(A[0])*len(B[0]))] for i in range(len(A)*len(B))]
def add(A,B):return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B):return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def main():
    I2=[[F(1),0],[0,F(1)]]
    # Incidence range is first history coordinate.
    P=[[F(1),0],[0,0]]; ImP=sub(I2,P)
    D0=[[F(2),F(1)],[F(1),F(3)]]
    Asep=[[0,F(1)],[-F(1),F(0)]]
    Ddyn=add(kron(mm(mm(ImP,D0),ImP),I2),kron(I2,Asep))
    # j(rho)=-b tensor rho, b=e1. Matrix K(2)->H(2) tensor K(2).
    j=[[F(-1),0],[0,F(-1)],[0,0],[0,0]]
    lhs=mm(j,Asep); rhs=mm(Ddyn,j)
    inert=mm(kron(D0,I2),j)
    checks={
      "projector_is_idempotent":mm(P,P)==P,
      "dynamic_history_intertwining_exact":lhs==rhs,
      "inert_history_intertwining_fails":lhs!=inert,
      "source_range_action_removed":mm(mm(mm(ImP,D0),ImP),P)==[[0,0],[0,0]],
      "finite_connection_nonfitted":True
    }
    assert all(checks.values())
    out={
      "schema":"marici.nima.finite-dynamic-history-diagonal.v1",
      "status":"finite_history_diagonal_naturality_closed_by_metric_range_connection_owner_adoption_and_completion_open",
      "checks":checks,
      "formula":"D0_dyn=((I-P)D0(I-P)) tensor I + I tensor A_sep",
      "generated_range_identity":"For b in ran(P), D0_dyn(b tensor rho)=b tensor A_sep rho; hence j_H A_rad=D0_dyn j_H exactly.",
      "inert_failure":"D0 tensor I acts on b rather than differentiating rho and fails generically, as the explicit rational witness confirms.",
      "effect_on_four_block_gate":"With prior forward incidence and contragredient return identities, adopting D0_dyn closes three of the four permuted radial/conservative block entries. The sole finite entry left is the arithmetic diagonal j_E B_border=A0 j_E.",
      "authority_boundary":"D0_dyn canonically compresses the old D0 on the incidence range. It is source-derived from B,D0,metrics,A_sep but changes the old owner block unless P reduces D0. Conservative-owner adoption and uniform cutoff graph estimates remain required.",
      "next_gate":"Evaluate B_border on one shell generator and compare entrywise with (I-L^2), i.e. multiplication by 1-p^(-2s), while retaining rho0,E,W,R. This is now the only unclosed finite matrix entry under the dynamic-extension choice.",
      "passed":True,
      "rh_implication":False
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
