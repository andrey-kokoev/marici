import json
from pathlib import Path

import sympy as sp


R = sp.Rational


def anomalies(fields):
    """fields are (dimension, Dynkin index, hypercharge) for LH Weyl fermions."""
    mixed = sum(index * charge for _, index, charge in fields)
    gravitational = sum(dim * charge for dim, _, charge in fields)
    cubic = sum(dim * charge**3 for dim, _, charge in fields)
    spin_index = sum(index for _, index, _ in fields)
    spinor_count = sum(1 for dim, _, _ in fields if dim == 4)
    return tuple(map(sp.factor, (mixed, gravitational, cubic, spin_index))), spinor_count


base = [(4, R(1, 2), R(-1, 2)), (5, R(1), R(1))]
completion_a = [(4, R(1, 2), R(1, 2)), (5, R(1), R(-1))]
completion_b = [
    (4, R(1, 2), R(-3, 2)),
    (1, R(0), R(0)),
    (1, R(0), R(1)),
    (1, R(0), R(2)),
]

base_anomaly, base_spinors = anomalies(base)
a_anomaly, a_spinors = anomalies(completion_a)
b_anomaly, b_spinors = anomalies(completion_b)

families = 3
c2_g = R(3)
scalar_subtraction = R(1, 3) * (R(1, 2) + R(1))
base_fermion_index = families * base_anomaly[3]
a_fermion_index = base_fermion_index + families * a_anomaly[3]
b_fermion_index = base_fermion_index + families * b_anomaly[3]
b0_a = sp.factor(R(11, 3) * c2_g - R(2, 3) * a_fermion_index - scalar_subtraction)
b0_b = sp.factor(R(11, 3) * c2_g - R(2, 3) * b_fermion_index - scalar_subtraction)

tests = {
    "base_per_family_anomaly_vector_is_exact": base_anomaly[:3] == (R(3, 4), R(3), R(9, 2)),
    "conjugate_completion_cancels_local_anomalies": tuple(base_anomaly[i] + a_anomaly[i] for i in range(3)) == (0, 0, 0),
    "chiral_completion_cancels_local_anomalies": tuple(base_anomaly[i] + b_anomaly[i] for i in range(3)) == (0, 0, 0),
    "conjugate_completion_has_even_global_spinor_parity": families * (base_spinors + a_spinors) % 2 == 0,
    "chiral_completion_has_even_global_spinor_parity": families * (base_spinors + b_spinors) % 2 == 0,
    "completions_are_inequivalent_charge_multisets": sorted(q for _, _, q in completion_a) != sorted(q for _, _, q in completion_b),
    "conjugate_completion_spin_index_is_three_halves": a_anomaly[3] == R(3, 2),
    "chiral_completion_spin_index_is_one_half": b_anomaly[3] == R(1, 2),
    "completion_a_one_loop_coefficient_is_nine_halves": b0_a == R(9, 2),
    "completion_b_one_loop_coefficient_is_thirteen_halves": b0_b == R(13, 2),
    "beta_coefficient_split_is_exactly_two": b0_b - b0_a == R(2),
    "both_completions_are_one_loop_asymptotically_free": b0_a > 0 and b0_b > 0,
    "deliberate_failure_conjugate_coefficient_cannot_equal_chiral_coefficient": sp.factor(b0_a - b0_b) == -2,
}
tests = {name: bool(value) for name, value in tests.items()}

result = {
    "work_package": "WP879",
    "status": "PASS" if all(tests.values()) else "FAIL",
    "summary": {"passed": sum(tests.values()), "total": len(tests), "all_passed": all(tests.values())},
    "tests": tests,
    "base_per_family": ["4_-1/2", "5_+1"],
    "base_anomaly_vector": [str(value) for value in base_anomaly[:3]],
    "completion_a": ["4_+1/2", "5_-1"],
    "completion_b": ["4_-3/2", "1_0", "1_+1", "1_+2"],
    "completed_anomaly_vectors": {"A": ["0", "0", "0"], "B": ["0", "0", "0"]},
    "global_spinor_parity": {"A": "even", "B": "even"},
    "one_loop_spin5_coefficients": {"A": str(b0_a), "B": str(b0_b), "difference_B_minus_A": str(b0_b - b0_a)},
    "classification": "anomaly cancellation and global spinor parity are nonfaithful on the simple-parent matter packet; they do not authorize one beta system",
    "contextual_partition": "the admitted anomaly probe places completions A and B in one class while the one-loop RG probe separates them",
    "smallest_exact_falsifier": "two per-family half-integer-lattice completions cancel identical anomalies but shift the three-family Spin(5) fermion index by 3 and b0 by 2",
    "remaining_source_gate": "derive a spectrum selector from a parent representation, zero-mode index, or locality theorem before solving fixed points",
    "remaining_threshold_gate": "derive masses and decoupling for the selected chiral completion",
    "remaining_instrument_gate": "unchanged: co-moving rank-two calibrated physical16 response",
}

out = Path(__file__).resolve().parents[1] / "results" / "wp879_spin5_anomaly_completion_beta_fiber.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
if not all(tests.values()):
    raise SystemExit(1)

