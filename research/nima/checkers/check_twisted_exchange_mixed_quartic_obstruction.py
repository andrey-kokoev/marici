import json
from pathlib import Path


# Exponents encode z1^a zb1^b z2^c zb2^d.
MIXED = (2, 0, 2, 0)


def common_quarter_turn_phase(exponents):
    a, b, c, d = exponents
    return (a - b + c - d) % 4


def cp_conjugate(exponents):
    a, b, c, d = exponents
    return b, a, d, c


# Under T: z1 -> eta z2, z2 -> eta^-1 z1, eta=e^(i*pi/4).
# Return transformed exponents and phase in units of pi/4.
def twisted_exchange(exponents):
    a, b, c, d = exponents
    transformed = (c, d, a, b)
    phase = (a - b - c + d) % 8
    return transformed, phase


assert common_quarter_turn_phase(MIXED) == 0
assert cp_conjugate(MIXED) == (0, 2, 0, 2)
assert twisted_exchange(MIXED) == (MIXED, 0)

# Re(MIXED) is therefore invariant under common D4, CP, and T.
mixed_quartic_allowed = True

# Angular potential:
# lambda*(cos(4 theta1)-cos(4 theta2)) + mu*cos(2(theta1+theta2)).
# On every selected axis-diagonal pair, theta1=m*pi/2 and
# theta2=(2n+1)*pi/4. The anisotropy derivatives vanish, while the mixed
# derivatives equal +/- 2 mu and are nonzero for mu != 0.
selected_pairs = tuple((m, n) for m in range(4) for n in range(4))
gradient_coefficients = {}
for m, n in selected_pairs:
    # sin(2(theta1+theta2)) = sin(m*pi + (2n+1)*pi/2) = +/- 1.
    sign = 1 if (m + n) % 2 == 0 else -1
    gradient = (-2 * sign, -2 * sign)  # coefficient multiplying mu
    gradient_coefficients[f"({m},{n})"] = gradient
    assert gradient != (0, 0)

# Setting mu=0 is not symmetry-protected by the declared group.
result = {
    "schema": "marici.nima.twisted-exchange-mixed-quartic-obstruction.v1",
    "mixed_quartic": "Re(z1^2 z2^2)",
    "common_d4_invariant": True,
    "cp_even": True,
    "twisted_exchange_invariant": True,
    "selected_vacuum_count": len(selected_pairs),
    "selected_vacua_stationary_for_nonzero_mixed_coefficient": 0,
    "gradient_coefficients_times_mu": gradient_coefficients,
    "verdict": "The quarter-twisted exchange permits a renormalizable mixed phase quartic whose nonzero coefficient displaces every proposed axis-diagonal vacuum; setting it to zero lacks symmetry authority."
}

out = Path(__file__).parents[1] / "results" / "twisted-exchange-mixed-quartic-obstruction.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
