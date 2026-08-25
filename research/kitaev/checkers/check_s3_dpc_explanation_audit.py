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

    inversion, inversion_digest = load("s3-controlled-inversion-magic-obstruction.json")
    phase, phase_digest = load("s3-record-phase-magic-obstruction.json")
    mechanism, mechanism_digest = load("s3-dpc-nonlinear-source-mechanism.json")
    intertwining, intertwining_digest = load("s3-dpc-five-rail-intertwining.json")

    assert not inversion["is_product_clifford"]
    assert phase["nonclifford_controlled_powers"] == [1, 2]
    assert all(mechanism["generated_resources"].values())
    assert all(mechanism["hostile_source_mutations_rejected"].values())
    assert not intertwining["complete_frozen_code_lift"]
    assert not intertwining["transversal_hybrid_exchange"]["preserves_code"]
    assert not any(row["preserves_code"] for row in intertwining["transversal_record_phases"][:2])

    result = {
        "schema": "marici.kitaev.s3-dpc-explanation-audit.v1",
        "bounded_replay": {
            "component_checkers": 4,
            "digests": {
                "controlled_inversion_obstruction": inversion_digest,
                "record_phase_obstruction": phase_digest,
                "nonlinear_source_mechanism": mechanism_digest,
                "five_rail_intertwining": intertwining_digest,
            },
        },
        "explanation_chain": [
            "frozen stabilizer invariants exclude the three missing logical controls",
            "independently specified nonlinear occupation/exchange dynamics generates those controls exactly",
            "source deletion or mistiming preserves formal support but destroys exact gate action",
            "raw railwise application fails the frozen-code intertwining test",
            "therefore the logical capability is source-explained while the physical five-rail lift requires a verified factory or code switch",
        ],
        "hard_to_vary": True,
        "not_a_restated_obstruction": True,
        "logical_layer": "proper generative explanation",
        "physical_fault_tolerant_layer": "open constructive problem with an exact frozen-code falsifier",
        "capability_status": {
            "frozen_stabilizer": "Obstructed",
            "logical_nonlinear_source": "Executable",
            "five_rail_nonlinear_extension": "Conditional",
        },
        "smallest_next_theorem": "construct a verified encoded resource injection or code-switch intertwiner and replay its one-fault exRec",
        "verdict": "The DPC is now a proper explanation of the logical D(S3) capability boundary: a source-level nonlinear mechanism generates exactly the operations excluded by stabilizer invariants, and hostile source mutations fail without changing formal support. The same audit falsifies the naive frozen-code lift, so the complete physical compiler remains honestly conditional rather than being inferred from the explanation.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
