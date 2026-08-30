"""Exact selfadjoint Hankel hostile with an off-seam endpoint zero."""

from fractions import Fraction
import json


H = ((Fraction(1), Fraction(2)), (Fraction(2), Fraction(0)))
r = Fraction(-1, 2)
e = (Fraction(1), r)


def matvec(A, x):
    return tuple(sum((row[j] * x[j] for j in range(len(x))), Fraction(0)) for row in A)


He = matvec(H, e)
endpoint = He[0]
determinant = H[0][0] * H[1][1] - H[0][1] * H[1][0]

checks = {
    "hankel_matrix_is_symmetric": H[0][1] == H[1][0],
    "source_coefficients_are_positive": H[0][0] > 0 and H[0][1] > 0,
    "character_ratio_is_nonzero": r != 0,
    "endpoint_matrix_coefficient_vanishes": endpoint == 0,
    "carrier_is_nonzero": determinant != 0,
    "off_seam_modulus": abs(r) != 1,
}

result = {
    "schema": "marici.grothendieck.selfadjoint-hankel-endpoint-hostile.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "H": [[str(x) for x in row] for row in H],
        "r": str(r),
        "H_e": [str(x) for x in He],
        "endpoint": str(endpoint),
        "determinant": str(determinant),
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
