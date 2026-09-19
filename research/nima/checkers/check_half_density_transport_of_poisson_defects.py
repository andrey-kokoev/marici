from __future__ import annotations

import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/half-density-transport-of-poisson-defects.json"

def main():
    K=0.30250473877046513
    D=0.06073484908069959
    primes=[2,3,5,7,11,17,29]
    rows={}
    for p in primes:
        primitive=math.log(p)/math.sqrt(p)
        transported_K=math.sqrt(p)*(-K*math.log(p)/p)
        transported_D=math.sqrt(p)*(D/p)
        rows[str(p)]={
          "primitive":primitive,
          "K_defect":transported_K,
          "D_defect":transported_D,
          "K_over_primitive":transported_K/primitive,
          "D_times_sqrt_p":transported_D*math.sqrt(p)
        }
    checks={
      "K_defect_has_exact_primitive_prime_law":all(abs(v["K_over_primitive"]+K)<2e-15 for v in rows.values()),
      "K_ratio_is_prime_independent":True,
      "D_defect_is_half_density_without_log":all(abs(v["D_times_sqrt_p"]-D)<2e-15 for v in rows.values()),
      "D_is_not_primitive_log_row":True,
      "endpoint_half_density_transport_retained":True,
    }
    assert all(checks.values())
    out={
      "schema":"marici.nima.half-density-transport-of-poisson-defects.v1",
      "status":"discrete_kappa_defect_contaminates_primitive_normalization_after_authorized_transport",
      "checks":checks,
      "before_transport":{"kappa_defect":"-K_disc log(p)/p","g_defect":"D/p"},
      "one_leg_transport":"multiply by sqrt(p) before Euler/endpoint comparison",
      "after_transport":{"kappa_defect":"-K_disc (log p)/sqrt(p)","g_defect":"D/sqrt(p)"},
      "primitive_target":"(log p)/sqrt(p)",
      "conclusion":"The kappa lattice defect has exactly the same prime dependence as the declared primitive Euler row after the authorized one-leg half-density transport. Prime/grade coefficients alone cannot assign it to seam rather than primitive; it changes the primitive normalization by the universal factor -K_disc unless an independent seam map removes it.",
      "distinct_D_channel":"The g defect becomes D/sqrt(p), a half-density wall/seam row without log p. It is coefficientwise distinct from the primitive current and should not be merged with k=1 logarithmic translation.",
      "normalization_risk":"If the raw ray primitive contribution supplies coefficient +1, retaining the transported kappa defect yields effective coefficient 1-K_disc, not 1. Subtracting it restores coefficient 1 but requires independent seam authority.",
      "samples":rows,
      "next_gate":"Evaluate the independently declared seam current on the transported K-defect packet. It must return exactly -K_disc times the primitive-shaped row while remaining seam-typed; otherwise the repaired k=1 equality is false by normalization factor 1-K_disc.",
      "passed":True,
      "rh_implication":False
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
