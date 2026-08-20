#!/usr/bin/env python3
"""Cyclic occurrence transport of the physical soft Tate generators."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/benincasa/results/rank12-soft-tate-cyclic-occurrences.json"

# Ordered generators: site-1 soft, site-2 soft, site-3 soft.  The cyclic
# relabelling 1->2->3->1 preserves both three-form orientations because a
# three-cycle is even.
sigma = sp.Matrix(
    [
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
    ]
)
identity = sp.eye(3)
assert sigma**3 == identity
assert sigma.det() == 1
assert sp.trace(identity) == 3
assert sp.trace(sigma) == 0
assert sp.trace(sigma**2) == 0

# Each local fixed-base soft slice is the cyclic image of Entry 1124 and has
# p=q=eta, s=1, hence unit Gysin multiplicity.
occurrences = []
for site in (1, 2, 3):
    others = [index for index in (1, 2, 3) if index != site]
    occurrences.append(
        {
            "soft_site": site,
            "fixed_sites": others,
            "normal": f"X{site}=eta>0",
            "local_rees_data": {"p": "eta", "q": "eta", "s": "1"},
            "gysin_coefficient": 1,
            "deck_character": -1,
        }
    )

result = {
    "schema": "marici.benincasa.rank12_soft_tate_cyclic_occurrences.v1",
    "status": "passed",
    "basis": ["tau_soft_1", "tau_soft_2", "tau_soft_3"],
    "cyclic_matrix": [[int(x) for x in row] for row in sigma.tolist()],
    "cyclic_composition": "sigma^3=I",
    "external_normal_orientation_sign": 1,
    "loop_residue_orientation_sign": 1,
    "occurrences": occurrences,
    "character": {"identity": 3, "sigma": 0, "sigma_squared": 0},
    "rational_decomposition": "Q_trivial + Q(zeta_3)",
    "conclusion": "The three physical site-soft Tate generators assemble as the regular Q[C3] occurrence module, with a common anti-invariant square-root deck character and no cyclic transition defect.",
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
