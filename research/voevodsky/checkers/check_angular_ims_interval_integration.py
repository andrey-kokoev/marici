from __future__ import annotations

import json
import math

from mpmath import iv


def upper_float(value) -> float:
    return math.nextafter(float(value.b), math.inf)


def l1_upper(cells: int):
    total = iv.mpf([0, 0])
    width = iv.mpf(1) / cells
    c = iv.pi / 2
    for index in range(cells):
        left = iv.mpf(index) / cells
        right = iv.mpf(index + 1) / cells
        t = iv.mpf([left.a, right.b])
        s = 35*t**4 - 84*t**5 + 70*t**6 - 20*t**7
        s1 = 140*t**3 - 420*t**4 + 420*t**5 - 140*t**6
        s2 = 420*t**2 - 1680*t**3 + 2100*t**4 - 840*t**5
        s3 = 840*t - 5040*t**2 + 8400*t**3 - 4200*t**4
        rho3 = -(c**3)*iv.cos(c*s)*(s1**3) - 3*(c**2)*iv.sin(c*s)*s1*s2 + c*iv.cos(c*s)*s3
        total += abs(rho3) * width
    return total


def main() -> None:
    coarse_cells = 8192
    fine_cells = 32768
    coarse = l1_upper(coarse_cells)
    fine = l1_upper(fine_cells)
    coarse_upper = upper_float(coarse)
    fine_upper = upper_float(fine)
    assert fine_upper < coarse_upper
    assert fine_upper < 94.14010122504427

    normalized = fine * 2 / (3 * iv.pi)
    normalized_upper = upper_float(normalized)
    assert normalized_upper < 19.97714993751625
    assert normalized_upper > 9.84825790

    result = {
        "schema": "marici.voevodsky.angular-ims-interval-integration.v1",
        "status": "directed_interval_upper_bound_verified",
        "interval_backend": "mpmath.iv via sympy ephemeral environment",
        "coarse_cells": coarse_cells,
        "coarse_L1_upper": coarse_upper,
        "fine_cells": fine_cells,
        "fine_L1_upper": fine_upper,
        "fine_L1_upper_exact_binary64": fine_upper.hex(),
        "normalized_localization_upper": normalized_upper,
        "normalized_localization_upper_exact_binary64": normalized_upper.hex(),
        "cell_enclosure_covers_full_cell": True,
        "quadrature_discretization_error_required": False,
        "upper_endpoint_conversion": "nextafter(float(interval_upper), +infinity)",
        "prior_analytic_upper": 19.97714993751625,
        "non_directed_scout": 9.84825790,
        "nested_improvement_verified": True,
        "scout_certified": False,
        "next_gate": "recompute source-derived tail cutoff and finite low-block size with this directed constant",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
