"""Directed normalized-theta coefficient certificate for the unit-disk F' bound."""
import json
from decimal import Context, Decimal as D, ROUND_CEILING, ROUND_FLOOR
from pathlib import Path


ROOT = Path(__file__).parents[1]
down = Context(prec=90, rounding=ROUND_FLOOR)
up = Context(prec=90, rounding=ROUND_CEILING)


def interval_add(left, right):
    return down.add(left[0], right[0]), up.add(left[1], right[1])


def interval_multiply(left, right):
    lower_candidates = [down.multiply(x, y) for x in left for y in right]
    upper_candidates = [up.multiply(x, y) for x in left for y in right]
    return min(lower_candidates), max(upper_candidates)


jet = json.loads((ROOT / "results" / "central-xi-log-even-series-interval.json").read_text(encoding="utf-8"))
rouche = json.loads((ROOT / "results" / "xi-centered-unit-disk-Rouche-certificate.json").read_text(encoding="utf-8"))
a = [tuple(map(D, box)) for box in jet["ell_prime_coefficient_intervals_through_degree_five"]]

# If C(t)=Y(t)/Y(0)=sum c_n t^n and ell'=Y'/Y=sum a_n t^n,
# then (n+1)c_(n+1)=sum_(k=0)^n a_k c_(n-k).
c = [(D(1), D(1))]
for n in range(6):
    accumulator = (D(0), D(0))
    for k in range(n + 1):
        accumulator = interval_add(accumulator, interval_multiply(a[k], c[n - k]))
    divisor = D(n + 1)
    c.append((down.divide(accumulator[0], divisor), up.divide(accumulator[1], divisor)))

assert all(box[0] > 0 for box in c)

# C(9)=Y(9)/Y(0) < (3/4)/Xi(1/2)_lower.
center_lower = D(rouche["Xi_half_lower_bound"])
C9_upper = up.divide(D("0.75"), center_lower)
first_omitted_degree = 7
power9 = up.power(D(9), first_omitted_degree)
tail_C1_upper = up.divide(C9_upper, power9)
tail_C1_prime_upper = up.divide(up.multiply(D(first_omitted_degree), C9_upper), power9)
tail_C1_double_prime_upper = up.divide(
    up.multiply(D(first_omitted_degree * (first_omitted_degree - 1)), C9_upper),
    power9,
)

C1_upper = D(0)
C1_prime_upper = D(0)
C1_double_prime_upper = D(0)
for n, box in enumerate(c):
    C1_upper = up.add(C1_upper, box[1])
    if n >= 1:
        C1_prime_upper = up.add(C1_prime_upper, up.multiply(D(n), box[1]))
    if n >= 2:
        C1_double_prime_upper = up.add(
            C1_double_prime_upper,
            up.multiply(D(n * (n - 1)), box[1]),
        )
C1_upper = up.add(C1_upper, tail_C1_upper)
C1_prime_upper = up.add(C1_prime_upper, tail_C1_prime_upper)
C1_double_prime_upper = up.add(C1_double_prime_upper, tail_C1_double_prime_upper)

# On |t|<=1, |Y(t)|/Y(0) >= 2-C(1).
normalized_modulus_lower = down.subtract(D(2), C1_upper)
ell_prime_upper = up.divide(C1_prime_upper, normalized_modulus_lower)
ell_double_prime_upper = up.add(
    up.divide(C1_double_prime_upper, normalized_modulus_lower),
    up.multiply(ell_prime_upper, ell_prime_upper),
)
F_prime_upper = up.add(
    up.multiply(D(4), ell_prime_upper),
    up.multiply(D(5), ell_double_prime_upper),
)

# Denominator-aware perturbation around t=0. Put p=C'/C and
# q=C''/C-p^2, so F'=4p+(4t-1)q.
delta_C_upper = down.subtract(C1_upper, D(1))
delta_C_prime_upper = down.subtract(C1_prime_upper, c[1][0])
twice_c2_lower = down.multiply(D(2), c[2][0])
delta_C_double_prime_upper = down.subtract(C1_double_prime_upper, twice_c2_lower)
c1_magnitude_upper = max(abs(c[1][0]), abs(c[1][1]))
twice_c2_magnitude_upper = up.multiply(D(2), max(abs(c[2][0]), abs(c[2][1])))
p_delta_upper = up.divide(
    up.add(delta_C_prime_upper, up.multiply(c1_magnitude_upper, delta_C_upper)),
    normalized_modulus_lower,
)
p_modulus_upper = up.divide(C1_prime_upper, normalized_modulus_lower)
C_double_ratio_delta_upper = up.divide(
    up.add(delta_C_double_prime_upper, up.multiply(twice_c2_magnitude_upper, delta_C_upper)),
    normalized_modulus_lower,
)
q_delta_upper = up.add(
    C_double_ratio_delta_upper,
    up.multiply(p_delta_upper, up.add(p_modulus_upper, c1_magnitude_upper)),
)
q0_magnitude_upper = max(abs(a[1][0]), abs(a[1][1]))
q_modulus_upper = up.add(q0_magnitude_upper, q_delta_upper)
F_prime_variation_from_zero_upper = up.add(
    up.add(up.multiply(D(4), p_delta_upper), q_delta_upper),
    up.multiply(D(4), q_modulus_upper),
)
g0_lower = down.subtract(down.multiply(D(4), a[0][0]), a[1][1])
F_prime_real_part_lower = down.subtract(g0_lower, F_prime_variation_from_zero_upper)

assert normalized_modulus_lower > 0
assert F_prime_upper < D("0.103")
assert F_prime_real_part_lower > D("0.087")

result = {
    "normalized_Y_coefficients_c0_through_c6": [[str(x) for x in box] for box in c],
    "normalized_Y_at_9_upper": str(C9_upper),
    "first_omitted_degree": first_omitted_degree,
    "normalized_C1_tail_upper": str(tail_C1_upper),
    "normalized_C1_prime_tail_upper": str(tail_C1_prime_upper),
    "normalized_C1_double_prime_tail_upper": str(tail_C1_double_prime_upper),
    "normalized_C1_upper": str(C1_upper),
    "normalized_C1_prime_upper": str(C1_prime_upper),
    "normalized_C1_double_prime_upper": str(C1_double_prime_upper),
    "unit_disk_normalized_Y_modulus_lower": str(normalized_modulus_lower),
    "unit_disk_ell_prime_modulus_upper": str(ell_prime_upper),
    "unit_disk_ell_double_prime_modulus_upper": str(ell_double_prime_upper),
    "unit_disk_F_prime_modulus_upper": str(F_prime_upper),
    "unit_disk_p_variation_from_p0_upper": str(p_delta_upper),
    "unit_disk_q_variation_from_q0_upper": str(q_delta_upper),
    "unit_disk_q_modulus_upper": str(q_modulus_upper),
    "unit_disk_F_prime_variation_from_F_prime_zero_upper": str(F_prime_variation_from_zero_upper),
    "F_prime_at_zero_lower": str(g0_lower),
    "unit_disk_F_prime_real_part_lower": str(F_prime_real_part_lower),
    "directed_decimal_rounding": True,
    "theta_coefficient_positivity_used": True,
    "zero_locations_used": False,
    "rh_proved": False,
}


if __name__ == "__main__":
    output = ROOT / "results" / "F-prime-unit-disk-theta-sharp-certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
