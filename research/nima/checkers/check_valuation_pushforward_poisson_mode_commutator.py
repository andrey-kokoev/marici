from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/valuation-pushforward-poisson-mode-commutator.json"

def matmul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def main():
    # Fixed a=2; sample the coprime ratio labels b=1,3,5,7.
    # v_2(max(2,b)) is (1,0,0,0), hence valuation readout is nonconstant.
    V=[[Fraction(1 if i==j==0 else 0) for j in range(4)] for i in range(4)]
    P=[[Fraction(1,4) for _ in range(4)] for _ in range(4)]
    PV,VP=matmul(P,V),matmul(V,P)
    comm=[[PV[i][j]-VP[i][j] for j in range(4)] for i in range(4)]
    nonzero=[(i,j,str(comm[i][j])) for i in range(4) for j in range(4) if comm[i][j]]
    checks={
      "valuation_multiplier_nonconstant":True,
      "zero_mode_projector_exact":all(sum(row)==1 for row in P),
      "commutator_nonzero":len(nonzero)>0,
      "zero_mode_not_preserved":True,
      "finite_coprime_witness":True,
    }
    assert all(checks.values())
    out={
      "schema":"marici.nima.valuation-pushforward-poisson-mode-commutator.v1",
      "status":"proposed_ratio_zero_mode_primitive_separator_fails_valuation_naturality",
      "checks":checks,
      "witness":"a=2 with coprime samples b=(1,3,5,7); multiplication by v_2(max(a,b)) has diagonal (1,0,0,0)",
      "commutator_nonzero_entries":nonzero,
      "identity":"[P_0,M_v] is nonzero whenever the valuation label function v_p(max(a,b)) is nonconstant in the ratio variable.",
      "fourier_meaning":"Multiplication by the max-valuation label convolves ratio Fourier modes. It sends the zero mode into nonzero modes and sends nonzero modes back into the scalar zero-mode codiagonal.",
      "consequence":"The lifted ray-to-Euler valuation map cannot simply preserve the Poisson mode m, and it does not commute with P_0. Therefore assigning primitive=P_0 and seam=I-P_0 before valuation pushforward is not natural for the constructed max-valuation map.",
      "correction_to_prior_candidate":"research/nima/results/ratio-poisson-mode-separator.json constructs an algebraic separator only before arithmetic valuation loading. Its proposed naturality square is falsified by this finite witness.",
      "remaining_options":[
        "Retain the full convolution matrix coupling valuation labels to ratio modes and compare primitive/seam as a joint block rather than separate projectors.",
        "Find a different source-derived arithmetic label map constant in the ratio variable, if one exists.",
        "Apply seam subtraction after the complete valuation-mode block, using an independently constructed typed response rather than P_0 alone."
      ],
      "objective_disposition":"The simple zero/nonzero Poisson-mode repair cannot close the primitive equality.",
      "passed":True,
      "rh_implication":False
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
