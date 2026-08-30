"""WP249: exact trigger-calibrated pilot acceptance gate."""

import json
from pathlib import Path

from sympy import Rational


ROOT = Path(__file__).resolve().parents[1]
PROV = json.loads((ROOT / "data/cms-open-data-19459-pilot/provenance.json").read_text())
WP246 = json.loads((ROOT / "results/wp246_tau_channel_feasibility_gate.json").read_text())


def main():
    scan = PROV["source_local_trigger_scan"]
    acceptance = Rational(scan["events_passing_both"], PROV["pilot_file"]["events"])
    threshold = Rational(str(WP246["feasibility"]["D"]["minimum_acceptance_for_95pct_at_least_one_event"]))
    max_preselection = Rational(str(WP246["feasibility"]["D"]["maximum_full_2016_events_before_selection"]))
    expected = max_preselection * acceptance
    obstruction = threshold - acceptance
    checks = {
        "one_event_menu_hash": scan["events_with_that_hash"] == PROV["pilot_file"]["events"],
        "menu_status_join_exact": scan["menu_status_length_mismatches"] == 0,
        "two_named_double_tau_paths": len(scan["target_paths"]) == 2,
        "intersection_bounded_by_each_factor": scan["events_passing_both"] <= min(scan["events_firing_either_target_path"], scan["events_with_two_offline_id_taus"]),
        "frozen_acceptance_fails_one_event_screen": acceptance < threshold,
        "deliberate_failure_obstruction_nonzero": obstruction != 0,
        "trigger_object_matching_cannot_repair_count": "can only reduce" in scan["scope"],
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP249",
        "trigger_scan": scan,
        "acceptance_exact": str(acceptance),
        "acceptance_decimal": float(acceptance),
        "weaker_pole_one_event_threshold": float(threshold),
        "maximum_weaker_pole_expected_events_at_full_2016_if_transferred": float(expected),
        "true_count_gate_obstruction_exact": str(obstruction),
        "classification": "named source-local 2015 trigger plus offline-ID pilot response; frozen selection fails the weaker-pole count gate",
        "smallest_exact_falsifier": f"{acceptance} < {threshold}",
        "remaining_instrument_gate": "an independently frozen higher-efficiency channel or selection, then 130/140/160 closure, common-era calibration, backgrounds, matching, and response rank",
        "checks": checks,
        "passed": all(checks.values()),
    }
    (ROOT / "results/wp249_tau_trigger_calibrated_pilot.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
