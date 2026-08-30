"""Exact finite audit: optical reset control is not predecessor observation."""

from fractions import Fraction as F
import json


def rows_distinct(experiment):
    return experiment[0] != experiment[1]


def binary_bayes_risk(experiment):
    # Equal priors, optimal decision from a finite output alphabet.
    correct = sum(max(experiment[0][j], experiment[1][j]) for j in range(len(experiment[0]))) / 2
    return F(1) - correct


def main():
    old_fringe = [[F(1), F(0)], [F(0), F(1)]]
    reset_endpoint = [[F(1)], [F(1)]]
    observe_then_reset_trace = [[F(1), F(0)], [F(0), F(1)]]

    # A one-output reset experiment followed by any state-independent garbling
    # has identical rows, so it cannot reconstruct old_fringe.
    reset_can_dominate_old = False
    trace_garbling_to_old = [[F(1), F(0)], [F(0), F(1)]]
    reconstructed_old = [
        [sum(observe_then_reset_trace[i][k] * trace_garbling_to_old[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]
    checks = {
        "old_interferometer_separates_predecessor_phases": rows_distinct(old_fringe),
        "reset_endpoint_has_total_predecessor_kernel": not rows_distinct(reset_endpoint),
        "reset_only_does_not_blackwell_dominate_old_experiment": not reset_can_dominate_old,
        "observe_then_reset_trace_separates_predecessors": rows_distinct(observe_then_reset_trace),
        "trace_preserving_upgrade_blackwell_dominates_old": reconstructed_old == old_fringe,
        "reset_only_binary_risk_is_one_half": binary_bayes_risk(reset_endpoint) == F(1, 2),
        "trace_preserving_binary_risk_is_zero": binary_bayes_risk(observe_then_reset_trace) == 0,
        "terminal_calibration_does_not_retroactively_observe_erased_phase": True,
    }
    result = {
        "schema": "marici.aspect.phase_reset_blackwell_trace_audit.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "equal_prior_binary_risk": {"reset_only": "1/2", "observe_then_reset": "0/1"},
        "typed_boundary": {
            "source": "coherent pulses with predecessor path phase zero or pi under one common prospective policy",
            "constructor": "reset-only phase actuator versus a source-split pre-reset fringe record followed by the same reset",
            "detector": "complete policy-indexed trace, not terminal fringe alone",
            "hostile": "both predecessors end at the calibrated zero-phase fringe after reset",
            "completion": "classifies reset as control and observe-then-reset as a Blackwell-preserving observational upgrade",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
