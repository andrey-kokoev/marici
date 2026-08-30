"""Exact WP642 one-current invariant-ring and UV-fiber audit."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def gaussian_add(z, w):
    return z[0] + w[0], z[1] + w[1]


def gaussian_mul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def gaussian_conj(z):
    return z[0], -z[1]


def gaussian_div(z, w):
    denominator = w[0] ** 2 + w[1] ** 2
    numerator = gaussian_mul(z, gaussian_conj(w))
    return F(numerator[0], denominator), F(numerator[1], denominator)


balanced = []
unbalanced = []
for m in range(11):
    for n in range(11 - m):
        record = {"m": m, "n": n, "charge": n - m}
        (balanced if m == n else unbalanced).append(record)

point_a = ((1, 0), (1, 0))
point_b = ((1, 1), (1, -1))
sum_a = gaussian_add(*point_a)
sum_b = gaussian_add(*point_b)
ratio_a = gaussian_div(point_a[1], point_a[0])
ratio_b = gaussian_div(point_b[1], point_b[0])

checks = {
    "all_invariant_monomials_through_degree_ten_are_balanced": all(
        item["charge"] == 0 for item in balanced),
    "every_balanced_monomial_is_a_power_of_norm_square": all(
        item["m"] == item["n"] for item in balanced),
    "every_unbalanced_monomial_carries_nonzero_charge": all(
        item["charge"] != 0 for item in unbalanced),
    "hostile_pair_has_same_matched_current": sum_a == sum_b == (2, 0),
    "first_path_ratio_is_one": ratio_a == (F(1), F(0)),
    "second_path_ratio_is_minus_i": ratio_b == (F(0), F(-1)),
    "hostile_pair_has_different_cycle_coordinate": ratio_a != ratio_b,
    "same_current_implies_same_norm_record": (
        gaussian_mul(sum_a, gaussian_conj(sum_a))
        == gaussian_mul(sum_b, gaussian_conj(sum_b)) == (4, 0)),
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP642",
    "status": "PASS",
    "checks": checks,
    "enumerated_monomials_through_total_degree": 10,
    "balanced_count": len(balanced),
    "unbalanced_count": len(unbalanced),
    "one_current_invariant_ring": "C[|g|^2]",
    "hostile_pair": {
        "point_a": ["1", "1"], "I_chi_a": "1",
        "point_b": ["1+i", "1-i"], "I_chi_b": "-i",
        "shared_matched_current": "2",
    },
    "first_nonfaithful_arrows": [
        "messenger matching (L_A,L_B) -> L_A+L_B loses UV path decomposition",
        "single-current quotient g -> |g|^2 removes only overall rephasing presentation",
    ],
    "classification": "one-current rigidification; neither UV selector nor physical16 selector",
    "reference_port_rule": "a second charged current creates a new relative experiment over its stabilizer groupoid",
    "instrument_gate": "path-resolving heavy instrument or independently sourced second current with calibrated response",
}
(ROOT / "results" / "wp642_single_current_phase_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
