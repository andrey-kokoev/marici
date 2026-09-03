#!/usr/bin/env python3
"""Exact spectral-gap certificate for a full fifteen-Pauli uncertainty box."""

import itertools
import json
from fractions import Fraction
from pathlib import Path

PAULI = ("I", "X", "Y", "Z")
COORDINATES = tuple(pair for pair in itertools.product(PAULI, repeat=2) if pair != ("I", "I"))
V = Fraction(4, 5)
DELTA = Fraction(1, 300)
HOSTILE_DELTA = Fraction(1, 50)
CENTER = {coordinate: Fraction(0) for coordinate in COORDINATES}
CENTER[("X", "X")] = V
CENTER[("Y", "Y")] = -V
CENTER[("Z", "Z")] = V
CENTER_MIN_EIGENVALUE = (1 - V) / 4
PERTURBATION_BOUND = len(COORDINATES) * DELTA / 4
CERTIFIED_MARGIN = CENTER_MIN_EIGENVALUE - PERTURBATION_BOUND
HOSTILE_BOUND = len(COORDINATES) * HOSTILE_DELTA / 4
FIDELITY_CENTER = (1 + CENTER[("X", "X")] - CENTER[("Y", "Y")] + CENTER[("Z", "Z")]) / 4
FIDELITY_RADIUS = 3 * DELTA / 4
FIDELITY_LOWER = FIDELITY_CENTER - FIDELITY_RADIUS
intervals = {str(coordinate): [str(CENTER[coordinate] - DELTA), str(CENTER[coordinate] + DELTA)] for coordinate in COORDINATES}

checks = {
    "fifteen_nonidentity_pauli_coordinates": len(COORDINATES) == 15,
    "all_fifteen_coordinates_have_nonzero_width": len(intervals) == 15 and DELTA > 0,
    "werner_center_minimum_eigenvalue_is_exact": CENTER_MIN_EIGENVALUE == Fraction(1, 20),
    "operator_norm_perturbation_bound_is_exact": PERTURBATION_BOUND == Fraction(1, 80),
    "full_box_has_strict_positive_margin": CERTIFIED_MARGIN == Fraction(3, 80) and CERTIFIED_MARGIN > 0,
    "center_fidelity_is_seventeen_twentieths": FIDELITY_CENTER == Fraction(17, 20),
    "full_box_fidelity_lower_bound_is_exact": FIDELITY_LOWER == Fraction(339, 400),
    "full_box_is_uniformly_entangled": FIDELITY_LOWER > Fraction(1, 2),
    "twelve_nuisance_coordinates_are_present": sum(value == 0 for value in CENTER.values()) == 12,
    "hostile_radius_exceeds_center_spectral_gap": HOSTILE_BOUND == Fraction(3, 40) and HOSTILE_BOUND > CENTER_MIN_EIGENVALUE,
    "hostile_radius_fails_this_positivity_certificate": CENTER_MIN_EIGENVALUE - HOSTILE_BOUND < 0,
    "trace_coordinate_is_fixed_outside_box": ("I", "I") not in COORDINATES,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.full-pauli-semidefinite-enclosure.v1", "status": "passed", "checks": checks, "coordinate_count": len(COORDINATES), "coordinate_radius": str(DELTA), "certified_spectral_margin": str(CERTIFIED_MARGIN), "fidelity_lower_bound": str(FIDELITY_LOWER), "hostile_radius": str(HOSTILE_DELTA), "intervals": intervals, "claim_boundary": "Exact spectral-gap enclosure around one Werner-type center; not a general SDP solver."}
output = Path(__file__).parents[1] / "results" / "full_pauli_semidefinite_enclosure.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "coordinate_count": len(COORDINATES), "margin": str(CERTIFIED_MARGIN), "fidelity_lower": str(FIDELITY_LOWER)}, sort_keys=True))
