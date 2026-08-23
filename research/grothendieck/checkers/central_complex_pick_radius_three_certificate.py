"""Directed normalized-theta certificate of Pick positivity on |t|<=3."""
import json
from decimal import Context, Decimal as D, ROUND_CEILING, ROUND_FLOOR
from pathlib import Path


ROOT = Path(__file__).parents[1]
down = Context(prec=90, rounding=ROUND_FLOOR)
up = Context(prec=90, rounding=ROUND_CEILING)

sharp = json.loads((ROOT / "results" / "F-prime-unit-disk-theta-sharp-certificate.json").read_text(encoding="utf-8"))
jet = json.loads((ROOT / "results" / "central-xi-log-even-series-interval.json").read_text(encoding="utf-8"))
c = [tuple(map(D, box)) for box in sharp["normalized_Y_coefficients_c0_through_c6"]]
a = [tuple(map(D, box)) for box in jet["ell_prime_coefficient_intervals_through_degree_five"]]
C9_upper = D(sharp["normalized_Y_at_9_upper"])
radius = D(3)
nine = D(9)


def positive_sum(derivative_order):
    total = D(0)
    start = max(1, derivative_order + 1)
    for n in range(start, 7):
        falling = D(1)
        for j in range(derivative_order):
            falling = up.multiply(falling, D(n - j))
        power = up.power(radius, n - derivative_order)
        total = up.add(total, up.multiply(c[n][1], up.multiply(falling, power)))
    first_omitted = 7
    falling = D(1)
    for j in range(derivative_order):
        falling = up.multiply(falling, D(first_omitted - j))
    tail = up.multiply(
        C9_upper,
        up.divide(up.multiply(falling, up.power(radius, first_omitted - derivative_order)), up.power(nine, first_omitted)),
    )
    return up.add(total, tail), tail


delta_C_upper, tail_C = positive_sum(0)
delta_C_prime_upper, tail_C_prime = positive_sum(1)
delta_C_double_prime_upper, tail_C_double_prime = positive_sum(2)
normalized_modulus_lower = down.subtract(D(1), delta_C_upper)

c1_upper = c[1][1]
twice_c2_upper = up.multiply(D(2), c[2][1])
p_delta_upper = up.divide(
    up.add(delta_C_prime_upper, up.multiply(c1_upper, delta_C_upper)),
    normalized_modulus_lower,
)
p_modulus_upper = up.divide(up.add(c1_upper, delta_C_prime_upper), normalized_modulus_lower)
C_double_ratio_delta_upper = up.divide(
    up.add(delta_C_double_prime_upper, up.multiply(twice_c2_upper, delta_C_upper)),
    normalized_modulus_lower,
)
q_delta_upper = up.add(
    C_double_ratio_delta_upper,
    up.multiply(p_delta_upper, up.add(p_modulus_upper, c1_upper)),
)
q0_upper = max(abs(a[1][0]), abs(a[1][1]))
q_modulus_upper = up.add(q0_upper, q_delta_upper)
F_prime_variation_upper = up.add(
    up.add(up.multiply(D(4), p_delta_upper), q_delta_upper),
    up.multiply(up.multiply(D(4), radius), q_modulus_upper),
)
g0_lower = down.subtract(down.multiply(D(4), a[0][0]), a[1][1])
F_prime_real_lower = down.subtract(g0_lower, F_prime_variation_upper)

# Positivity gives |C(t)-1| <= C(9)-1 < 1 on |t|<=9.
radius_nine_modulus_lower = down.subtract(D(2), C9_upper)

assert radius_nine_modulus_lower > 0
assert normalized_modulus_lower > 0
assert F_prime_real_lower > D("0.014")

result = {
    "complex_t_disk_radius": str(radius),
    "normalized_C_variation_upper": str(delta_C_upper),
    "normalized_C_prime_variation_upper": str(delta_C_prime_upper),
    "normalized_C_double_prime_variation_upper": str(delta_C_double_prime_upper),
    "degree_seven_tail_C_Cprime_Cdoubleprime": [str(tail_C), str(tail_C_prime), str(tail_C_double_prime)],
    "normalized_C_modulus_lower_on_radius_three": str(normalized_modulus_lower),
    "normalized_C_modulus_lower_on_radius_nine": str(radius_nine_modulus_lower),
    "analyticity_radius_from_theta_Rouche": "9",
    "p_variation_upper": str(p_delta_upper),
    "q_variation_upper": str(q_delta_upper),
    "q_modulus_upper": str(q_modulus_upper),
    "F_prime_variation_from_zero_upper": str(F_prime_variation_upper),
    "F_prime_at_zero_lower": str(g0_lower),
    "F_prime_real_part_lower_on_radius_three": str(F_prime_real_lower),
    "upper_half_disk_pick_margin_per_unit_height": str(F_prime_real_lower),
    "Im_F_strictly_positive_on_upper_radius_three_disk": True,
    "directed_decimal_rounding": True,
    "zero_locations_used": False,
    "rh_proved": False,
}


if __name__ == "__main__":
    output = ROOT / "results" / "central-complex-pick-radius-three-certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
