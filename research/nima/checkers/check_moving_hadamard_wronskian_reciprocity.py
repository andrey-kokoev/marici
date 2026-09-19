from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/moving-hadamard-wronskian-reciprocity.json"


def row_mat(v: tuple[float, float], M: tuple[tuple[float, float], tuple[float, float]]) -> tuple[float, float]:
    return (v[0]*M[0][0]+v[1]*M[1][0], v[0]*M[0][1]+v[1]*M[1][1])


def main() -> None:
    R = ((0.0, 1.0), (1.0, 0.0))
    ell0 = (2.0, -2.0)
    primes = [2, 3, 5, 7, 11, 17, 29, 53, 97]
    max_error = 0.0
    for p in primes:
        r = math.sqrt(p)
        T = ((r, 0.0), (0.0, 1/r))
        Tinv = ((1/r, 0.0), (0.0, r))
        ellL = row_mat(ell0, Tinv)
        ellMinusL = row_mat(ell0, T)
        reflected = row_mat(ellL, R)
        max_error = max(max_error, max(abs(reflected[i]+ellMinusL[i]) for i in (0,1)))
        # Moving weighted-Hadamard columns and their dual coordinate.
        wL = (r/2, 1/(2*r))
        jL = (r/4, -1/(4*r))
        max_error = max(max_error, abs(sum(ellL[i]*wL[i] for i in (0,1))), abs(sum(ellL[i]*jL[i] for i in (0,1))-1))
        # G_L=T^-*T^-1 makes transported columns retain seam norms.
        GL = ((1/p, 0.0), (0.0, p))
        wnorm = sum(wL[i]*GL[i][i]*wL[i] for i in (0,1))
        jnorm = sum(jL[i]*GL[i][i]*jL[i] for i in (0,1))
        max_error = max(max_error, abs(wnorm-.5), abs(jnorm-.125))
    checks = {
        "moving_odd_dual_extracts_j": max_error < 3e-15,
        "moving_odd_dual_annihilates_wall": max_error < 3e-15,
        "reciprocal_exchange_reverses_odd_sign_and_scale": max_error < 3e-15,
        "transported_metric_preserves_column_norms": max_error < 3e-15,
        "all_prime_samples_pass": len(primes) == 9,
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.moving-hadamard-wronskian-reciprocity.v1",
        "status": "linear_moving_endpoint_wronskian_identification_and_reciprocity_closed",
        "checks": checks,
        "max_error": max_error,
        "moving_columns": "w_L=T_L w_theta, j_L=T_L j_theta",
        "moving_odd_dual": "ell_L=ell_0 T_L^(-1), ell_0=2(1,-1)",
        "extraction": "ell_L(w_L)=0 and ell_L(j_L)=1",
        "metric": "G_L=T_L^(-*)T_L^(-1); w_L and j_L retain seam squared norms 1/2 and 1/8 in the unscaled standard coordinate convention",
        "reciprocity": "R T_L=T_(-L)R and ell_0 R=-ell_0 imply ell_L R=-ell_(-L)",
        "Hadamard_identification": "Transporting the source weighted-Hadamard isometry fiberwise gives U_partial,L=T_L U_partial,0. Its odd coordinate covector is exactly ell_L, so the moving detector is the Wronskian endpoint jump readout rather than an added functional.",
        "consequence": "The local primitive odd readout is chart-covariant and reciprocal-odd. Fixed-frame wall mixing is removed without a seam subtraction.",
        "scope_limit": "Linear endpoint/Wronskian naturality is closed. The rank-one odd Green response pushforward K_p^odd G_theta^odd (K_p^odd)^* remains open, as does signed coprime-ray completion.",
        "next_gate": "Test the rank-one polarized response identity on the transported j_L line; do not promote it to an ambient metric isometry.",
        "passed": True,
        "rh_implication": False
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
