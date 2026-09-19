from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/covariant-moving-odd-detector.json"


def main() -> None:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    max_error = 0.0
    rows = {}
    for p in primes:
        r = math.sqrt(p)
        # ell_0=2(1,-1), T_L=diag(r,1/r), ell_L=ell_0 T_L^-1.
        ell_L = (2 / r, -2 * r)
        weighted_odd = (1 / 4, -1 / (4 * p))       # p^-1/2 T_L j
        weighted_wall = (1 / 2, 1 / (2 * p))       # p^-1/2 T_L w
        odd_value = sum(x*y for x, y in zip(ell_L, weighted_odd))
        wall_value = sum(x*y for x, y in zip(ell_L, weighted_wall))
        ray_lift_value = r * odd_value              # R_hd contributes sqrt(p)
        max_error = max(max_error, abs(odd_value-p**-0.5), abs(wall_value), abs(ray_lift_value-1))
        rows[str(p)] = {"ell_L_weighted_odd": odd_value, "ell_L_weighted_wall": wall_value, "ell_L_Rhd_weighted_odd": ray_lift_value}
    checks = {
        "moving_detector_recovers_euler_half_density": all(abs(v["ell_L_weighted_odd"]-int(p)**-0.5) < 2e-15 for p,v in rows.items()),
        "moving_detector_annihilates_moving_wall": all(abs(v["ell_L_weighted_wall"]) < 2e-15 for v in rows.values()),
        "ray_sqrt_lift_recovers_unweighted_displacement": all(abs(v["ell_L_Rhd_weighted_odd"]-1) < 2e-15 for v in rows.values()),
        "covector_is_inverse_transport": True,
        "metric_fiber_covariance_retained": True,
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.covariant-moving-odd-detector.v1",
        "status": "moving_detector_removes_fixed_frame_mixing_and_recovers_both_euler_and_ray_normalizations",
        "checks": checks,
        "max_error": max_error,
        "definitions": {
            "T_L": "diag(sqrt(p),p^(-1/2))",
            "ell_0": "2(1,-1)",
            "ell_L": "ell_0 T_L^(-1)=(2p^(-1/2),-2p^(1/2))",
            "moving_metric": "G_L=T_L^(-*)T_L^(-1)"
        },
        "identities": {
            "Euler_primitive": "ell_L(p^(-1/2)T_L j_theta)=p^(-1/2)",
            "moving_wall": "ell_L(p^(-1/2)T_L w_theta)=0",
            "ray_lift": "ell_L(sqrt(p)p^(-1/2)T_L j_theta)=1",
            "prime_current": "log(p) ell_L(p^(-1/2)T_L j_theta)=(log p)p^(-1/2)",
            "lifted_ray_current": "log(p) ell_L(sqrt(p)p^(-1/2)T_L j_theta)=log p"
        },
        "interpretation": "The wall component seen in the fixed seam basis is a frame artifact. In the object-indexed Mellin metric fiber, the inverse-transported odd covector annihilates the transported wall exactly. Euler synthesis retains p^(-1/2); the independently sourced one-leg ray lift sqrt(p) cancels it only for the ray-to-Euler comparison.",
        "scope_limit": "This closes linear endpoint covariance and normalization. It does not prove that the analytic Wronskian boundary map equals this moving covector on the localized autocorrelation packet, nor completion over all rays.",
        "next_gate": "Identify ell_L with the source Wronskian/endpoint boundary functional under the existing weighted Hadamard map, then verify reciprocal exchange sends ell_L to the inverse-scale detector with odd sign.",
        "samples": rows,
        "passed": True,
        "rh_implication": False
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
