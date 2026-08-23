"""Directed elementary-anchor certificate of Pick positivity on |t|<=7."""
import json
from decimal import Context, Decimal as D, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).parents[1]
down = Context(prec=90, rounding=ROUND_FLOOR)
up = Context(prec=90, rounding=ROUND_CEILING)
sharp = json.loads((ROOT / "results" / "F-prime-unit-disk-theta-sharp-certificate.json").read_text(encoding="utf-8"))
jet = json.loads((ROOT / "results" / "central-xi-log-even-series-interval.json").read_text(encoding="utf-8"))
rouche = json.loads((ROOT / "results" / "xi-centered-unit-disk-Rouche-certificate.json").read_text(encoding="utf-8"))
c = [tuple(map(D, box)) for box in sharp["normalized_Y_coefficients_c0_through_c6"]]
a = [tuple(map(D, box)) for box in jet["ell_prime_coefficient_intervals_through_degree_five"]]

# At t=25, s=11/2. Elementary bounds:
# pi^(-11/4)<1/20, Gamma(11/4)<63/32, zeta(11/2)<21/20.
xi_eleven_halves_upper = Q(99, 8) * Q(1, 20) * Q(63, 32) * Q(21, 20)
center_lower = D(rouche["Xi_half_lower_bound"])
C25_upper = up.divide(D(xi_eleven_halves_upper.numerator) / D(xi_eleven_halves_upper.denominator), center_lower)
assert C25_upper < D(3)
anchor_upper = D(3)
anchor_radius = D(25)
radius = D(7)


def variation(derivative_order):
    total = D(0)
    for n in range(max(1, derivative_order + 1), 7):
        falling = D(1)
        for j in range(derivative_order):
            falling = up.multiply(falling, D(n - j))
        total = up.add(total, up.multiply(c[n][1], up.multiply(falling, up.power(radius, n - derivative_order))))
    first = 7
    falling = D(1)
    for j in range(derivative_order):
        falling = up.multiply(falling, D(first - j))
    tail = up.divide(
        up.multiply(anchor_upper, up.multiply(falling, up.power(radius, first - derivative_order))),
        up.power(anchor_radius, first),
    )
    return up.add(total, tail), tail


delta_C, tail_C = variation(0)
delta_C_prime, tail_C_prime = variation(1)
delta_C_double, tail_C_double = variation(2)
denominator_lower = down.subtract(D(1), delta_C)
c1_upper = c[1][1]
twice_c2_upper = up.multiply(D(2), c[2][1])
p_delta = up.divide(up.add(delta_C_prime, up.multiply(c1_upper, delta_C)), denominator_lower)
p_upper = up.divide(up.add(c1_upper, delta_C_prime), denominator_lower)
C_double_ratio_delta = up.divide(
    up.add(delta_C_double, up.multiply(twice_c2_upper, delta_C)), denominator_lower
)
q_delta = up.add(C_double_ratio_delta, up.multiply(p_delta, up.add(p_upper, c1_upper)))
q0_upper = max(abs(a[1][0]), abs(a[1][1]))
q_upper = up.add(q0_upper, q_delta)
F_prime_variation = up.add(
    up.add(up.multiply(D(4), p_delta), q_delta),
    up.multiply(up.multiply(D(4), radius), q_upper),
)
g0_lower = down.subtract(down.multiply(D(4), a[0][0]), a[1][1])
F_prime_real_lower = down.subtract(g0_lower, F_prime_variation)

analytic_radius_nine_lower = D(sharp["unit_disk_normalized_Y_modulus_lower"])
# The actual radius-nine lower bound is 2-C(9), not the unit-disk value.
analytic_radius_nine_lower = down.subtract(D(2), D(sharp["normalized_Y_at_9_upper"]))

assert analytic_radius_nine_lower > 0
assert denominator_lower > 0
assert F_prime_real_lower > D("0.017")

result = {
    "elementary_Xi_eleven_halves_upper": str(xi_eleven_halves_upper),
    "normalized_C25_upper": str(C25_upper),
    "tail_anchor_used": "C(25)<3",
    "complex_t_disk_radius": str(radius),
    "degree_seven_tail_C_Cprime_Cdoubleprime": [str(tail_C), str(tail_C_prime), str(tail_C_double)],
    "normalized_C_modulus_lower_on_radius_seven": str(denominator_lower),
    "normalized_C_modulus_lower_on_radius_nine": str(analytic_radius_nine_lower),
    "F_prime_variation_from_zero_upper": str(F_prime_variation),
    "F_prime_at_zero_lower": str(g0_lower),
    "F_prime_real_part_lower_on_radius_seven": str(F_prime_real_lower),
    "upper_half_disk_pick_margin_per_unit_height": str(F_prime_real_lower),
    "Im_F_strictly_positive_on_upper_radius_seven_disk": True,
    "directed_decimal_rounding": True,
    "zero_locations_used": False,
    "rh_proved": False,
}


if __name__ == "__main__":
    output = ROOT / "results" / "central-complex-pick-radius-seven-certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
