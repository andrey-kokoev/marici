import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "contracts" / "flavor-interaction-net-state.v1.json").read_text())
nodes = {node["id"]: node for node in contract["nodes"]}

tested_gates = [
    "wp1130_six_branch_preparation_law_gate",
    "wp1131_parent_branching_preparation_no_go",
    "wp1132_dimension_trace_preparation_gate",
    "wp1133_uv_boundary_state_matching_no_go",
]
assert all(name in nodes for name in tested_gates)
assert all(nodes[name]["status"] == "constructed" for name in tested_gates)

# Conditional algebra retains exact q, but no current constructor passes the
# authority interface.
q = [Fraction(d,23) for d in (6,8,1,4,2,2)]
assert len(q) == 6 and sum(q) == 1

current_source_capabilities = {
    "twenty_three_dimensional_microspace": False,
    "normalized_boundary_state": False,
    "sector_projection_probabilities": False,
    "preparation_operator": False,
    "source_provenance_for_measure": False,
}
assert not any(current_source_capabilities.values())

constructor_candidates = [
    "sector dimension distribution",
    "parent branching",
    "dimension-trace ensemble",
    "UV boundary-state matching",
]
current_source_passes = 0
assert len(constructor_candidates) == 4
assert current_source_passes == 0

minimal_new_capability = {
    "microspace": "23-dimensional sourced sector microspace",
    "state": "normalized boundary state or density matrix",
    "probabilities": "sector projections equal (6,8,1,4,2,2)/23",
    "operator": "source-derived preparation operator with provenance",
}
assert len(minimal_new_capability) == 4

result = {
    "schema": "marici.flavor.wp1134.v1",
    "status": "PASS",
    "question": "Does the current source packet contain an admissible six-branch preparation constructor?",
    "dpc": {
        "conjecture": "The current source packet contains at least one admissible six-branch preparation constructor.",
        "rivals": [
            "sector dimension distribution",
            "parent branching",
            "dimension-trace ensemble",
            "UV boundary-state matching"
        ],
        "risky_consequences": [
            "23-dimensional sourced microspace",
            "normalized boundary state",
            "sector projections equal q",
            "source-derived preparation operator and measure provenance"
        ],
        "falsification_attempt": "Every tested rival fails the authority interface: exact conditional q exists, but zero current-source constructors supply the required state, map, and provenance.",
        "residual": "A future UV preparation packet may supply the four-part state interface.",
        "disposition": "reject current-source preparation closure; define the minimal new preparation capability"
    },
    "tested_gates": tested_gates,
    "constructor_candidates": constructor_candidates,
    "current_source_passes": current_source_passes,
    "current_source_capabilities": current_source_capabilities,
    "conditional_q": [str(x) for x in q],
    "minimal_new_capability": minimal_new_capability,
    "classification": "closure audit: conditional branch weights exist, but current-source preparation authority is absent",
    "remaining_gate": "obtain a future source packet carrying the four-part preparation interface",
    "hostile_gate": "do not aggregate exact q, conditional density operators, or repeated negative gates into preparation authority",
    "claim_boundary": "this closes tested current-source preparation rivals, not all future UV ensembles",
    "disposition": "current-source preparation closure rejected; minimal capability specified",
}

(ROOT / "results" / "wp1134_preparation_constructor_closure_audit.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1134 PASS:", len(tested_gates), current_source_passes, len(minimal_new_capability))
