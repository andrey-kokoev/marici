#!/usr/bin/env python3
"""Audit whether endpoint two-torsion is a module over the Cartan quadric."""

import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/endpoint-torsion-cartan-module.json"


# A nonzero element killed by 2 cannot occur in a module over a ring in which
# 2 is invertible.  This rules out the rational and complex Cartan algebras.
two_invertible_obstruction = {
    "Q": (2 * pow(2, -1)) == 1,
    "C": True,
}

# The only scalar base change retaining the endpoint class is the mod-2 fiber
# C_2 = F_2[x,y,z]/(x^2+y^2+z^2).  In characteristic two its relation is the
# square of the linear form x+y+z.
quadric_values = {}
characters = []
for alpha in product((0, 1), repeat=3):
    ax, ay, az = alpha
    q_value = (ax * ax + ay * ay + az * az) % 2
    linear_value = (ax + ay + az) % 2
    quadric_values[str(alpha)] = {
        "q": q_value,
        "linear_square": (linear_value * linear_value) % 2,
    }
    if q_value == 0:
        characters.append(alpha)

# A rank-one action invariant under all permutations of the three axis labels
# has alpha_x=alpha_y=alpha_z.  The Cartan relation then forces alpha=0.
permutation_invariant = [a for a in characters if a[0] == a[1] == a[2]]

checks = {
    "two_is_invertible_over_Q": two_invertible_obstruction["Q"],
    "two_is_invertible_over_C": two_invertible_obstruction["C"],
    "quadric_becomes_square_mod_two": all(
        row["q"] == row["linear_square"] for row in quadric_values.values()
    ),
    "exactly_four_rank_one_mod_two_characters": len(characters) == 4,
    "only_symmetric_character_is_trivial": permutation_invariant == [(0, 0, 0)],
    # Deliberate hostile witness: the tempting equal nonzero action violates q.
    "equal_nonzero_action_is_rejected": (1, 1, 1) not in characters,
}
assert all(checks.values()), {k: v for k, v in checks.items() if not v}

packet = {
    "schema": "marici.endpoint-torsion-cartan-module.v1",
    "question": (
        "Does the source-derived endpoint two-torsion form a module over the "
        "Cartan quadric algebra?"
    ),
    "cartan_algebra": "Z[x,y,z]/(x^2+y^2+z^2)",
    "rational_or_complex_disposition": (
        "impossible for nonzero two-torsion because 2 is invertible"
    ),
    "integral_disposition": (
        "possible only through the characteristic-two fiber; a source action "
        "has not yet been derived"
    ),
    "special_fiber": "F2[x,y,z]/((x+y+z)^2)",
    "rank_one_characters": [list(a) for a in characters],
    "symmetric_rank_one_characters": [list(a) for a in permutation_invariant],
    "nonalias_frontier": (
        "derive the labelled axis action on the integral endpoint divisor; "
        "without a marked axis only the trivial rank-one action survives"
    ),
    "checks": checks,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(f"PASS {sum(checks.values())}/{len(checks)}")
print("rank-one mod-2 characters", characters)
print("permutation-invariant characters", permutation_invariant)
print(OUT)
