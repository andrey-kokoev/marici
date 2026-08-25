"""WP251: exact object-coherence and remaining count-budget gate."""

import json
from pathlib import Path

from sympy import Rational, floor

ROOT = Path(__file__).resolve().parents[1]
PROV = json.loads((ROOT / "data/cms-open-data-19459-pilot/provenance.json").read_text())
WP246 = json.loads((ROOT / "results/wp246_tau_channel_feasibility_gate.json").read_text())

def main():
    scan = PROV["mu_tau_object_match_scan"]
    total, accepted = scan["events"], scan["coherent_object_matched_events"]
    threshold = Rational(str(WP246["feasibility"]["D"]["minimum_acceptance_for_95pct_at_least_one_event"]))
    acceptance = Rational(accepted, total)
    minimum = int(floor(threshold * total)) + 1
    margin = accepted - minimum
    hostile = accepted - (margin + 1)
    checks = {
        "object_matching_reduces_parent": accepted < scan["wp250_parent_events"],
        "parent_loss_within_preregistered_budget": scan["wp250_parent_events"] - accepted <= 48,
        "object_coherent_acceptance_passes": acceptance > threshold,
        "remaining_margin_is_23": margin == 23,
        "one_beyond_margin_falsifies": Rational(hostile, total) < threshold,
        "deliberate_failure_residual_nonzero": threshold - Rational(hostile, total) != 0,
        "oddball_zero_coherence_failures_recorded": scan["events_reaching_both_offline_objects_but_failing_object_coherence"] == 0,
    }
    checks = {k: bool(v) for k, v in checks.items()}
    result = {
        "work_package": "WP251", "scan": scan,
        "acceptance_exact": str(acceptance), "acceptance_decimal": float(acceptance),
        "minimum_passing_count": minimum, "remaining_loss_margin": margin,
        "smallest_hostile_count": hostile,
        "hostile_residual_exact": str(threshold - Rational(hostile, total)),
        "classification": "source-local object-coherent physical/readout pilot passes the count screen with a 23-event remaining margin",
        "smallest_exact_falsifier": f"subsequent typing retains at most {hostile} of {total} events",
        "remaining_instrument_gate": "background-calibrated discrimination, 130/140/160 response closure, common-era calibration, and rank-two source response",
        "checks": checks, "passed": all(checks.values()),
    }
    (ROOT / "results/wp251_mu_tau_object_match.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]: raise SystemExit(1)

if __name__ == "__main__": main()
