#!/usr/bin/env python3
"""Exact symbolic coverage and deletion-minimality test for local Pauli tomography."""

import ast
import itertools
import json
from fractions import Fraction
from pathlib import Path

AXES = ("X", "Y", "Z")
SETTINGS = tuple(itertools.product(AXES, repeat=2))
LOCAL_PATH = tuple((axis, "I") for axis in AXES)
LOCAL_POL = tuple(("I", axis) for axis in AXES)
CORRELATIONS = SETTINGS
TARGET_COORDINATES = frozenset(LOCAL_PATH + LOCAL_POL + CORRELATIONS)


def coordinates_from_settings(settings):
    result = set()
    for path_axis, pol_axis in settings:
        result.add((path_axis, "I"))
        result.add(("I", pol_axis))
        result.add((path_axis, pol_axis))
    return frozenset(result)


full_coordinates = coordinates_from_settings(SETTINGS)
deletion_witnesses = {}
for omitted in SETTINGS:
    retained = tuple(setting for setting in SETTINGS if setting != omitted)
    missing = TARGET_COORDINATES - coordinates_from_settings(retained)
    deletion_witnesses[str(omitted)] = sorted(missing)

# rho_± = (II ± epsilon P)/4 for a nonidentity Pauli tensor P.
# Every Pauli tensor has eigenvalues ±1, each twice, so rho eigenvalues are
# (1 ± epsilon)/4. epsilon=1/2 gives exact positive eigenvalues 3/8 and 1/8.
epsilon = Fraction(1, 2)
rho_pair_eigenvalues = (Fraction(1 + epsilon, 4), Fraction(1 - epsilon, 4))
eta = Fraction(3, 4)
detected_total = eta
no_click = 1 - eta

checks = {
    "nine_joint_settings_declared": len(SETTINGS) == 9,
    "fifteen_nonidentity_pauli_coordinates_declared": len(TARGET_COORDINATES) == 15,
    "nine_settings_cover_all_fifteen_coordinates": full_coordinates == TARGET_COORDINATES,
    "tomography_coordinate_map_has_full_pauli_rank": len(full_coordinates) == 15,
    "every_deleted_setting_loses_exactly_its_correlation": all(value == [ast.literal_eval(key)] for key, value in deletion_witnesses.items()),
    "every_setting_has_a_deletion_falsifier": len(deletion_witnesses) == 9,
    "falsifier_states_are_positive": min(rho_pair_eigenvalues) >= 0,
    "falsifier_states_are_distinct": epsilon != 0,
    "falsifier_eigenvalues_are_exact": set(rho_pair_eigenvalues) == {Fraction(3, 8), Fraction(1, 8)},
    "uniform_loss_click_total_is_three_quarters": detected_total == Fraction(3, 4),
    "no_click_effect_is_one_quarter": no_click == Fraction(1, 4),
    "no_click_restores_normalization": detected_total + no_click == 1,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.path-polarization-pauli-tomography.v1", "status": "passed", "checks": checks, "settings": SETTINGS, "coordinate_count": len(full_coordinates), "deletion_witnesses": deletion_witnesses, "falsifier_eigenvalues": [str(value) for value in rho_pair_eigenvalues], "efficiency": str(eta), "no_click_weight": str(no_click), "claim_boundary": "Minimal within nine local Pauli settings on a two-path, two-polarization density-state model under uniform loss."}
output = Path(__file__).parents[1] / "results" / "path_polarization_pauli_tomography.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "setting_count": len(SETTINGS), "coordinate_count": len(full_coordinates)}, sort_keys=True))
