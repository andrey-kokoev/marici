"""Exact rational audit of the completed Mellin exponent bookkeeping."""
import json
from fractions import Fraction as Q
from pathlib import Path


# w=1/2+z and x=e^(2u).  The Haar-form exponent is x^(w/2-1/4) dx/x.
haar_exponent = (Q(1, 2), Q(-1, 4))  # coefficient of w, constant

# Multiplication by the two powers in G followed by dx/x gives ordinary
# Mellin exponents s-1.
first_s = (haar_exponent[0], haar_exponent[1] + Q(9, 4))
second_s = (haar_exponent[0], haar_exponent[1] + Q(5, 4))
assert first_s == (Q(1, 2), Q(2))
assert second_s == (Q(1, 2), Q(1))

# Both theta derivative terms produce zeta(w).
first_zeta_argument = (2 * first_s[0], 2 * first_s[1] - 4)
second_zeta_argument = (2 * second_s[0], 2 * second_s[1] - 2)
assert first_zeta_argument == (Q(1), Q(0))
assert second_zeta_argument == (Q(1), Q(0))

# Under x -> 1/x, the ordinary dx exponent transforms A -> -A-2.
# For the combined modular G, w/2-5/4 becomes -w/2-3/4, which is
# exactly (1-w)/2-5/4.
ordinary_exponent = (Q(1, 2), Q(-5, 4))
inverted = (-ordinary_exponent[0], -ordinary_exponent[1] - 2)
reflected = (Q(-1, 2), Q(1, 2) - Q(5, 4))
assert inverted == reflected == (Q(-1, 2), Q(-3, 4))

result = {
    "haar_power_x": "w/2-1/4",
    "ordinary_dx_power_x": "w/2-5/4",
    "first_gamma_argument": "w/2+2",
    "second_gamma_argument": "w/2+1",
    "both_zeta_arguments": "w",
    "inversion_maps_w_to_1_minus_w": True,
    "saddle_equation": "x*G_prime(x)/G(x)=-z/2",
    "exact_rational_arithmetic": True,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-completed-mellin-affine-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

