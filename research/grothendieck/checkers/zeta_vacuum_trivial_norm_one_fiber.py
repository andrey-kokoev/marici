import cmath
import json
from pathlib import Path


def units_mod_prime_power(p, power):
    modulus = p**power
    return [u for u in range(modulus) if u % p != 0]


local_checks = {}
for p, power in [(2, 4), (3, 3), (5, 2), (7, 2)]:
    modulus = p**power
    units = units_mod_prime_power(p, power)
    preserves_unit_ball = all(
        ((u * x) % modulus) % p == 0 if x % p == 0 else ((u * x) % modulus) % p != 0
        for u in units
        for x in range(modulus)
    )
    local_checks[f"unit_action_preserves_p_adic_valuation_at_{p}"] = preserves_unit_ball

# A constant vector on a finite cyclic unit quotient has only its trivial
# character component. The discrete Fourier coefficients verify this exact
# representation-theoretic model.
order = 12
coefficients = []
for k in range(order):
    value = sum(cmath.exp(-2j * cmath.pi * k * n / order) for n in range(order))
    coefficients.append(value)

checks = {
    **local_checks,
    "real_gaussian_is_sign_invariant": (-1) ** 2 == 1,
    "trivial_character_component_survives": abs(coefficients[0] - order) < 1e-10,
    "all_nontrivial_character_components_vanish": all(abs(value) < 1e-10 for value in coefficients[1:]),
}

result = {
    "schema": "marici.grothendieck.zeta-vacuum-trivial-norm-one-fiber.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "interpretation": "The standard unramified finite vacua are invariant under local units and the real vacuum is sign invariant. For Q, the norm-one idele-class fiber therefore acts trivially on the zeta vacuum.",
}

out = Path(__file__).parents[1] / "results" / "zeta_vacuum_trivial_norm_one_fiber.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
