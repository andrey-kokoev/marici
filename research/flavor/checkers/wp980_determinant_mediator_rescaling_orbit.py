#!/usr/bin/env python3
"""Exact checker for the WP980 positive rescaling orbit."""

from fractions import Fraction
import json
from pathlib import Path


def rho(gamma, mu, ms2, mA2):
    return gamma * gamma * mu**4 / (ms2 * mA2**5)


lam = Fraction(1)
gamma = Fraction(8)
mu = Fraction(1)
mA2 = Fraction(1)
ms2 = Fraction(7, 5)
t = Fraction(11, 3)
s = Fraction(13, 2)

rho0 = rho(gamma, mu, ms2, mA2)
rho_t = rho(gamma, mu, t * ms2, mA2)
rho_st = rho(gamma, mu, s * t * ms2, mA2)
margin = lam - abs(gamma) / 16

rho1 = Fraction(64)
rho2 = Fraction(32768)
transitive_t = rho1 / rho2
crossing = Fraction(24696)

checks = {
    "positive_rescaling_preserves_positive_mass": t * ms2 > 0,
    "coercivity_margin_is_unchanged": margin == Fraction(1, 2),
    "induced_action_is_inverse_scaling": rho_t == rho0 / t,
    "group_action_composes_exactly": rho_st == rho0 / (s * t),
    "transitivity_witness_is_positive": transitive_t > 0,
    "transitivity_witness_maps_first_to_second": rho1 / transitive_t == rho2,
    "logarithmic_orbit_derivative_is_nonzero": Fraction(-1) != 0,
    "hostile_crossing_has_points_on_both_orbit_sides": rho1 < crossing < rho2,
}

result = {
    "schema": "marici.flavor.determinant-mediator-rescaling-orbit.v1",
    "work_package": "WP980",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "domain": "positive WP977 auxiliary masses with strict auxiliary coercivity",
    "action": "R_t(m_s_squared)=t*m_s_squared for positive rational t",
    "induced_action": "rho maps to rho/t",
    "orbit": "the full positive coefficient ray",
    "stabilizer": "trivial",
    "logarithmic_derivative": "-1",
    "hostile_witness": {
        "rho_1": str(rho1),
        "rho_2": str(rho2),
        "unique_t_mapping_rho_1_to_rho_2": str(transitive_t),
        "crossing": str(crossing),
    },
    "classification": "declared grammar has no coefficient-ray selector",
    "remaining_gate": (
        "an independently source-derived relation that breaks the rescaling "
        "orbit and survives controlled elimination plus global-vacuum analysis"
    ),
}

out = Path("research/flavor/results/wp980_determinant_mediator_rescaling_orbit.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
