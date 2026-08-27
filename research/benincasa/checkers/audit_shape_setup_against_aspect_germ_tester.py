#!/usr/bin/env python3
"""Test the physical shape setup against Aspect's current germ hostiles."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


six = load("research/benincasa/results/relative-shape-six-term-jet.json")
pole = load("research/benincasa/results/relative-shape-pole-depth.json")
pair = load("research/benincasa/results/shape-wall-pairwise-coherence.json")
ternary = load("research/benincasa/results/shape-wall-ternary-circuits.json")
costalk = load("research/benincasa/results/shape-branch-mixed-costalk.json")
physical = load("research/benincasa/results/shape-costalk-physical-incidence.json")
obstruction = load("research/benincasa/results/shape-logarithmic-lowering-obstruction.json")
conductor = load("research/benincasa/results/shape-conductor-correction.json")

gates = {
    "full_fiber_gate": {
        "status": "pass",
        "evidence": "nonzero coefficient costalk and zero literal physical selector remain distinct",
        "value": costalk["anti_invariant_branch_costalk_value"] == "17/3" and physical["literal_physical_pairing"] == 0,
    },
    "native_arity_gate": {
        "status": "pass",
        "evidence": "all six source occurrences and the complete three-wall branch germ are retained",
        "value": six["native_arity"] == 6 and ternary["triple_count"] == 84,
    },
    "authority_gate": {
        "status": "pass",
        "evidence": "literal cycle gives zero; no analytic continuation is inferred",
        "value": not physical["analytic_continuation_to_costalk_constructed"],
    },
    "coherence_preservation_gate": {
        "status": "pass",
        "evidence": "the two square-root sheets and anti-invariant deck character are retained",
        "value": costalk["deck_character"] == -1 and costalk["normalized_sheet_values"] == ["-17/6", "17/6"],
    },
    "order_reversal_gate": {
        "status": "pass_with_koszul_sign",
        "evidence": "constant dual normals commute; reversing two codimension-one residues changes only the required orientation sign",
        "value": pair["all_checks_pass"] and pair["transverse_pair_count"] == 33,
    },
    "higher_depth_history_gate": {
        "status": "open",
        "evidence": "only associated-grade symbols are compiled; the complete triangular lowering homotopy is absent",
        "value": not pole["filtered_lowering_homotopy_constructed"],
    },
    "operation_insertion_gate": {
        "status": "fail_regular_lowering_with_supported_obstruction",
        "evidence": "A1 nondegeneracy forbids the regular lowering; the normalization-conductor sequence records its nonzero supported obstruction",
        "value": obstruction["all_checks_pass"] and conductor["supported_correction_constructed"] and not conductor["descends_to_nodal_branch"],
    },
}

assert all(gate["value"] for gate in gates.values()), gates
packet = {
    "schema": "marici.shape-setup-aspect-germ-tester.v1",
    "gates": gates,
    "passed": [name for name, gate in gates.items() if gate["status"].startswith("pass")],
    "open": [name for name, gate in gates.items() if gate["status"] == "open"],
    "failed": [name for name, gate in gates.items() if gate["status"].startswith("fail")],
    "verdict": "coefficient costalk theorem survives; regular physical lowering functor is obstructed",
    "prohibited_inference": "use the local lowering calculation as an authorized physical readout map",
    "next_falsifier": "test whether any source relative cycle has a nonzero map into the conductor line; the literal chamber map is zero",
}
out = ROOT / "research/benincasa/results/shape-setup-aspect-germ-tester.json"
out.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("PASS expected gate disposition")
print("passed:", ", ".join(packet["passed"]))
print("open:", ", ".join(packet["open"]))
print("failed:", ", ".join(packet["failed"]))
print(out)
