import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1120,1121,1122,1123,1124,1125,1126)
wp1120=json.loads((ROOT/"results"/"wp1120_complete_mixing_source_no_go.json").read_text())
wp1121=json.loads((ROOT/"results"/"wp1121_irreversible_boundary_mixing_no_go.json").read_text())
wp1122=json.loads((ROOT/"results"/"wp1122_boundary_s_matrix_hadamard_gate.json").read_text())
wp1123=json.loads((ROOT/"results"/"wp1123_unitary_s_matrix_hadamard_classification.json").read_text())
wp1124=json.loads((ROOT/"results"/"wp1124_hadamard_phase_matching_gate.json").read_text())
wp1125=json.loads((ROOT/"results"/"wp1125_anomaly_sector_phase_provenance_no_go.json").read_text())
wp1126=json.loads((ROOT/"results"/"wp1126_green_residue_event_basis_no_go.json").read_text())
assert wp1120["classification"].startswith("negative gate: complete mixing")
assert wp1121["classification"].startswith("negative gate: conservative")
assert wp1122["classification"].startswith("conditional gate: F6 Hadamard")
assert wp1123["classification_label"].startswith("exact gate")
assert wp1124["classification"].startswith("conditional gate: source-shaped")
assert wp1125["classification"].startswith("negative gate: anomaly")
assert wp1126["classification"].startswith("negative gate: rank-one")
# The exact boundary algebra is classified, but the current source supplies
# no orientation-odd selector, channels, phases, or event-time map.
hadamard_classification=True
kronecker_algebra=True
complete_mixing_sourced=False
irreversible_mixing_sourced=False
c6_generator_sourced=False
endpoint_symmetry=False
anomaly_phase_provenance=False
residue_channels=False
orientation_odd_datum=False
selected_split=False
clock_orientation=False
physical16_channels=False
source_values=False
assert hadamard_classification and kronecker_algebra
assert not (complete_mixing_sourced or irreversible_mixing_sourced or c6_generator_sourced or endpoint_symmetry)
assert not (anomaly_phase_provenance or residue_channels or orientation_odd_datum or selected_split or clock_orientation or physical16_channels or source_values)
result={
    "schema":"marici.flavor.wp1252.v1",
    "status":"PASS",
    "question":"Can the current source construct an orientation-odd boundary datum?",
    "dpc":{
        "conjecture":"Boundary S-matrix or phase data may construct the orientation-odd UV datum selecting the split, clock orientation, and production algebra.",
        "rivals":["complete-mixing source","irreversible boundary generator","C6 Fourier Hadamard","C3xZ2 Kronecker Hadamard","anomaly-sector phases","Green-residue channels"],
        "risky_consequences":["complete mixing needs x=0 and irreversible six-state rates","the required unitary class is H6 with all moduli squared 1/6","F3 tensor F2 is target compatible","anomaly or Green residues must source phases and six event channels"],
        "falsification_attempt":"history has three isometric slots, zero dissipative rates and event-time maps, no C6 generator, endpoint Z2 fails packet symmetry, anomaly coefficients are not phase characters, and the Green residue has rank one.",
        "residual":"derive a sourced boundary character with a selected-packet-preserving six-channel map and event-time interface",
        "disposition":"retain H6/F3 tensor F2 as target algebra; reject current-source orientation-odd datum"
    },
    "complete_mixing":{
        "markov_form":wp1120["markov_form"],
        "uniformity_requires":wp1120["uniformity_requires"],
        "history_slots":wp1120["history_slots"]
    },
    "irreversible_mixing":{
        "required_generator_shape":wp1121["required_generator_shape"],
        "sourced_dissipative_rates":wp1121["sourced_dissipative_rates"],
        "sourced_event_time_maps":wp1121["sourced_event_time_maps"]
    },
    "hadamard":{
        "fourier_order":wp1122["fourier_order"],
        "squared_magnitude":wp1123["required_modulus_squared"],
        "classification":wp1123["classification"],
        "gauge_equivalences":wp1123["gauge_equivalences"]
    },
    "kronecker":{
        "kronecker_shape":wp1124["kronecker_shape"],
        "c3_history_invariant":wp1124["c3_history_invariant"],
        "endpoint_z2_selected_packet_symmetry":wp1124["endpoint_z2_selected_packet_symmetry"]
    },
    "anomaly_phases":{
        "anomaly_coefficients":wp1125["anomaly_coefficients"],
        "phase_characters_sourced":wp1125["phase_characters_sourced"],
        "six_channel_bijections":wp1125["six_channel_bijections"]
    },
    "green_residue":{
        "brane_couplings":wp1126["brane_couplings"],
        "residue_rank":wp1126["residue_rank"],
        "phase_observables_sourced":wp1126["phase_observables_sourced"]
    },
    "hadamard_classification":hadamard_classification,
    "kronecker_algebra":kronecker_algebra,
    "complete_mixing_sourced":complete_mixing_sourced,
    "irreversible_mixing_sourced":irreversible_mixing_sourced,
    "c6_generator_sourced":c6_generator_sourced,
    "endpoint_symmetry":endpoint_symmetry,
    "anomaly_phase_provenance":anomaly_phase_provenance,
    "residue_channels":residue_channels,
    "orientation_odd_datum":orientation_odd_datum,
    "selected_split":selected_split,
    "clock_orientation":clock_orientation,
    "physical16_channels":physical16_channels,
    "source_values":source_values,
    "classification":"conditional boundary-datum gate: H6 algebra exact, orientation-odd source absent",
    "remaining_gate":"derive a sourced boundary character, packet-preserving six-channel map, and event-time interface",
    "hostile_gate":"do not call Markov limits, isometric history, H6 algebra, anomaly integers, endpoint signs, or rank-one residues an orientation-odd boundary datum",
    "claim_boundary":"WP1120 through WP1126 classify target algebra and reject current source provenance; no split, clock orientation, or field values are derived",
    "disposition":"orientation-odd boundary-datum leaf resolved conditionally; sourced boundary-character rival selected"
}
(ROOT/"results"/"wp1252_orientation_odd_boundary_datum_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1252 PASS: H6 algebra exact, orientation-odd source absent")
