#!/usr/bin/env python3
"""Verify overlap coherence of the two fiber-chart radial Gysin forms."""

import json


# On U_a: z=b/a, eta_a=a^-1 dz/W_a.
# On U_b: z'=a/b=z^-1, eta_b=-b^-1 dz'/W_b.
# b^-1=a^-1 z^-1, dz'=-z^-2 dz, W_b=z^-3 W_a.
sign = (-1) * (-1)
z_exponent = -1 - 2 + 3
assert sign == 1
assert z_exponent == 0

print(json.dumps({
    "Euler_contraction": "(a*db-b*da)/w",
    "U_a_form": "a^-1*dz/W_a",
    "U_b_form": "-b^-1*dz_prime/W_b",
    "overlap_substitution": {
        "z_prime": "z^-1",
        "dz_prime": "-z^-2*dz",
        "b_inverse": "a^-1*z^-1",
        "W_b": "z^-3*W_a"
    },
    "overlap_ratio_eta_b_over_eta_a": 1,
    "orientation_coherent": True,
}, indent=2))
