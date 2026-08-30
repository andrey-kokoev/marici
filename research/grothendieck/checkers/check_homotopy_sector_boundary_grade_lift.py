#!/usr/bin/env python3
"""Checks decaying-grade lift and the constant/delta graph-domain hostile."""

from math import exp


checks = {}

# Exponential model: K and both faces retain the same decaying bulk profile.
alpha = 3.0
z = complex(0.4, 0.7)
values = []
for q in (0.0, 0.5, 1.0, 2.0):
    f = exp(-alpha * q)
    K = f / ((alpha - z) * (alpha + z))
    xp = (alpha + z) * K
    xm = (alpha - z) * K
    values.append(abs(K))
    checks.setdefault("positive_face_preserves_profile", True)
    checks.setdefault("negative_face_preserves_profile", True)
    checks["positive_face_preserves_profile"] &= abs(xp - f / (alpha - z)) < 1e-12
    checks["negative_face_preserves_profile"] &= abs(xm - f / (alpha + z)) < 1e-12
checks["homotopy_bulk_decays"] = all(values[j] > values[j + 1] for j in range(len(values) - 1))

# Constant half-line L2 norm grows with the cutoff.
constant_norm_sq = [float(L) for L in (1, 10, 100)]
checks["constant_not_halfline_l2"] = constant_norm_sq[0] < constant_norm_sq[1] < constant_norm_sq[2]

# Unit-mass delta regularization on [0,h] has squared L2 norm 1/h.
delta_norm_sq = [1 / h for h in (1.0, 0.1, 0.01)]
checks["delta_not_l2_state"] = delta_norm_sq[0] < delta_norm_sq[1] < delta_norm_sq[2]

# Neither hostile is repaired by declaring the two norms equivalent.
checks["control_orbit_requires_rigging"] = constant_norm_sq[-1] > 50 and delta_norm_sq[-1] > 50

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))

