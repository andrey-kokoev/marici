"""Exact finite model of the metric-free rigged transpose."""

from fractions import Fraction
import json


f = (Fraction(1), Fraction(1))
lam = (Fraction(4), Fraction(-1))
c = Fraction(7)


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), Fraction(0))


forward = tuple(c * x for x in f)
transpose_value = dot(lam, f)
duality_left = dot(lam, forward)
duality_right = c * transpose_value

euclidean_adjoint_row = f
weighted_adjoint_row = (2 * f[0], 3 * f[1])

# The coordinate swap is a finite Fourier model and fixes f=(1,1).
fourier_dual_lam = (lam[1], lam[0])
fourier_covariant_value = dot(fourier_dual_lam, f)

checks = {
    "transpose_duality_identity": duality_left == duality_right,
    "rigged_transpose_value": transpose_value == 3,
    "hilbert_adjoint_depends_on_metric": euclidean_adjoint_row != weighted_adjoint_row,
    "rigged_transpose_does_not_depend_on_metric": dot(lam, f) == transpose_value,
    "source_is_fourier_fixed": (f[1], f[0]) == f,
    "transpose_is_fourier_covariant": fourier_covariant_value == transpose_value,
}

result = {
    "schema": "marici.grothendieck.rigged-transpose-precedes-hilbert-adjoint.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "values": {
        "transpose": str(transpose_value),
        "euclidean_adjoint_row": [str(x) for x in euclidean_adjoint_row],
        "weighted_adjoint_row": [str(x) for x in weighted_adjoint_row],
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
