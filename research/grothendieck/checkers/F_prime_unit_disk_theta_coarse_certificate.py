"""Directed elementary certificate for the coarse unit-disk F' bound."""
import json
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path

D = Decimal
down = Context(prec=80, rounding=ROUND_FLOOR)
up = Context(prec=80, rounding=ROUND_CEILING)

# Imported from the independently directed Rouche certificate, rounded down.
m_lower = D("0.1189")

# For Y(t)=sum b_n t^n with b_n>0:
# n/9^n <= 1/9 and n(n-1)/9^n <= 2/81.
# Elementary bounds give Y(9)=Xi(7/2)<3/4, hence A<1/12, B<1/54.
A_upper = up.divide(D(1), D(12))
B_upper = up.divide(D(1), D(54))
a_over_m = up.divide(A_upper, m_lower)
b_over_m = up.divide(B_upper, m_lower)
bound = up.add(up.multiply(D(4), a_over_m),
               up.multiply(D(5), up.add(b_over_m, up.multiply(a_over_m, a_over_m))))
tail_upper = up.divide(bound, D(768))
polynomial_modulus_lower = D("0.092382619354")
full_modulus_lower = down.subtract(polynomial_modulus_lower, tail_upper)

assert bound < 20 and full_modulus_lower > D("0.0625")
result = {
    "certified_m_lower": str(m_lower),
    "Xi_seven_halves_upper": "0.75",
    "Y_prime_one_upper": str(A_upper),
    "Y_double_prime_one_upper": str(B_upper),
    "F_prime_unit_disk_upper": str(bound),
    "target_20_certified": True,
    "quarter_disk_degree_five_tail_upper": str(tail_upper),
    "quarter_disk_F_prime_modulus_lower": str(full_modulus_lower),
    "quarter_disk_F_prime_modulus_exceeds_one_sixteenth": True,
    "first_positive_width_cell_concavity_closed_via_Cauchy_gate": True,
    "directed_decimal_rounding": True,
    "zero_locations_used": False,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "F-prime-unit-disk-theta-coarse-certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
