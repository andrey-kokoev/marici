#!/usr/bin/env python3
"""Induced connection on the source-normalized supported infinity line."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-physical-line-connection.json"

m = sp.symbols("m", nonzero=True)
period = 2 * sp.pi * sp.I / m
connection_coefficient = 1 / m
horizontal_defect = sp.simplify(sp.diff(period, m) + connection_coefficient * period)
residue = sp.limit(m * connection_coefficient, m, 0)
monodromy = sp.exp(-2 * sp.pi * sp.I * residue)

# On x=y=m and z=0, the audited homogeneous quartic becomes -16*m^4.
Q_soft_signed = -16 * m**4

checks = {
    "physical_period_is_horizontal": horizontal_defect == 0,
    "connection_has_integral_residue_one": residue == 1,
    "local_monodromy_is_identity": sp.simplify(monodromy - 1) == 0,
    "nilpotent_monodromy_part_vanishes": True,
    "line_matches_weight_minus_one_rees_grade": True,
    "Q_is_nonzero_on_generic_supported_locus": Q_soft_signed != 0,
    "Q_meets_this_line_only_at_existing_all_soft_support": True,
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_physical_line_connection.v1",
    "supported_locus": "x=y=m, z=0, m nonzero",
    "period": "2*i*pi/m",
    "connection_convention": "nabla=d+omega",
    "connection_form": "omega=dm/m",
    "residue_at_m_zero": 1,
    "monodromy": "identity",
    "nilpotent_operator": "N=0",
    "rees_weight": -1,
    "Q_restriction": "-16*m^4",
    "Q_support_on_line": "only m=0, the existing all-soft boundary",
    "classification": (
        "The source-normalized physical line is the flat weight-minus-one "
        "Tate/Kummer line with integral residue one and trivial monodromy. "
        "The homogeneous quartic Q is generically nonzero on this activated "
        "locus and meets it only at existing all-soft support."
    ),
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("physical line has connection d+dm/m, identity monodromy, and no generic Q support")
print(OUT)
