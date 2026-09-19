from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/transported-primitive-endpoint-mixing.json"


def main() -> None:
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    rows = {}
    for p in primes:
        # p^-1/2 T_log(p) j_theta = (1/4,-1/(4p)).
        x0, x1 = Fraction(1, 4), Fraction(-1, 4 * p)
        # x=alpha*w_theta+beta*j_theta, w=(1/2,1/2), j=(1/4,-1/4).
        alpha = x0 + x1
        beta = 2 * (x0 - x1)
        assert alpha * Fraction(1, 2) + beta * Fraction(1, 4) == x0
        assert alpha * Fraction(1, 2) - beta * Fraction(1, 4) == x1
        rows[str(p)] = {"endpoint": [str(x0), str(x1)], "wall_alpha": str(alpha), "odd_beta": str(beta)}
    checks = {
        "transported_first_coordinate_constant": all(v["endpoint"][0] == "1/4" for v in rows.values()),
        "reciprocal_coordinate_is_minus_one_over_4p": all(v["endpoint"][1] == f"-1/{4*int(p)}" for p, v in rows.items()),
        "wall_component_nonzero": all(v["wall_alpha"] != "0" for v in rows.values()),
        "odd_coefficient_not_one": all(v["odd_beta"] != "1" for v in rows.values()),
        "exact_reconstruction": True,
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.transported-primitive-endpoint-mixing.v1",
        "status": "one_leg_half_density_transport_mixes_wall_and_odd_endpoint_channels",
        "checks": checks,
        "input_column": "j_theta=(1/4,-1/4)",
        "transport": "p^(-1/2) T_log(p)=diag(1,p^(-1))",
        "transported_column": "(1/4,-1/(4p))",
        "parity_decomposition": "p^(-1/2)T_log(p)j_theta=((1-p^(-1))/4)w_theta+((1+p^(-1))/2)j_theta",
        "odd_detector_value": "ell_odd=2(x0-x1)=(1+p^(-1))/2, not 1",
        "wall_detector_value": "the even/wall coefficient is (1-p^(-1))/4, nonzero for every prime",
        "consequence": "The finite pair-shell sqrt(p) repair is natural, but after Euler weighting it does not land in the fixed pure odd endpoint line. A prime-dependent even component is forced and must be assigned to the seam/wall channel before the primitive row can equal L_prim.",
        "correction": "The earlier formula ell_odd((log p)j_theta)=log p applies in the seam frame only. It cannot be transported to prime scale while keeping j_theta fixed.",
        "samples": rows,
        "next_gate": "Construct the covariant moving odd detector in the metric fiber G_log(p), or subtract the source-authorized wall component through the seam current; compare both choices with the declared fixed primitive Euler row.",
        "passed": True,
        "rh_implication": False
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
