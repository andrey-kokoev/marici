from fractions import Fraction
import json
from pathlib import Path


def add(left, right):
    return tuple(left[i] + right[i] for i in range(3))


def typed_log_total(packet, weights=(Fraction(1), Fraction(1))):
    primitive, square, tail = packet
    return weights[0] * primitive + weights[1] * square + tail


def mixed_log_total(packet, alpha=Fraction(1)):
    primitive, square, tail = packet
    return primitive + square + tail + alpha * primitive * square


packet_a = (Fraction(2), Fraction(0), Fraction(3))
packet_b = (Fraction(0), Fraction(5), Fraction(7))
combined = add(packet_a, packet_b)

assert typed_log_total(combined) == typed_log_total(packet_a) + typed_log_total(packet_b)
mixed_residual = mixed_log_total(combined) - mixed_log_total(packet_a) - mixed_log_total(packet_b)
assert mixed_residual == 10

# An authorized refinement preserves each typed total.
coarse = (Fraction(4), Fraction(6), Fraction(8))
fine_parts = [(Fraction(1), Fraction(2), Fraction(3)), (Fraction(3), Fraction(4), Fraction(5))]
assert add(fine_parts[0], fine_parts[1]) == coarse
assert sum((typed_log_total(part) for part in fine_parts), Fraction(0)) == typed_log_total(coarse)

# A cutoff-dependent multiplier can remain additive within each cutoff but
# cannot be natural between the coarse and refined presentations.
def cutoff_log_total(packet, cutoff):
    primitive, square, tail = packet
    return cutoff * primitive + square + tail

refinement_residual = (
    sum((cutoff_log_total(part, 2) for part in fine_parts), Fraction(0))
    - cutoff_log_total(coarse, 1)
)
assert refinement_residual == coarse[0]

result = {
    "schema": "marici.rh.anomaly-character-totalization.v1",
    "typed_direct_sum_residual": 0,
    "mixed_term_direct_sum_residual": int(mixed_residual),
    "typed_refinement_residual": 0,
    "cutoff_dependent_refinement_residual": int(refinement_residual),
    "verdict": "global totalization requires two typed monoidal natural anomaly characters",
}

out = Path(__file__).parents[1] / "results" / "rh-anomaly-character-totalization.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
