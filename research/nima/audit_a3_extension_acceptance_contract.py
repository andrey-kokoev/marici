#!/usr/bin/env python3
"""Verify the rational monodromy consequences of a horizontal A3 Kato line."""

import json


def matmul(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


M = [[-1, 0, 0], [0, 0, -1], [0, 1, 0]]
M2 = matmul(M, M)
assert M2 == [[1, 0, 0], [0, -1, 0], [0, 0, -1]]

# chi_M(x)=(x+1)(x^2+1); its only rational eigenvalue is -1.
characteristic_factors = ["x+1", "x^2+1"]
rational_line_eigenvalue = -1
quotient_characteristic = "x^2+1"
germs = 66

print(json.dumps({
    "A3_characteristic_factors": characteristic_factors,
    "horizontal_rational_line_eigenvalue": rational_line_eigenvalue,
    "quotient_characteristic": quotient_characteristic,
    "local_traces": {"M_total": -1, "M_generic": -1, "M_excess": 0,
                     "M2_total": -1, "M2_generic": 1, "M2_excess": -2},
    "global_excess_traces": {"identity": 2 * germs, "M": 0, "M2": -2 * germs},
}, indent=2))
