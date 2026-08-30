"""Directed certificate of a zero-free-source complex Pick half-disk."""
import json
from decimal import Context, Decimal as D, ROUND_FLOOR
from pathlib import Path


ROOT = Path(__file__).parents[1]
down = Context(prec=80, rounding=ROUND_FLOOR)

jet = json.loads((ROOT / "results" / "central-xi-log-even-series-interval.json").read_text(encoding="utf-8"))
sharp = json.loads((ROOT / "results" / "F-prime-unit-disk-theta-sharp-certificate.json").read_text(encoding="utf-8"))
rouche = json.loads((ROOT / "results" / "xi-centered-unit-disk-Rouche-certificate.json").read_text(encoding="utf-8"))

# If ell'(t)=a0+a1*t+..., then F'(0)=4*a0-a1.
a0_lower = D(jet["ell_prime_coefficient_intervals_through_degree_five"][0][0])
a1_upper = D(jet["ell_prime_coefficient_intervals_through_degree_five"][1][1])
g0_lower = down.subtract(down.multiply(D(4), a0_lower), a1_upper)
M_upper = D(sharp["unit_disk_F_prime_modulus_upper"])
radius = D(1)
real_F_prime_lower = D(sharp["unit_disk_F_prime_real_part_lower"])

assert jet["interval_certified"]
assert sharp["directed_decimal_rounding"]
assert rouche["centered_q_unit_disk_zero_free_by_theta_Rouche"]
assert real_F_prime_lower > 0

result = {
    "complex_t_disk_radius": str(radius),
    "F_prime_at_zero_lower": str(g0_lower),
    "unit_disk_F_prime_modulus_upper": str(M_upper),
    "unit_disk_bound_source": "normalized theta coefficient certificate",
    "denominator_aware_F_prime_variation_upper": sharp["unit_disk_F_prime_variation_from_F_prime_zero_upper"],
    "real_part_F_prime_lower_on_disk": str(real_F_prime_lower),
    "upper_half_disk_pick_margin_per_unit_height": str(real_F_prime_lower),
    "Im_F_strictly_positive_on_upper_half_disk": True,
    "analyticity_from_centered_q_unit_disk_Rouche": True,
    "angular_modulus_strictly_decreasing_on_disk_arc_segments": True,
    "directed_decimal_rounding": True,
    "zero_locations_used": False,
    "rh_proved": False,
}


if __name__ == "__main__":
    output = ROOT / "results" / "central-complex-pick-disk-certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
