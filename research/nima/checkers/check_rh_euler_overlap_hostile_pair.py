from fractions import Fraction
import json
from pathlib import Path


def hostile_multiplier(s):
    return 1 + Fraction(256, 3) * s * (s - 1) * (s - Fraction(1, 2)) ** 2


pre_scalar_germ = {
    "analytic_synthesis": "same-U",
    "primitive_incidence": "same-I1",
    "square_incidence": "same-I2",
    "archimedean_incidence": "same-I-infinity",
    "zero_frequency_incidence": "same-I0",
    "reciprocal_transport": "same-R",
    "cutoff_bonding": "same-bonding",
}
actual_packet_germ = dict(pre_scalar_germ)
hostile_packet_germ = dict(pre_scalar_germ)
assert actual_packet_germ == hostile_packet_germ

for s in [Fraction(-3), Fraction(-1), Fraction(0), Fraction(1, 4), Fraction(2, 5), Fraction(2)]:
    assert hostile_multiplier(1 - s) == hostile_multiplier(s)

for anchor in [Fraction(0), Fraction(1, 2), Fraction(1)]:
    assert hostile_multiplier(anchor) == 1

assert hostile_multiplier(Fraction(1, 4)) == 0
assert hostile_multiplier(Fraction(3, 4)) == 0

# The discriminator is evaluated only at s=2 in the zero-free Euler chamber.
distinguishing_point = Fraction(2)
euler_value = Fraction(5)
actual_section_value = euler_value
hostile_section_value = hostile_multiplier(distinguishing_point) * euler_value
actual_overlap_residual = actual_section_value - euler_value
hostile_overlap_residual = hostile_section_value - euler_value

assert hostile_multiplier(distinguishing_point) == 385
assert actual_overlap_residual == 0
assert hostile_overlap_residual == 1920
assert distinguishing_point not in [Fraction(1, 4), Fraction(3, 4)]

result = {
    "schema": "marici.rh.euler-overlap-hostile-pair.v1",
    "pre_scalar_germ_equal": True,
    "reciprocal_symmetry_preserved": True,
    "anchor_normalizations_preserved": ["0", "1/2", "1"],
    "hostile_divisor_points": ["1/4", "3/4"],
    "distinguishing_point": "2",
    "actual_overlap_residual": str(actual_overlap_residual),
    "hostile_overlap_residual": str(hostile_overlap_residual),
    "discriminator_inspects_hostile_zero": False,
    "verdict": "Euler-theta overlap rejects hostile divisor insertion before zero inspection but does not prove zero confinement",
}

out = Path(__file__).parents[1] / "results" / "rh-euler-overlap-hostile-pair.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
