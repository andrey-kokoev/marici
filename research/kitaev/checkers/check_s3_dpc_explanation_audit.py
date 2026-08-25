#!/usr/bin/env python3
"""Consolidate the generative DPC mechanism and its exact physical boundary."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "s3-dpc-explanation-audit.json"


def replay(checker):
    completed = subprocess.run(
        ["uv", "run", "--with", "numpy", "python", str(K / "checkers" / checker)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert completed.returncode == 0, completed.stderr


def load(name):
    path = K / "results" / name
    return json.loads(path.read_text(encoding="utf-8")), hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    replay("check_s3_controlled_inversion_magic_obstruction.py")
    replay("check_s3_record_phase_magic_obstruction.py")
    replay("check_s3_dpc_nonlinear_source_mechanism.py")
    replay("check_s3_dpc_five_rail_intertwining.py")
    replay("check_s3_dpc_source_independence_attack.py")
    replay("check_dpc_universal_law_countermodels.py")

    inversion, inversion_digest = load("s3-controlled-inversion-magic-obstruction.json")
    phase, phase_digest = load("s3-record-phase-magic-obstruction.json")
    mechanism, mechanism_digest = load("s3-dpc-nonlinear-source-mechanism.json")
    intertwining, intertwining_digest = load("s3-dpc-five-rail-intertwining.json")
    attack, attack_digest = load("s3-dpc-source-independence-attack.json")
    universal, universal_digest = load("dpc-universal-law-countermodels.json")

    assert not inversion["is_product_clifford"]
    assert phase["nonclifford_controlled_powers"] == [1, 2]
    assert all(mechanism["generated_resources"].values())
    assert all(mechanism["hostile_source_mutations_rejected"].values())
    assert not intertwining["complete_frozen_code_lift"]
    assert not intertwining["transversal_hybrid_exchange"]["preserves_code"]
    assert not any(row["preserves_code"] for row in intertwining["transversal_record_phases"][:2])
    assert all(attack["attacks_succeeded"].values())
    assert all(universal["countermodels"].values())

    result = {
        "schema": "marici.kitaev.s3-dpc-explanation-audit.v1",
        "bounded_replay": {
            "component_checkers": 6,
            "digests": {
                "controlled_inversion_obstruction": inversion_digest,
                "record_phase_obstruction": phase_digest,
                "nonlinear_source_mechanism": mechanism_digest,
                "five_rail_intertwining": intertwining_digest,
                "source_independence_attack": attack_digest,
                "universal_law_countermodels": universal_digest,
            },
        },
        "explanation_chain": [
            "frozen stabilizer invariants exclude the three missing logical controls",
            "postulated nonlinear occupation/exchange dynamics realizes those controls exactly",
            "the proposed generators are reconstructed spectral logarithms of the target gates",
            "inequivalent source logarithms give identical endpoint operations",
            "the native D(S3) Hamiltonian does not derive the proposed couplers or fitted pulse angles",
            "raw railwise application fails the frozen-code intertwining test",
            "therefore only the conditional realization survives; physical explanation and five-rail execution remain open",
        ],
        "hard_to_vary": False,
        "not_a_restated_obstruction": False,
        "logical_layer": "exact conditional realization, not an independently derived explanation",
        "physical_fault_tolerant_layer": "open constructive problem with an exact frozen-code falsifier",
        "capability_status": {
            "frozen_stabilizer": "Obstructed",
            "logical_nonlinear_source": "Executable",
            "five_rail_nonlinear_extension": "Conditional",
        },
        "source_independence_attack": attack["attacks_succeeded"],
        "universal_law_countermodels": universal["countermodels"],
        "dpc_final_classification": "bounded audit framework, not a universal explanatory law",
        "smallest_next_theorem": "within declared epsilon, time, and resource budgets, derive a gauge-compatible effective interaction from an independently validated D(S3) model and separately certify its recovered encoded channel",
        "verdict": "The first DPC mechanism is an exact conditional logical realization, not a proper source explanation. Its generators are target spectral logarithms, its calibrations are fitted to the desired characters, and the native D(S3) Hamiltonian does not supply the couplers. The stronger universal DPC also fails: finite countermodels show that chronological priority, named-resource necessity, microscopic uniqueness, certificate co-generation, and exact projector intertwining are not necessary for explanation. What survives is a bounded audit framework joining an independently validated physical model, resource-class counterfactuals, and a separate recovered-channel certificate.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
