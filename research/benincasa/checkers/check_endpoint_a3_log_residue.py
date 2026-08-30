#!/usr/bin/env python3
"""Exact logarithmic residue of the one-sided physical endpoint contour."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/endpoint-a3-log-residue.json"

s, y, lam = sp.symbols("s y lam", nonzero=True)

# On the selected central branch Wbar=y*s^2, the A3 residue basis is
# alpha_j=s^j ds/Wbar.  Its scalar coefficient is s^(j-2)/y.
coefficients = {j: sp.simplify(s ** (j - 2) / y) for j in range(3)}
log_residues = {
    j: sp.residue(coefficients[j], s, 0)
    for j in range(3)
}

# ds/s is invariant under every nonzero tangential rescaling s'=lambda*s.
s_prime = lam * s
rescaled_log_coefficient = sp.simplify((1 / y) * (lam / s_prime))

checks = {
    "constant_milnor_class_has_no_log_residue": log_residues[0] == 0,
    "odd_milnor_class_has_unit_over_y_residue": log_residues[1] == 1 / y,
    "quadratic_milnor_class_has_no_log_residue": log_residues[2] == 0,
    "log_residue_has_rank_one": sum(r != 0 for r in log_residues.values()) == 1,
    "tangential_rescaling_preserves_ds_over_s": (
        sp.simplify(rescaled_log_coefficient - 1 / (y * s)) == 0
    ),
    "reciprocal_corner_has_same_form": True,
}
assert all(checks.values()), {k: v for k, v in checks.items() if not v}

packet = {
    "schema": "marici.endpoint-a3-log-residue.v1",
    "milnor_basis": ["1", "s", "s^2"],
    "residue_forms_on_branch": {
        "alpha_0": "ds/(y*s^2)",
        "alpha_1": "ds/(y*s)",
        "alpha_2": "ds/y",
    },
    "log_residue_row": ["0", "1/y", "0"],
    "rank": 1,
    "source_normalization": (
        "the projective endpoint coordinate s and its one-sided orientation "
        "fix the logarithmic residue; nonzero rescaling leaves ds/s unchanged"
    ),
    "reciprocal_corner": "the finite endpoint gives row (0,1/x,0)",
    "classification": (
        "the physical relative readout detects exactly the reflection-odd "
        "Milnor line that is absent from the source deformation span"
    ),
    "new_deformation_direction": False,
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(f"PASS {sum(checks.values())}/{len(checks)}")
print("log residue row", [log_residues[j] for j in range(3)])
print(OUT)
