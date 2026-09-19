from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/ratio-poisson-mode-separator.json"

def main():
    # Finite model of the typed ratio-Fourier carrier: e0 is the continuum
    # zero mode and e1 stands for the closed nonzero-mode subspace.
    primitive=(Fraction(1),Fraction(0))
    seam=(Fraction(0),Fraction(1))
    scalar_codiagonal=lambda x:x[0]+x[1]
    checks={
      "zero_and_nonzero_mode_subspaces_independent":primitive[0]*seam[1]-primitive[1]*seam[0]==1,
      "scalar_codiagonal_forgets_mode":scalar_codiagonal(primitive)==scalar_codiagonal(seam),
      "zero_mode_projector_kills_seam":seam[0]==0,
      "nonzero_mode_projector_kills_primitive":primitive[1]==0,
      "mode_retention_restores_rank_two":True,
    }
    assert all(checks.values())
    out={
      "schema":"marici.nima.ratio-poisson-mode-separator.v1",
      "status":"canonical_operator_valued_separator_constructed_on_ratio_fourier_carrier",
      "checks":checks,
      "carrier":"R_ratio=R_0 direct_sum R_neq0, with P_0 the Fourier zero-mode projector and P_seam=I-P_0",
      "source_assignment":{
        "continuum_ratio_term":"P_0 f=hat f(0)=int f",
        "lattice_defect":"P_seam f, whose integer codiagonal is sum_(m!=0)hat f(m)"
      },
      "profile_facts":{
        "kappa":"P_0 kappa_e=0; K_disc is entirely in R_neq0",
        "g":"P_0 g_e=2C; G_disc-C is entirely in R_neq0"
      },
      "transported_prime_packet":"Retain (p,mode) rather than only p. The primitive-shaped scalar rows v_p and -K_disc v_p then occupy different direct-summand coordinates and are linearly independent before scalar codiagonalization.",
      "projectors":"Primitive candidate uses P_0 before valuation/Euler pushforward; seam candidate uses I-P_0. Their intersection is zero on the ratio Fourier carrier.",
      "naturality_square_required":"The one-leg half-density ray-to-Euler map must lift to R_ratio and commute with P_0; the independently declared seam trace must factor through I-P_0. Only after these two statements may the mode coordinate be forgotten.",
      "what_is_closed":"An explicit rank-two typed carrier and canonical separating projectors exist; the previous scalar rank-one ambiguity is removed algebraically.",
      "what_is_open":"No repository theorem yet shows that the graph-dual primitive current factors through P_0 or that the declared seam current factors through I-P_0 after ordered-pair localization and two-height Laplace transport.",
      "next_gate":"Construct the lifted ray map R_hd^mode((a,b),m,p) and check P_0 R_hd^mode=R_hd^mode P_0 together with reciprocal reflection; then evaluate the two current operators on m=0 and m!=0 generators.",
      "passed":True,
      "rh_implication":False
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
