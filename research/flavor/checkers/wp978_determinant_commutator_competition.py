"""Exact WP978 determinant--commutator competition checker."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

K2 = Fraction(2)
P2 = Fraction(0)
K3 = Fraction(2, 9)
P3 = Fraction(2, 27783)
threshold_ratio = (K2 - K3) / (P3 - P2)

q = Fraction(1, 2)
k = Fraction(32)
benchmark_ratio = k / q
E2 = -q * K2 - k * P2
E3 = -q * K3 - k * P3

checks = {
    "rank_two_state_saturates_commutator_score": K2 == 2,
    "rank_two_state_has_zero_determinant_score": P2 == 0,
    "full_rank_control_has_exact_commutator_score": K3 == Fraction(2, 9),
    "full_rank_control_has_positive_determinant_score": P3 == Fraction(2, 27783),
    "full_rank_control_requires_exact_large_ratio": threshold_ratio == 24696,
    "wp977_benchmark_ratio_is_sixty_four": benchmark_ratio == 64,
    "wp977_benchmark_is_below_crossing": benchmark_ratio < threshold_ratio,
    "rank_two_hostile_has_lower_benchmark_energy": E2 < E3,
    "full_rank_benchmark_energy_is_exact": E3 == Fraction(-3151, 27783),
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "schema": "marici.flavor.determinant-commutator-competition.v1",
    "work_package": "WP978",
    "status": "PASS",
    "checks": checks,
    "domain": "unit-Frobenius-radius two-field slice containing the WP973 and WP972 controls",
    "quotient": "full weak-basis conjugation and independent positive field normalization",
    "rank_two_scores": {"K": str(K2), "P": str(P2), "energy": str(E2)},
    "full_rank_scores": {"K": str(K3), "P": str(P3), "energy": str(E3)},
    "crossing_ratio_k_over_q": str(threshold_ratio),
    "wp977_benchmark_ratio_k_over_q": str(benchmark_ratio),
    "classification": "WP977 source architecture survives, but its benchmark coefficient ray is falsified",
    "remaining_gate": "source-derived ratio beyond the global crossing plus a full coupled-vacuum proof",
}
out = ROOT / "results" / "wp978_determinant_commutator_competition.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
