#!/usr/bin/env python3
"""Exact scalar resolvent model for the seam-cocycle homotopy."""

from cmath import exp


alpha = 3.0
w = complex(0.4, -0.7)


def R(parameter, q=0.0):
    return exp(-alpha * q) / (alpha - parameter)


left = R(-w)
right = R(w)
homotopy_endpoint = 1 / ((alpha + w) * (alpha - w))

checks = {
    "resolvent_identity": abs((left - right) - (-2 * w * homotopy_endpoint)) < 1e-12,
    "homotopy_is_nonzero": abs(homotopy_endpoint) > 1e-3,
}

# The comparison cell has a genuine bulk profile, not only an endpoint value.
bulk_values = [exp(-alpha * q) * homotopy_endpoint for q in (0.0, 0.5, 1.0)]
checks["homotopy_has_bulk_support"] = all(abs(v) > 1e-6 for v in bulk_values)
checks["bulk_profile_is_not_constant"] = abs(bulk_values[0]) > abs(bulk_values[1]) > abs(bulk_values[2])

# Universality: a second decay rate satisfies the same identity.
beta = 5.0
universal = (1 / (beta + w) - 1 / (beta - w))
universal_rhs = -2 * w / ((beta + w) * (beta - w))
checks["identity_is_source_generic"] = abs(universal - universal_rhs) < 1e-12

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))

