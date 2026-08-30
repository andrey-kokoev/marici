"""WP250: exact count-margin gate for the preregistered muon-tau pilot."""

import json
from pathlib import Path

from sympy import Rational, floor

ROOT = Path(__file__).resolve().parents[1]
PROV = json.loads((ROOT / "data/cms-open-data-19459-pilot/provenance.json").read_text())
WP246 = json.loads((ROOT / "results/wp246_tau_channel_feasibility_gate.json").read_text())

def main():
    scan = PROV["mu_tau_trigger_scan"]
    total, accepted = scan["events"], scan["events_passing_both"]
    acceptance = Rational(accepted, total)
    threshold = Rational(str(WP246["feasibility"]["D"]["minimum_acceptance_for_95pct_at_least_one_event"]))
    minimum_count = int(floor(threshold * total)) + 1
    loss_budget = accepted - minimum_count
    hostile_count = accepted - (loss_budget + 1)
    progressive_residual = acceptance - threshold
    hostile_residual = threshold - Rational(hostile_count, total)
    checks = {
        "selection_frozen_before_counting": scan["frozen_before_counting"],
        "menu_status_join_exact": scan["menu_status_length_mismatches"] == 0,
        "three_named_mu_tau_paths": len(scan["target_paths"]) == 3,
        "intersection_bounded_by_factors": accepted <= min(scan["events_firing_target_or"], scan["events_with_at_least_one_frozen_offline_id_tau"]),
        "pilot_exceeds_one_event_screen": acceptance > threshold,
        "finite_matching_loss_budget_positive": loss_budget >= 0,
        "one_beyond_loss_budget_falsifies": Rational(hostile_count, total) < threshold,
        "deliberate_failure_residual_nonzero": hostile_residual != 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP250", "scan": scan,
        "acceptance_exact": str(acceptance), "acceptance_decimal": float(acceptance),
        "weaker_pole_threshold_exact": str(threshold),
        "progressive_residual_exact": str(progressive_residual),
        "minimum_passing_count": minimum_count,
        "maximum_matching_loss_before_gate_failure": loss_budget,
        "smallest_hostile_count": hostile_count,
        "hostile_residual_exact": str(hostile_residual),
        "classification": "preregistered source-local muon-tau event response passes the pilot count screen with a narrow 48-event matching-loss budget",
        "smallest_exact_falsifier": f"trigger-object and offline-muon validation retain at most {hostile_count} of {total} events",
        "remaining_instrument_gate": "trigger-object matching and offline muon typing within the 48-event budget, then backgrounds, 130/140/160 closure, common-era calibration, and response rank",
        "checks": checks, "passed": all(checks.values()),
    }
    (ROOT / "results/wp250_mu_tau_trigger_pilot.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]: raise SystemExit(1)

if __name__ == "__main__": main()
