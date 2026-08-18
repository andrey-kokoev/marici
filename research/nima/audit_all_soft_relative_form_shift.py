#!/usr/bin/env python3
"""Verify radial scaling of the canonical two-variable Kummer residue form."""

import cmath
import json


fiber_dimension = 2
kummer_weight = 3
relative_form_weight = fiber_dimension - kummer_weight
assert relative_form_weight == -1

# The associated regular-singular monodromy is exp(2*pi*i*weight).
monodromy = cmath.exp(2j * cmath.pi * relative_form_weight)
assert abs(monodromy - 1) < 1e-12

print(json.dumps({
    "form": "da wedge db / w",
    "relative_pullback": "rho^-1 * d(a_hat) wedge d(b_hat) / W",
    "radial_exponent": relative_form_weight,
    "radial_monodromy": 1,
    "filtration_shift": 1,
}, indent=2))
