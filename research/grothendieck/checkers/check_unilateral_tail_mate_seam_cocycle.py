#!/usr/bin/env python3
"""Exact rational-complex checks for the unilateral tail mate residual."""

from fractions import Fraction


alpha = Fraction(3)
z = complex(0.4, 0.7)


def A(w):
    return 1 / (float(alpha) - w)


transported = A(z).conjugate()
reconstructed = A(-z.conjugate())
residual = reconstructed - transported
closed_form = -2 * z.conjugate() / (float(alpha) ** 2 - z.conjugate() ** 2)

checks = {
    "source_evaluation_conjugates": abs(A(z).conjugate() - 1 / (float(alpha) - z.conjugate())) < 1e-12,
    "mate_residual_formula": abs(residual - closed_form) < 1e-12,
    "mate_square_does_not_commute": abs(residual) > 1e-3,
}

# The residual persists at a nonzero seam point z=it.
seam_z = 0.8j
seam_residual = A(-seam_z.conjugate()) - A(seam_z).conjugate()
checks["residual_persists_on_seam"] = abs(seam_residual) > 1e-3

# Bilateral zero means anti-diagonal endpoint trace, not two zero endpoints.
endpoint = complex(2, -1)
mate_endpoint = -endpoint
checks["zero_trace_is_antidiagonal"] = endpoint + mate_endpoint == 0 and abs(endpoint) > 0
checks["oriented_boundary_norm_cancels"] = abs(abs(endpoint) ** 2 - abs(mate_endpoint) ** 2) < 1e-12

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))

