#!/usr/bin/env python3
"""Finite-field black-box evaluator for the rational chi_12345 trace."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OFPT = ROOT / "research/benincasa/results/five-cycle-ofpt-packet.json"
COVER = ROOT / "research/benincasa/results/five-site-d3-marked-kummer-cover.json"
OUTPUT = ROOT / "research/nima/results/five-site-weight-five-rational-trace.json"

terms = json.loads(OFPT.read_text(encoding="utf-8"))["five_cycle"]["terms"]
facets = json.loads(COVER.read_text(encoding="utf-8"))["facet_forms"]
common = ["G", "g_1", "g_2", "g_3", "g_4", "g_5"]


def inv(a: int, prime: int) -> int:
    return pow(a % prime, prime - 2, prime)


def q_value(label: str, t: int, ys: list[int], prime: int) -> int:
    q = facets[label]
    return (sum(int(a) * t for a in q["x"]) +
            sum(int(a) * y for a, y in zip(q["y"], ys))) % prime


def omega(t: int, ys: list[int], prime: int) -> int | None:
    denominator = 1
    for label in common:
        value = q_value(label, t, ys, prime)
        if value == 0:
            return None
        denominator = denominator * value % prime
    total = 0
    for term in terms:
        product = 1
        for label in term:
            value = q_value(label, t, ys, prime)
            if value == 0:
                return None
            product = product * value % prime
        total = (total + inv(product, prime)) % prime
    return total * inv(denominator, prime) % prime


def radicands(u1: int, u2: int, u3: int, prime: int) -> list[int]:
    f1 = (2*u1*u1 + 2*u2*u2 + u3*u3 - 2*u1*u2 - 2*u2*u3) % prime
    return [f1, (f1-2*u1+1) % prime, (f1-2*u2+2) % prime,
            (f1-2*u3+3) % prime,
            (f1+2*u1+2*u2-8*u3+29) % prime]


def sample(prime: int, seed: int) -> dict:
    roots = {x*x % prime: x for x in range(prime)}
    for offset in range(10000):
        u = [(seed + 3*offset + 2) % prime, (2*seed + 5*offset + 3) % prime,
             (3*seed + 7*offset + 5) % prime]
        fs = radicands(*u, prime)
        if any(value == 0 or value not in roots for value in fs):
            continue
        ys0 = [roots[value] for value in fs]
        t = (11*seed + 13) % prime
        trace = 0
        complete = True
        for mask in range(32):
            ys = [(-y if mask & (1 << i) else y) % prime for i, y in enumerate(ys0)]
            value = omega(t, ys, prime)
            if value is None:
                complete = False
                break
            # chi_12345 is the product of all five sheet signs.
            trace = (trace + (-value if mask.bit_count() & 1 else value)) % prime
        if not complete:
            continue
        y_product = 1
        for y in ys0:
            y_product = y_product * y % prime
        base_value = trace * inv(32 * y_product, prime) % prime

        # Rechoosing any one square root negates both trace and y-product.
        ys1 = ys0.copy()
        ys1[0] = -ys1[0] % prime
        trace1 = 0
        for mask in range(32):
            ys = [(-y if mask & (1 << i) else y) % prime for i, y in enumerate(ys1)]
            value = omega(t, ys, prime)
            assert value is not None
            trace1 = (trace1 + (-value if mask.bit_count() & 1 else value)) % prime
        y_product1 = 1
        for y in ys1:
            y_product1 = y_product1 * y % prime
        base_value1 = trace1 * inv(32 * y_product1, prime) % prime
        assert base_value == base_value1
        return {"prime": prime, "t": t, "u": u, "radicands": fs,
                "base_weight_five_value": base_value,
                "root_choice_invariant": True}
    raise RuntimeError("no nonsingular five-square sample found")


def main() -> None:
    samples = [sample(1009, 1), sample(1013, 2)]
    assert all(row["base_weight_five_value"] != 0 for row in samples)
    out = {
        "schema": "marici.five_site.weight_five_rational_trace.v1",
        "normalization": "(1/32 y1 y2 y3 y4 y5) sum_g chi_12345(g) g*Omega",
        "samples": samples,
        "nonzero_at_all_samples": True,
        "root_choice_invariant_at_all_samples": True,
        "scope": "Black-box rational Fourier component; no de Rham exactness claim.",
        "passed": True,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
