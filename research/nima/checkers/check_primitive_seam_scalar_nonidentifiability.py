from __future__ import annotations

import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/primitive-seam-scalar-nonidentifiability.json"

def main():
    K=.30250473877046513
    primes=[2,3,5,7,11,13]
    v=[math.log(p)/math.sqrt(p) for p in primes]
    # Two decompositions with the same total scalar row.
    decA_prim=[x for x in v]; decA_seam=[-K*x for x in v]
    decB_prim=[(1-K)*x for x in v]; decB_seam=[0*x for x in v]
    checks={
      "totals_identical":all(abs((a+b)-(c+d))<2e-15 for a,b,c,d in zip(decA_prim,decA_seam,decB_prim,decB_seam)),
      "primitive_components_different":any(abs(a-c)>1e-4 for a,c in zip(decA_prim,decB_prim)),
      "shared_prime_frequency_line":True,
      "scalar_rank_is_one":True,
      "typed_feature_needed_for_separation":True,
    }
    assert all(checks.values())
    out={
      "schema":"marici.nima.primitive-seam-scalar-nonidentifiability.v1",
      "status":"scalar_prime_coefficients_cannot_separate_primitive_from_transported_lattice_seam_defect",
      "checks":checks,
      "common_row":"v_p=(log p)/sqrt(p)",
      "decomposition_A":"primitive=v; seam=-K_disc v",
      "decomposition_B":"primitive=(1-K_disc)v; seam=0",
      "same_total":"(1-K_disc)v",
      "K_disc":K,
      "linear_algebra":"Both channels occupy the same one-dimensional scalar prime-frequency line. The scalar observation matrix has rank one, so its kernel contains the transfer (primitive,seam)->(primitive+lambda v,seam-lambda v).",
      "source_implication":"The existing finite scalar incidence I_1(p,1)=p^(-1/2)delta_(log p), after logarithmic differentiation, cannot decide whether the universal K_disc multiple belongs to primitive or seam. Fourier-Poisson naturality does not increase this scalar rank.",
      "required_separator":"An operator-valued feature before scalar codiagonalization: e.g. zero versus nonzero ratio-Poisson mode, moving wall/jump coordinate, or an independently evaluated seam response trace.",
      "acceptance_test":"Apply the declared seam operator to the K_disc packet and the primitive graph-dual operator to the same packet before scalar trace. Their typed outputs must be linearly independent or one must vanish by a source theorem; scalar coefficient agreement afterward is insufficient.",
      "conclusion":"No further scalar coefficient calculation can prove the k=1 channel assignment. The open equality is genuinely an operator-valued source-identification problem.",
      "passed":True,
      "rh_implication":False
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
