import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1036,1037,1038,1039)
wp1036=json.loads((ROOT/"results"/"wp1036_nonprimitive_integer_lift_capacity.json").read_text())
wp1037=json.loads((ROOT/"results"/"wp1037_discrete_source_actuator_type_no_go.json").read_text())
wp1038=json.loads((ROOT/"results"/"wp1038_common_substrate_integer_preparation_fiber.json").read_text())
wp1039=json.loads((ROOT/"results"/"wp1039_integer_coefficient_pole_typing_fiber.json").read_text())
assert wp1036["classification"] == "arithmetic capacity point and presentation rigidifier only; not a source selector"
assert wp1037["classification"] == "arithmetic capacity without actuator; neither selector nor physical rigidifier"
assert wp1038["classification"] == "common-substrate preparation rigidifier only; the selecting energy/order is additional source data"
assert wp1039["classification"] == "integer coefficient rigidifier only; not a typed single-pole threshold selector"
# A compatible integer lift exists at (k,C)=(2,23), but local control,
# common support, and coefficient normalization do not type or select it.
nonprimitive_capacity=True
unique_k2_c23_slice=True
local_actuator_absent=True
common_substrate_unselected=True
pole_spectrum_unfixed=True
representation_theorem=False
absolute_label_order=False
single_pole_degeneracy=False
threshold_matching=False
calibrated_count_pole_instrument=False
assert nonprimitive_capacity and unique_k2_c23_slice and local_actuator_absent
assert common_substrate_unselected and pole_spectrum_unfixed
assert not (representation_theorem or absolute_label_order or single_pole_degeneracy or threshold_matching or calibrated_count_pole_instrument)
result={
    "schema":"marici.flavor.wp1237.v1",
    "status":"PASS",
    "question":"Can a discrete source actuator type and select the conditional integer lift?",
    "dpc":{
        "conjecture":"The nonprimitive integer lift (k,C)=(2,23) is selected and typed as the required pole operator by discrete source actuation.",
        "rivals":["nonprimitive integer lift","local continuous control","finite common substrate","zero-momentum integer coefficient","complete finite-momentum pole spectrum"],
        "risky_consequences":["at k=2, C=23 is the unique fitted integer coefficient","integer labels live in object space and admit no rank-two local actuator","a finite three-point substrate selects only a relative middle slot","C=23 fixes zero-momentum h but not pole degeneracy","single-pole and split-pole packets differ by 3/230 at q squared=1"],
        "falsification_attempt":"arithmetic capacity does not become a source operation; common support does not fix the absolute label; integer normalization does not fix threshold typing.",
        "residual":"an anomaly-complete representation theorem selecting k=2,C=23, a source-derived absolute label order, single-pole degeneracy and residues, threshold transport, and calibrated count/pole instrumentation",
        "disposition":"accept (k,C)=(2,23) as conditional arithmetic capacity only; reject discrete source-actuator typing"
    },
    "compatible_packet":wp1036["compatible_packet"],
    "adjacent_falsifiers":wp1036["adjacent_falsifiers"],
    "local_actuator":wp1037["authorized_local_actuator"],
    "translation_fiber":wp1038["translation_fiber"],
    "hostile_packets":wp1039["hostile_packets"],
    "finite_response_difference":wp1039["finite_response_difference"],
    "nonprimitive_capacity":nonprimitive_capacity,
    "unique_k2_c23_slice":unique_k2_c23_slice,
    "local_actuator_absent":local_actuator_absent,
    "common_substrate_unselected":common_substrate_unselected,
    "pole_spectrum_unfixed":pole_spectrum_unfixed,
    "representation_theorem":representation_theorem,
    "absolute_label_order":absolute_label_order,
    "single_pole_degeneracy":single_pole_degeneracy,
    "threshold_matching":threshold_matching,
    "calibrated_count_pole_instrument":calibrated_count_pole_instrument,
    "classification":"conditional discrete capacity: (k,C)=(2,23) is unique in one arithmetic slice but untyped and unselected",
    "remaining_gate":"derive one anomaly-complete representation selecting k=2,C=23 and enforcing single-pole threshold data before using the fitted interval",
    "hostile_gate":"do not call integer existence, slice uniqueness, common support, or zero-momentum normalization a discrete source actuator or pole type",
    "claim_boundary":"the arithmetic point survives only as a conditional capacity packet; source operations and finite-momentum type are absent",
    "disposition":"discrete source-actuator-typing leaf resolved conditionally; representation-theorem rival selected"
}
(ROOT/"results"/"wp1237_discrete_source_actuator_typing_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1237 PASS: (2,23) capacity conditional, representation theorem absent")
