#!/usr/bin/env python3
"""Exact scalar model of the three-sector resolvent incidence."""

from cmath import exp


z = complex(0.4, 0.7)


def packet(alpha, q):
    f = exp(-alpha * q)
    x_plus = f / (alpha - z)
    x_minus = f / (alpha + z)
    K = f / ((alpha - z) * (alpha + z))
    # D acts as multiplication by alpha on this scalar resolvent model.
    return x_plus, K, x_minus


checks = {}
for alpha in (3.0, 5.0):
    for q in (0.0, 0.5, 1.0):
        xp, K, xm = packet(alpha, q)
        checks.setdefault("positive_face", True)
        checks.setdefault("negative_face", True)
        checks.setdefault("coherence_difference", True)
        checks["positive_face"] &= abs((alpha + z) * K - xp) < 1e-12
        checks["negative_face"] &= abs((alpha - z) * K - xm) < 1e-12
        checks["coherence_difference"] &= abs((xm - xp) - (-2 * z * K)) < 1e-12

# A two-sector scalar comparison varies with the source decay rate.
ratio_3 = packet(3.0, 0.0)[2] / packet(3.0, 0.0)[0]
ratio_5 = packet(5.0, 0.0)[2] / packet(5.0, 0.0)[0]
checks["two_sector_comparator_is_source_dependent"] = abs(ratio_3 - ratio_5) > 1e-3

# Endpoint evaluation is the common final cell and preserves coherence.
xp, K, xm = packet(3.0, 0.0)
checks["endpoint_mate"] = abs((xm - xp) - (-2 * z * K)) < 1e-12

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))

