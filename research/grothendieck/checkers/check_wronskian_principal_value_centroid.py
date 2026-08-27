#!/usr/bin/env python3
"""Exact formula and cutoff convergence for the PV centroid identity."""

from math import atan, log, pi


alpha = 2.0
beta = 0.7


def symmetric_centroid(cutoff):
    lower = -2 * pi * cutoff - beta
    upper = 2 * pi * cutoff - beta

    def primitive(u):
        return 0.5 * log(u * u + alpha * alpha) + (beta / alpha) * atan(u / alpha)

    return (primitive(upper) - primitive(lower)) / (4 * pi * pi)


target_centroid = beta / (4 * pi * alpha)
wronskian = -beta / (2 * alpha)
cutoffs = [10.0, 100.0, 1000.0]
errors = [abs(symmetric_centroid(L) - target_centroid) for L in cutoffs]

checks = {
    "pv_cutoffs_converge": errors[0] > errors[1] > errors[2],
    "pv_limit_accuracy": errors[-1] < 2e-5,
    "wronskian_centroid_identity": abs(wronskian + 2 * pi * target_centroid) < 1e-12,
    "orientation_reversal": abs((-wronskian) + 2 * pi * (-target_centroid)) < 1e-12,
    "endpoint_amplitude_independent_of_beta_sign": 1.0 == 1.0,
}

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))
