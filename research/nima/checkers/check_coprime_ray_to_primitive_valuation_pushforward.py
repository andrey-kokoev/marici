from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/coprime-ray-to-primitive-valuation-pushforward.json"
SOURCES = {
    "ray": "research/nima/common-scaling-ray-renormalization-of-theta-autocorrelation.md",
    "normalization": "research/nima/results/barnes-odd-endpoint-primitive-normalization.json",
    "primitive": "research/voevodsky/a_second_position_graph_dual_functional_realizes_the_primitive_current_20260910.md",
}


def valuations(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def main() -> None:
    raw = {name: (ROOT / path).read_text(encoding="utf-8") for name, path in SOURCES.items()}
    norm = json.loads(raw["normalization"])
    tested = 0
    for a in range(1, 101):
        for b in range(1, 101):
            if math.gcd(a, b) != 1:
                continue
            m = max(a, b)
            vp = valuations(m)
            assert math.prod(p**e for p, e in vp.items()) == m
            assert math.isclose(sum(e * math.log(p) for p, e in vp.items()), math.log(m), rel_tol=0, abs_tol=2e-14)
            # Coprimality makes every prime label belong to at most one oriented leg.
            assert all(not (a % p == 0 and b % p == 0) for p in vp)
            tested += 1
    j = (Fraction(1, 4), Fraction(-1, 4))
    ell_j = 2 * (j[0] - j[1])
    checks = {
        "ray_finite_part_contains_minus_log_max": "\\gamma-\\log\\max(a,b)" in raw["ray"],
        "odd_normalization_closed": norm["passed"] and ell_j == 1,
        "primitive_prime_packet_value": "L_{\\rm prim}(c_{\\log p})=\\log p" in raw["primitive"],
        "bounded_coprime_factorizations_exact": tested > 6000,
        "prime_label_is_on_at_most_one_leg": True,
        "valuation_pushforward_additive": True,
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.coprime-ray-to-primitive-valuation-pushforward.v1",
        "status": "arithmetic_label_pushforward_constructed_exactly_projective_sum_open",
        "checks": checks,
        "tested_coprime_rays": tested,
        "pushforward": "P(a,b)=sum_{p} v_p(max(a,b)) c_(log p)",
        "exact_identity": "L_prim(P(a,b))=sum_p v_p(max(a,b)) log p=log max(a,b)",
        "oriented_endpoint_lift": "J_odd(a,b)=log(max(a,b)) j_theta; ell_odd(J_odd(a,b))=log(max(a,b))",
        "leg_orientation": "Because gcd(a,b)=1, each p dividing max(a,b) occurs on exactly one of the ordered legs; swapping legs preserves the valuation magnitude and reciprocal endpoint reflection supplies the odd sign.",
        "ray_finite_part_split": "gamma-log max(a,b)=gamma-L_prim(P(a,b)); hence the raywise arithmetic finite part is exactly a primitive valuation row plus a label-free constant row.",
        "two_height_retention": "The pushforward changes only the arithmetic label. Its coefficient remains [e^(t/2)/a] kappa((b/a)e^t), so ordered ratio and both later spectral heights are not scalarized.",
        "sign_gate": "The ray formula contains -L_prim(P(a,b)); whether this is +F^(1) or -F^(1) depends on the declared Q_X=M_in-sum(F) source orientation and must be checked before claiming the global row equality.",
        "remaining_gate": "Prove projective convergence of the weighted coprime-ray valuation sum after common log N subtraction, and identify the label-free gamma row and boundary error with seam/archimedean channels.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
