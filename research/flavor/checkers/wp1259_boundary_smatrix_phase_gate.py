import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1150,1151,1152)
wp1150=json.loads((ROOT/"results"/"wp1150_smatrix_phase_matching_gate.json").read_text())
wp1151=json.loads((ROOT/"results"/"wp1151_fixed_q_smatrix_disjointness.json").read_text())
wp1152=json.loads((ROOT/"results"/"wp1152_doubly_stochastic_support_gate.json").read_text())
assert wp1150["classification"].startswith("negative gate: universal Hadamard")
assert wp1151["classification"].startswith("classification no-go")
assert wp1152["classification"].startswith("negative gate: sparse support-two")
# Hadamard and fixed-q support algebra are exact, but no class selector,
# S-matrix matching intersection, sparse localized modulus, or source packet
# exists.
phase_classification=True
disjointness=True
support_gate=True
selected_class=False
smatrix_matching_intersection=False
sparse_modulus=False
physical16_channels=False
selected_kernel=False
assert phase_classification and disjointness and support_gate
assert wp1151["smatrix_matching_intersection"]==0 and wp1152["consistent_support_two_patterns"]==0
assert not (selected_class or smatrix_matching_intersection or sparse_modulus or physical16_channels or selected_kernel)
result={
    "schema":"marici.flavor.wp1259.v1",
    "status":"PASS",
    "question":"Can boundary S-matrix phase data select a quotient matching class?",
    "dpc":{
        "conjecture":"Boundary S-matrix phases or fixed-q unitary moduli may select one of the three quotient matching classes.",
        "rivals":["universal Hadamard phase","fixed-q S-matrix matching","sparse support-two modulus","support-three search"],
        "risky_consequences":["H6 moduli are universal","matching maps are fixed-q and nonuniversal","fixed-q doubly stochastic maps form a 20-dimensional affine family","67950 support-two patterns are tested"],
        "falsification_attempt":"Hadamard phases are class-independent, every rank-three matching fails double stochasticity, and every support-two pattern is linearly inconsistent with the fixed-q target.",
        "residual":"decide whether support three admits a fixed-q doubly stochastic solution",
        "disposition":"retain exact phase/disjointness/support classifications; reject current S-matrix packet"
    },
    "phase_matching":{
        "matching_classes":wp1150["matching_classes"],
        "hadamard_modulus_universal":wp1150["hadamard_modulus_universal"],
        "matching_maps_universal":wp1150["matching_maps_universal"],
        "class_discriminating_phase_channels":wp1150["class_discriminating_phase_channels"],
        "physical16_asymptotic_channels":wp1150["physical16_asymptotic_channels"]
    },
    "fixed_q_disjointness":{
        "matching_maps":wp1151["matching_maps"],
        "matching_maps_doubly_stochastic":wp1151["matching_maps_doubly_stochastic"],
        "smatrix_matching_intersection":wp1151["smatrix_matching_intersection"],
        "fixed_q_doubly_stochastic_affine_dimension":wp1151["fixed_q_doubly_stochastic_affine_dimension"],
        "uniform_member":wp1151["uniform_member"]
    },
    "support_gate":{
        "support_one_maps":wp1152["support_one_maps"],
        "support_two_patterns_tested":wp1152["support_two_patterns_tested"],
        "consistent_support_two_patterns":wp1152["consistent_support_two_patterns"],
        "full_support_solution":wp1152["full_support_solution"],
        "minimal_possible_support_lower_bound":wp1152["minimal_possible_support_lower_bound"]
    },
    "phase_classification_exact":phase_classification,
    "fixed_q_disjointness_exact":disjointness,
    "support_gate_exact":support_gate,
    "selected_class":selected_class,
    "smatrix_matching_intersection":smatrix_matching_intersection,
    "sparse_modulus":sparse_modulus,
    "physical16_channels":physical16_channels,
    "selected_kernel":selected_kernel,
    "classification":"conditional S-matrix gate: phase, disjointness, and support facts exact, packet absent",
    "remaining_gate":"decide support-three fixed-q doubly stochastic realizability, then derive source phase authority",
    "hostile_gate":"do not call H6 phases, fixed-q disjointness, support-two failure, J6/6, or support algebra a boundary S-matrix packet",
    "claim_boundary":"WP1150 through WP1152 classify algebra and close tested routes; no phase channels, matching intersection, sparse modulus, or selected kernel is sourced",
    "disposition":"boundary S-matrix phase gate resolved conditionally; support-three rival selected"
}
(ROOT/"results"/"wp1259_boundary_smatrix_phase_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1259 PASS: phase, disjointness, and support facts exact, packet absent")
