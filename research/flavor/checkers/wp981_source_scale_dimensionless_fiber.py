#!/usr/bin/env python3
"""Exact checker for the WP981 source-scale dimensionless fiber."""

from fractions import Fraction
import json
from pathlib import Path


def rho(gamma, mu, ms2, mA2):
    return gamma**2 * mu**4 / (ms2 * mA2**5)


def rho_hat(gamma, a, b, c):
    return gamma**2 * a**4 / (b * c**5)


gamma = Fraction(8)
N = Fraction(7, 3)
b = Fraction(1)
c = Fraction(1)
a_low = Fraction(4)
a_high = Fraction(5)
crossing = Fraction(24696)

mu_low = a_low * N
mu_high = a_high * N
ms2 = b * N**2
mA2 = c * N**2

low_direct = N**8 * rho(gamma, mu_low, ms2, mA2)
high_direct = N**8 * rho(gamma, mu_high, ms2, mA2)
low_normalized = rho_hat(gamma, a_low, b, c)
high_normalized = rho_hat(gamma, a_high, b, c)

checks = {
    "normalization_cancels_for_low_packet": low_direct == low_normalized,
    "normalization_cancels_for_high_packet": high_direct == high_normalized,
    "normalized_masses_are_shared": ms2 / N**2 == mA2 / N**2 == 1,
    "low_packet_is_exactly_16384": low_normalized == 16384,
    "high_packet_is_exactly_40000": high_normalized == 40000,
    "normalized_packets_straddle_crossing": low_normalized < crossing < high_normalized,
    "single_scale_does_not_select_dimensionless_ray": low_normalized != high_normalized,
}

result = {
    "schema": "marici.flavor.source-scale-dimensionless-fiber.v1",
    "work_package": "WP981",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "domain": "positive source scale and positive WP977 normalized masses",
    "dimensionless_coordinate": "rho_hat=N^8*(k/q)=gamma^2*a^4/(b*c^5)",
    "shared_data": {
        "gamma": str(gamma),
        "N": str(N),
        "b": str(b),
        "c": str(c),
    },
    "hostile_packets": [
        {"a": str(a_low), "rho_hat": str(low_normalized)},
        {"a": str(a_high), "rho_hat": str(high_normalized)},
    ],
    "crossing": str(crossing),
    "classification": "source scale repairs units but is not a dimensionless coefficient selector",
    "remaining_gate": (
        "derive a source relation that constrains gamma^2*a^4/(b*c^5) "
        "before flavor readout and survives coupled-vacuum and instrument tests"
    ),
}

out = Path("research/flavor/results/wp981_source_scale_dimensionless_fiber.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
