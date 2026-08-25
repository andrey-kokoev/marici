#!/usr/bin/env python3
"""Exact audit of the frozen five-face toric constructor prediction."""

from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = ROOT / "research" / "nima" / "results" / "toric_source_closed_constructor.json"


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def main():
    # A minimal faithful W=diag(+1,-1) representation.
    one, zero = Fraction(1), Fraction(0)
    pp = [[one, zero], [zero, zero]]
    pm = [[zero, zero], [zero, one]]
    ident = [[one, zero], [zero, one]]

    source = (K / "toric-source-instrument-and-capability-fiber.md").read_text()
    faults = (K / "wilson-constructor-single-fault-audit.md").read_text()

    gates = {
        "task_projectors_complete": add(pp, pm) == ident,
        "conditional_successors_idempotent": mm(pp, pp) == pp and mm(pm, pm) == pm,
        "repeatability_exact": mm(pp, pm) == [[zero, zero], [zero, zero]],
        "source_gate_word_present": "coherently XOR" in source and "controlled string" in source,
        "pointer_and_record_present": "pointer qubit prepared in `|0>`" in source and "exclusive computational outcomes" in source,
        "reset_or_fresh_replacement_derived": False,
        "reset_absence_acknowledged": "verified cat preparation" in source and "remain open" in source,
        "fault_tolerant_cycle_derived": False,
        "fault_scope_is_strictly_partial": "Excluded locations include preparation faults" in faults,
    }
    assert all(v for k, v in gates.items() if k not in {
        "reset_or_fresh_replacement_derived", "fault_tolerant_cycle_derived"
    })
    assert not gates["reset_or_fresh_replacement_derived"]
    assert not gates["fault_tolerant_cycle_derived"]

    result = {
        "schema": "marici.toric-source-closed-constructor.v1",
        "gates": gates,
        "verdict": {
            "source_derived_repeatable_instrument": True,
            "source_closed_measurement_constructor": False,
            "failure_face": "return",
            "fault_tolerant_recovery_constructor": False,
            "prediction_status": "falsified_at_predeclared_reset_falsifier",
        },
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
