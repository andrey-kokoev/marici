import json
from math import comb
from pathlib import Path

import sympy as sp


def witness(N):
    m = N + 1
    c = [sp.Integer((-1) ** j * comb(m, j)) for j in range(m + 1)]
    cmax = max(abs(value) for value in c)
    B = sp.Integer((N + 2) * (cmax + 1))
    alternating_sum = sum(sp.Integer((-1) ** j) for j in range(m + 1))
    t = -B * alternating_sum / sp.Integer(N + 2)
    baseline = [B + t * sp.Integer((-1) ** j) for j in range(m + 1)]
    plus = [baseline[j] + c[j] for j in range(m + 1)]
    minus = [baseline[j] - c[j] for j in range(m + 1)]
    moments_plus = [sum(plus[j] * sp.Integer(j) ** k for j in range(m + 1)) for k in range(m + 1)]
    moments_minus = [sum(minus[j] * sp.Integer(j) ** k for j in range(m + 1)) for k in range(m + 1)]
    cosine_plus = sum(plus[j] * sp.Integer((-1) ** j) for j in range(m + 1))
    cosine_minus = sum(minus[j] * sp.Integer((-1) ** j) for j in range(m + 1))
    return {
        "N": N,
        "positive_weights": bool(all(value > 0 for value in plus + minus)),
        "matched_moments_through_N": moments_plus[: N + 1] == moments_minus[: N + 1],
        "first_unmatched_moment_is_N_plus_1": moments_plus[N + 1] != moments_minus[N + 1],
        "opposite_cosine_signs_at_pi": bool(cosine_plus > 0 > cosine_minus),
        "cosine_values": [str(cosine_plus), str(cosine_minus)],
    }


witnesses = [witness(N) for N in range(13)]
checks = {
    "all_weights_strictly_positive": all(item["positive_weights"] for item in witnesses),
    "all_declared_moment_towers_match": all(item["matched_moments_through_N"] for item in witnesses),
    "deliberate_failure_appears_at_next_moment": all(item["first_unmatched_moment_is_N_plus_1"] for item in witnesses),
    "all_cosine_readouts_have_opposite_sign": all(item["opposite_cosine_signs_at_pi"] for item in witnesses),
}

result = {
    "schema": "marici.grothendieck.finite_odd_moment_ports_are_unfaithful.v1",
    "construction": "signed (N+1)-st finite difference on support 0,...,N+1 around a positive baseline with zero cosine readout at pi",
    "checks": checks,
    "witnesses": witnesses,
}

assert all(checks.values())
output = Path("research/grothendieck/results/finite_odd_moment_ports_are_unfaithful.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
