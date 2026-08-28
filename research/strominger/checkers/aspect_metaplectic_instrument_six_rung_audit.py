"""Apply Aspect's current falsifier/tower gates to the metaplectic instrument."""

import hashlib
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STROMINGER = ROOT / "strominger"
ASPECT = ROOT / "aspect"
RESULT = STROMINGER / "results" / "aspect_metaplectic_instrument_six_rung_audit.json"


def rank(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    if not rows:
        return 0
    row = 0
    for column in range(len(rows[0])):
        pivot = next((index for index in range(row, len(rows)) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[row], rows[pivot] = rows[pivot], rows[row]
        scale = rows[row][column]
        rows[row] = [value / scale for value in rows[row]]
        for index in range(len(rows)):
            if index == row:
                continue
            factor = rows[index][column]
            rows[index] = [a - factor * b for a, b in zip(rows[index], rows[row])]
        row += 1
    return row


def run(script):
    completed = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True, check=False
    )
    assert completed.returncode == 0, completed.stderr


def main():
    run(STROMINGER / "checkers" / "minimal_metaplectic_sign_instrument_checks.py")
    run(ASPECT / "checkers" / "check_reset_full_falsifier_suite.py")
    run(ASPECT / "checkers" / "check_six_rung_tower.py")

    instrument = json.loads(
        (STROMINGER / "results" / "minimal_metaplectic_sign_instrument_checks.json").read_text()
    )
    aspect_reset = json.loads((ASPECT / "results" / "reset_full_falsifier_suite.json").read_text())
    aspect_six = json.loads((ASPECT / "results" / "six_rung_tower.json").read_text())

    # One terminal blindness alarm sees every missing-capability basis mutation
    # identically. Three component monitors suffice alongside that alarm.
    terminal_observation = [[1, 1, 1, 1]]
    repaired_observation = terminal_observation + [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
    ]
    current_rank = rank(terminal_observation)
    repaired_rank = rank(repaired_observation)

    rungs = {
        "1_formal_realization": {
            "pass": instrument["status"] == "pass",
            "physical": False,
        },
        "2_hostile_deletion_tester": {
            "pass": all(instrument["gates"].values()),
            "single_deletions": 4,
        },
        "3_falsifier_compiler": {
            "pass": current_rank == 4,
            "declared_failure_dimension": 4,
            "diagnostic_rank": current_rank,
            "unresolved_kernel_dimension": 4 - current_rank,
            "minimum_additional_independent_monitors": 3,
            "repaired_rank": repaired_rank,
        },
        "4_ontology_falsifier": {
            "pass": False,
            "relative_declared_carrier_closed": repaired_rank == 4,
            "absolute_ontology_closed": False,
            "fresh_challenges": [
                "correlated_two_port_failure",
                "spectator_grade_leakage",
                "control_phase_drift",
                "context_dependent_branch_swap",
            ],
        },
        "5_admissibility_governor": {
            "pass": False,
            "reason": "no source-authorized physical controller or readout",
        },
        "6_portfolio_controller": {
            "pass": False,
            "reason": "no calibrated apparatus records, costs, or availability contract",
        },
    }
    gates = {
        "aspect_reset_suite_replayed": aspect_reset["status"] == "pass",
        "aspect_six_rung_suite_replayed": aspect_six["status"] == "pass",
        "formal_instrument_passes": rungs["1_formal_realization"]["pass"],
        "deletion_tester_passes": rungs["2_hostile_deletion_tester"]["pass"],
        "terminal_observation_rank_is_one": current_rank == 1,
        "three_dimensional_diagnostic_kernel_exposed": 4 - current_rank == 3,
        "three_additional_monitors_restore_declared_rank": repaired_rank == 4,
        "absolute_ontology_closure_rejected": not rungs["4_ontology_falsifier"]["pass"],
        "physical_admissibility_rejected": not rungs["5_admissibility_governor"]["pass"],
        "apparatus_portfolio_rejected": not rungs["6_portfolio_controller"]["pass"],
    }
    payload = {
        "schema": "marici.strominger.aspect-metaplectic-instrument-six-rung-audit.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "disposition": "formal_detector_admitted_but_diagnostic_and_physical_closure_rejected",
        "rungs": rungs,
        "current_observation_matrix": terminal_observation,
        "minimal_declared_carrier_repair_matrix": repaired_observation,
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
