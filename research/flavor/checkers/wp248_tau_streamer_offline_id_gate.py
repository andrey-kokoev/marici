"""WP248: exact arithmetic gate for the repaired tau-ID pilot scan."""

import json
from pathlib import Path

from sympy import Rational


ROOT = Path(__file__).resolve().parents[1]
PROVENANCE = json.loads((ROOT / "data/cms-open-data-19459-pilot/provenance.json").read_text())
WP246 = json.loads((ROOT / "results/wp246_tau_channel_feasibility_gate.json").read_text())


def main():
    scan = PROVENANCE["repaired_streamer_scan"]
    fraction = Rational(scan["events_with_at_least_two_passing_taus"], scan["entries"])
    one_gate = Rational(str(WP246["feasibility"]["D"]["minimum_acceptance_for_95pct_at_least_one_event"]))
    ten_gate = Rational(str(WP246["feasibility"]["D"]["minimum_acceptance_for_ten_expected_events"]))
    lower_residual = fraction - one_gate
    upper_residual = ten_gate - fraction
    checks = {
        "repaired_dictionary_exists_in_probe": scan["shared_object_created"],
        "full_pilot_scanned": scan["entries"] == PROVENANCE["pilot_file"]["events"],
        "one_stable_id_schema": scan["distinct_tau_id_schemas"] == 1,
        "exactly_98_ids_per_tau": scan["tau_id_count_per_tau"] == 98,
        "all_required_ids_frozen": len(scan["frozen_required_ids"]) == 4,
        "offline_two_tau_fraction_exceeds_one_event_screen": fraction > one_gate,
        "offline_two_tau_fraction_fails_ten_event_screen": fraction < ten_gate,
        "deliberate_failure_residuals_nonzero": lower_residual != 0 and upper_residual != 0,
        "trigger_and_layout_validation_still_open": "no trigger" in scan["scope"] and "official-CMSSW" in scan["scope"],
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP248",
        "scan": scan,
        "offline_two_tau_event_fraction_exact": str(fraction),
        "offline_two_tau_event_fraction_decimal": float(fraction),
        "weaker_pole_screen": {
            "one_event_threshold": float(one_gate),
            "ten_event_threshold": float(ten_gate),
        },
        "true_residuals_exact": {
            "above_one_event_gate": str(lower_residual),
            "below_ten_event_gate": str(upper_residual),
        },
        "classification": "file-local executable offline tau-ID response; count-promising but not trigger-calibrated detector acceptance or source identification",
        "smallest_falsifier": "official CMSSW readback disagrees with the repaired dictionary on any tau-ID name or value",
        "remaining_instrument_gate": "official-layout validation, trigger calibration, 130/140/160 response closure, backgrounds, and finite-power rank",
        "checks": checks,
        "passed": all(checks.values()),
    }
    (ROOT / "results/wp248_tau_streamer_offline_id_gate.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
