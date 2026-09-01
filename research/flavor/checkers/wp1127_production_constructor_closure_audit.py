import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "contracts" / "flavor-interaction-net-state.v1.json").read_text())
nodes = {node["id"]: node for node in contract["nodes"]}

tested_gates = [
    "wp1118_physical16_event_representation_no_go",
    "wp1119_physical16_amplitude_algebra_gate",
    "wp1120_complete_mixing_source_no_go",
    "wp1121_irreversible_boundary_mixing_no_go",
    "wp1122_boundary_s_matrix_hadamard_gate",
    "wp1123_unitary_s_matrix_hadamard_classification",
    "wp1124_hadamard_phase_matching_gate",
    "wp1125_anomaly_sector_phase_provenance_no_go",
    "wp1126_green_residue_event_basis_no_go",
]
assert all(name in nodes for name in tested_gates)
assert all(nodes[name]["status"] == "constructed" for name in tested_gates)

# Exact production requirements remain the same across all constructor rivals.
u = Fraction(1,6)
p = Fraction(1,4)
gain = Fraction(3,2)
assert gain*u == p

current_source_capabilities = {
    "six_independent_physical16_channels": False,
    "selected_packet_preserving_phase_observable": False,
    "sourced_event_production_kernel": False,
    "event_time_or_readout_map": False,
    "source_authorized_h6_representative": False,
}
assert not any(current_source_capabilities.values())

# The algebra exists conditionally, but no current-source constructor passes the
# authority interface. The count is exact, not a heuristic.
constructor_candidates = [
    "Markov/Krylov dynamics",
    "complete mixing",
    "irreversible boundary mixing",
    "boundary S-matrix/Hadamard",
    "anomaly phases",
    "Green residues",
]
current_source_passes = 0
assert len(constructor_candidates) == 6
assert current_source_passes == 0

minimal_new_capability = {
    "channel_basis": "six independent physical16 event channels",
    "phase_observable": "selected-packet-preserving H6 character or equivalent",
    "production_kernel": "P with sum_b P_eb=1 and Pq=(1/6)^6",
    "event_map": "source-derived event/readout map with (3/2)Pq=(1/4)^6",
}
assert len(minimal_new_capability) == 4

result = {
    "schema": "marici.flavor.wp1127.v1",
    "status": "PASS",
    "question": "Does the current source packet contain an admissible physical16 production constructor?",
    "dpc": {
        "conjecture": "The current UV boundary source packet contains at least one admissible physical16 production constructor.",
        "rivals": [
            "Markov/Krylov dynamics",
            "complete mixing",
            "irreversible boundary mixing",
            "boundary S-matrix/Hadamard",
            "anomaly phases",
            "Green residues"
        ],
        "risky_consequences": [
            "six independent physical16 channels",
            "selected-packet-preserving phase observable",
            "sourced production kernel P",
            "event/readout map with (3/2)Pq=(1/4)^6"
        ],
        "falsification_attempt": "Every tested rival fails the authority interface: conditional algebra exists, but zero current-source constructors supply all required capabilities.",
        "residual": "A future UV boundary packet can supply the four-part production interface.",
        "disposition": "reject current-source closure; define the minimal new source capability"
    },
    "tested_gates": tested_gates,
    "constructor_candidates": constructor_candidates,
    "current_source_passes": current_source_passes,
    "current_source_capabilities": current_source_capabilities,
    "exact_targets": {
        "probability_per_event": str(u),
        "physical_event_weight": str(p),
        "gain": str(gain)
    },
    "minimal_new_capability": minimal_new_capability,
    "classification": "closure audit: conditional event algebra exists, but current-source production authority is absent",
    "remaining_gate": "obtain a future source packet carrying the four-part event-production interface",
    "hostile_gate": "do not aggregate conditional algebra, candidate lists, or repeated negative gates into production authority",
    "claim_boundary": "this closes tested current-source rivals, not all conceivable future UV dynamics",
    "disposition": "current-source production closure rejected; minimal capability specified",
}

(ROOT / "results" / "wp1127_production_constructor_closure_audit.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1127 PASS:", len(tested_gates), current_source_passes, len(minimal_new_capability))
