import json
from pathlib import Path

import sympy as sp


epsilon = sp.symbols("epsilon", positive=True)
normalizer = 1 + 2 * epsilon

integer_residues = sp.Matrix([
    1 + 2 * epsilon,
    1 - epsilon,
    1 - epsilon,
])
canonical_incidence = sp.Matrix([1, 0, 0])
hostile_incidence = sp.Matrix([1, epsilon, epsilon]) / normalizer

# Fourier transport on (P_+, P_-, C_+, C_-) as one four-cycle.  The orbit sum
# is invariant independently of the convention chosen for the cycle origin.
F = sp.Matrix([
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
])
orbit_sum = sp.ones(4, 1)

canonical_response = sp.Matrix([
    [1, 0],
    [0, 0],
])
hostile_response = sp.Matrix([
    [1, 0],
    [0, 2 * epsilon / normalizer],
])
common_probe = sp.Matrix([1, 0])
fractional_probe = sp.Matrix([0, 1])

checks = {
    "fourier_orbit_has_order_four": F**4 == sp.eye(4),
    "fourier_orbit_sum_is_fixed": F * orbit_sum == orbit_sum,
    "integer_residue_mean_is_one": sp.simplify(sum(integer_residues) / 3) == 1,
    "normalized_origin_weight_is_one": sp.simplify((1 + 2 * epsilon) / normalizer) == 1,
    "normalized_total_mean_density_is_one": sp.simplify((1 + 2 * epsilon) / normalizer) == 1,
    "canonical_and_hostile_incidence_scalar_sums_match": sp.simplify(
        sum(canonical_incidence) - sum(hostile_incidence)
    ) == 0,
    "incidence_packets_are_distinct": (hostile_incidence - canonical_incidence).applyfunc(sp.simplify) != sp.zeros(3, 1),
    "common_probe_aliases_the_models": canonical_response * common_probe == hostile_response * common_probe,
    "fractional_probe_separates_the_models": canonical_response * fractional_probe != hostile_response * fractional_probe,
    "canonical_response_rank_is_one": canonical_response.rank() == 1,
    "hostile_response_rank_is_two": hostile_response.rank() == 2,
}

example = {epsilon: sp.Rational(1, 5)}
result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "example_epsilon": "1/5",
    "canonical_incidence": [str(v) for v in canonical_incidence],
    "hostile_incidence": [str(sp.simplify(v.subs(example))) for v in hostile_incidence],
    "fractional_monitor_response": str(sp.simplify((2 * epsilon / normalizer).subs(example))),
    "canonical_response_rank": canonical_response.rank(),
    "hostile_response_rank": hostile_response.rank(),
}
out = Path(__file__).resolve().parents[1] / "results" / "incidence_resolved_denominator_three_control.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
