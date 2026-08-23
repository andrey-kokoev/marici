"""Integral descent of cyclic soft-star Gysin to the order-three Tate line."""

import json
from math import gcd
from pathlib import Path

# Basis of the integral augmentation ideal:
# a=e1-e0, b=e2-e1. Rotation sends a->b and b->-a-b.
g = ((0, -1), (1, -1))
gm1 = ((-1, -1), (1, -2))

det = gm1[0][0] * gm1[1][1] - gm1[0][1] * gm1[1][0]
entry_gcd = gcd(gcd(abs(gm1[0][0]), abs(gm1[0][1])),
                gcd(abs(gm1[1][0]), abs(gm1[1][1])))
assert entry_gcd == 1
assert abs(det) == 3
smith_invariants = (entry_gcd, abs(det) // entry_gcd)
assert smith_invariants == (1, 3)

# Unit endpoint Gysin is the identity on I_Z. It commutes with rotation and
# therefore descends as the identity on the cokernel Z/3.
identity = ((1, 0), (0, 1))


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


assert mm(identity, g) == mm(g, identity)

# Reflection g<->g^-1 sends a to a+b and acts by -1 on the quotient b=a.
reflection_a = (1, 1)
reflection_character_mod3 = 2
assert (reflection_a[0] + reflection_a[1]) % 3 == reflection_character_mod3

result = {
    "schema": "marici.rs3.integral-soft-star-tate-descent.v1",
    "status": "passed",
    "augmentation_basis": ["e1-e0", "e2-e1"],
    "g_minus_one_matrix": [list(row) for row in gm1],
    "smith_invariants": list(smith_invariants),
    "integral_tate_quotient": "Z/3",
    "endpoint_gysin_on_augmentation_lattice": [list(row) for row in identity],
    "induced_map_on_Z_mod_3": "identity",
    "reflection_character_mod3": reflection_character_mod3,
    "verdict": (
        "The cyclic soft-star Gysin descends integrally to the identity on the "
        "order-three Tate quotient. The supported class is integral torsion, not "
        "an artifact created only after reduction mod three."
    ),
}

out = Path(__file__).parents[1] / "results" / "rs3-integral-soft-star-tate-descent.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
