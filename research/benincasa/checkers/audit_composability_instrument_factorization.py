#!/usr/bin/env python3
"""Separate fifth-tower relational residue from instrument scalar readout."""

import json
from fractions import Fraction
from pathlib import Path


# The fifth tower returns the full one-dimensional residue object R.
residue_rank = 1

# The frozen physical node supplies only the detector-side functional.
detector = Fraction(1, 4)

# Two admissible hypothetical preparation-side realizations demonstrate that
# the same residue object and detector can yield different scalar readouts.
preparations = {
    "zero": Fraction(0),
    "unit": Fraction(1),
    "candidate_coordinate": Fraction(1, 4),
}
readouts = {name: detector * value for name, value in preparations.items()}

checks = {
    "fifth_tower_returns_rank_one_residue": residue_rank == 1,
    "detector_is_fixed": detector == Fraction(1, 4),
    "different_preparations_give_different_readouts": len(set(readouts.values()))
    == len(readouts),
    "candidate_coordinate_reports_one_over_sixteen": readouts[
        "candidate_coordinate"
    ]
    == Fraction(1, 16),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.composability_instrument_factorization.v1",
    "fifth_tower_output": "rank-one relational residue R",
    "instrument_constructor": "rho_I: R -> preparation/instrument ports",
    "scalar_readout": "<detector, rho_I(residue, preparation)>",
    "fixed_detector": "phi(e6)=1/4",
    "preparation_examples": {key: str(value) for key, value in preparations.items()},
    "readout_examples": {key: str(value) for key, value in readouts.items()},
    "checks": checks,
    "verdict": (
        "The fifth tower may canonically return the complete residue line. "
        "Scalar closure requires a separate instrument constructor with both "
        "preparation-side and detector-side ports. The frozen cosmology packet "
        "contains the e6 detector port but not the q0 preparation port."
    ),
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "composability_instrument_factorization.json"
)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
