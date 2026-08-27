from __future__ import annotations

import json
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).parents[1]
CONTRACT = ROOT / "contracts" / "path-marker-mate-interferometer-preregistration.v1.json"


def q(value):
    return F(str(value))


def expected_curves(gamma, cosines):
    return {
        "untouched_signal_plus": [F(1, 2) for _ in cosines],
        "conditioned_plus_signal_plus": [(1 + gamma * c) / 2 for c in cosines],
        "conditioned_minus_signal_plus": [(1 - gamma * c) / 2 for c in cosines],
        "coherent_uncompute_signal_plus": [(1 + gamma * c) / 2 for c in cosines],
    }


def make_positive_fixture(contract):
    cosines = [q(value) for value in contract["phase_cosines"]]
    cells = {}
    for gamma_text in contract["environment_overlap_settings"]:
        gamma = q(gamma_text)
        cells[gamma_text] = {
            name: [str(value) for value in curve]
            for name, curve in expected_curves(gamma, cosines).items()
        }
    return {
        "records_present": list(contract["required_records"]),
        "full_outcome_law_retained": True,
        "calibration_epoch_matches": True,
        "minimum_efficiency": "1/2",
        "minimum_effective_trials": contract["minimum_effective_trials_per_primary_proportion"],
        "cells": cells,
        "post_record_change": "0",
        "marker_reset_probability": "1",
    }


def evaluate(contract, fixture):
    tolerance = q(contract["absolute_probability_tolerance"])
    cosines = [q(value) for value in contract["phase_cosines"]]
    gates = {}
    gates["all_required_records_present"] = set(contract["required_records"]).issubset(fixture["records_present"])
    gates["full_outcome_law_retained"] = fixture["full_outcome_law_retained"]
    gates["calibration_epoch_matches"] = fixture["calibration_epoch_matches"]
    gates["efficiency_inverse_bounded"] = q(fixture["minimum_efficiency"]) >= q(contract["calibration"]["minimum_signal_port_efficiency"])
    gates["minimum_effective_trials_met"] = fixture["minimum_effective_trials"] >= contract["minimum_effective_trials_per_primary_proportion"]

    all_primary = True
    totalizes = True
    orthogonal_blocks = True
    residuals = {}
    for gamma_text in contract["environment_overlap_settings"]:
        expected = expected_curves(q(gamma_text), cosines)
        observed = fixture["cells"][gamma_text]
        residuals[gamma_text] = {}
        for name, expected_curve in expected.items():
            observed_curve = [q(value) for value in observed[name]]
            curve_residuals = [abs(left - right) for left, right in zip(observed_curve, expected_curve)]
            residuals[gamma_text][name] = [str(value) for value in curve_residuals]
            all_primary = all_primary and max(curve_residuals) <= tolerance
        plus = [q(value) for value in observed["conditioned_plus_signal_plus"]]
        minus = [q(value) for value in observed["conditioned_minus_signal_plus"]]
        totalizes = totalizes and all(abs((x + y) / 2 - F(1, 2)) <= tolerance for x, y in zip(plus, minus))
        if gamma_text == "0":
            coherent = [q(value) for value in observed["coherent_uncompute_signal_plus"]]
            orthogonal_blocks = orthogonal_blocks and all(abs(value - F(1, 2)) <= tolerance for value in coherent)

    gates["all_primary_laws_within_tolerance"] = all_primary
    gates["conditioned_fibers_totalize"] = totalizes
    gates["post_record_control_is_invariant"] = abs(q(fixture["post_record_change"])) <= tolerance
    gates["coherent_route_resets_marker"] = q(fixture["marker_reset_probability"]) >= 1 - tolerance
    gates["orthogonal_environment_blocks_recovery"] = orthogonal_blocks
    return {"accepted": all(gates.values()), "gates": gates, "residuals": residuals}


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    assert contract["primary_proportion_count"] == (
        len(contract["environment_overlap_settings"])
        * len(contract["phase_samples"])
        * len(contract["primary_estimands_per_environment_phase_cell"])
    ) == 48

    # Exact Chebyshev plus union bound: M/(4*N*epsilon^2).
    m = F(contract["primary_proportion_count"])
    n = F(contract["minimum_effective_trials_per_primary_proportion"])
    epsilon = q(contract["absolute_probability_tolerance"])
    familywise_bound = m / (4 * n * epsilon * epsilon)
    assert familywise_bound == q(contract["familywise_error_upper_bound"]) == F(6, 625)
    assert familywise_bound < F(1, 100)

    positive = make_positive_fixture(contract)
    positive_report = evaluate(contract, positive)
    assert positive_report["accepted"]

    click_only = deepcopy(positive)
    click_only["full_outcome_law_retained"] = False
    click_only["records_present"].remove("signal_no_click")
    click_only["cells"]["1"]["untouched_signal_plus"] = ["2/3", "1/2", "1/3", "1/2"]
    click_only_report = evaluate(contract, click_only)
    assert not click_only_report["accepted"]
    assert not click_only_report["gates"]["full_outcome_law_retained"]
    assert not click_only_report["gates"]["all_required_records_present"]
    assert not click_only_report["gates"]["all_primary_laws_within_tolerance"]

    stale = deepcopy(positive)
    stale["calibration_epoch_matches"] = False
    stale_report = evaluate(contract, stale)
    assert not stale_report["accepted"]
    assert not stale_report["gates"]["calibration_epoch_matches"]

    conditioning_as_actuation = deepcopy(positive)
    conditioning_as_actuation["cells"]["1"]["coherent_uncompute_signal_plus"] = ["1/2"] * 4
    conditioning_report = evaluate(contract, conditioning_as_actuation)
    assert not conditioning_report["accepted"]
    assert not conditioning_report["gates"]["all_primary_laws_within_tolerance"]

    result = {
        "schema": "marici.aspect.path-marker-mate-interferometer-preregistration-check.v1",
        "status": "pass",
        "contract": str(CONTRACT.relative_to(ROOT.parent.parent)).replace("\\", "/"),
        "primary_proportion_count": 48,
        "minimum_effective_trials_per_primary_proportion": int(n),
        "absolute_probability_tolerance": str(epsilon),
        "familywise_error_upper_bound": str(familywise_bound),
        "positive_fixture_accepted": positive_report["accepted"],
        "deliberate_failures": {
            "click_only_projection_rejected": not click_only_report["accepted"],
            "stale_calibration_rejected": not stale_report["accepted"],
            "conditioning_reported_as_actuation_rejected": not conditioning_report["accepted"],
        },
        "positive_gates": positive_report["gates"],
        "claim_boundary": contract["claim_boundary"],
    }
    output = ROOT / "results" / "path_marker_mate_interferometer_preregistration_check.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
