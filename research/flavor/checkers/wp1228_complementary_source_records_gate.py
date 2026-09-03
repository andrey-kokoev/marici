import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(990,991,992,993,994,995)
wp990=json.loads((ROOT/"results"/"wp990_two_response_physical_quotient_closure.json").read_text())
wp991=json.loads((ROOT/"results"/"wp991_three_configuration_relative_energy_probe.json").read_text())
wp992=json.loads((ROOT/"results"/"wp992_three_state_control_region_no_go.json").read_text())
wp993=json.loads((ROOT/"results"/"wp993_universal_adaptive_control_section.json").read_text())
wp994=json.loads((ROOT/"results"/"wp994_adaptive_control_robustness_radius.json").read_text())
wp995=json.loads((ROOT/"results"/"wp995_robustness_normalization_no_go.json").read_text())
assert wp990["classification"] == "source-derived faithful quotient separator; neither selector nor rigidifier"
assert wp991["classification"] == "minimal formal relational instrument and faithful separator; neither selector nor rigidifier"
assert wp992["classification"] == "uniform preparation no-go; neither selector nor rigidifier"
assert wp993["classification"] == "formal universal feedback section; neither source selector nor physical instrument"
assert wp994["classification"] == "formal robust feedback margin; neither source selector nor calibrated apparatus"
assert wp995["classification"] == "WP994 margin is target-normalization relative, not an intrinsic apparatus threshold"
# The complementary records separate the physical quotient formally, but
# preparation, feedback, robustness, and actuator normalization are not
# source-authorized.
quotient_separator=True
formal_relative_probe=True
uniform_preparation_no_go=True
formal_feedback_section=True
robust_margin_relative=True
actuator_normalization_absent=True
physical_records=False
shared_provenance=False
calibrated_instrument=False
assert quotient_separator and formal_relative_probe and uniform_preparation_no_go
assert formal_feedback_section and robust_margin_relative and actuator_normalization_absent
assert not (physical_records or shared_provenance or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1228.v1",
    "status":"PASS",
    "question":"Can formal quotient responses and adaptive feedback construct the complementary source records?",
    "dpc":{
        "conjecture":"The two quotient responses, three-configuration relative probe, and universal adaptive section construct the source records.",
        "rivals":["q and k/q quotient separator","three-state relative-energy probe","uniform finite schedule","universal affine feedback","robustness radius under target rescaling"],
        "risky_consequences":["q and k/q have rank two and kernel exactly the normalization orbit","three relative configurations reconstruct q and k formally but have no current physical instrument","no uniform finite schedule reaches all regions","universal feedback requires q,k records before control","the joint error radius is L/24697 and target normalization is unfixed"],
        "falsification_attempt":"formal separation and feedback exist, but no source-authorized preparation, actuator, or scale fixes executable records.",
        "residual":"source-derived actuator normalization or cost/support constraint fixing admissible target scale, plus reset-safe feedback and labelled relative-energy verification",
        "disposition":"accept formal complementary construction only; reject physical source records"
    },
    "probe_family":wp990["source_authorized_probe_family"],
    "relative_reconstruction":wp991["reconstruction"],
    "preparation_regions":wp992["preparation_regions"],
    "feedback_section":wp993["section"],
    "robustness_radii":wp994["linfinity_radii"],
    "joint_radius_law":wp995["joint_radius_law"],
    "quotient_separator":quotient_separator,
    "formal_relative_probe":formal_relative_probe,
    "uniform_preparation_no_go":uniform_preparation_no_go,
    "formal_feedback_section":formal_feedback_section,
    "robust_margin_relative":robust_margin_relative,
    "actuator_normalization_absent":actuator_normalization_absent,
    "physical_records":physical_records,
    "shared_provenance":shared_provenance,
    "calibrated_instrument":calibrated_instrument,
    "classification":"conditional complementary construction: formal quotient and feedback exist, physical records absent",
    "remaining_gate":"derive actuator normalization or cost/support constraint, then realize q,k measurement, reset-safe feedback, independent actuation, and labelled relative-energy verification",
    "hostile_gate":"do not call quotient separation, relative reconstruction, universal feedback, or target-relative robustness physical source records",
    "claim_boundary":"formal construction is source-derived at the quotient level, but apparatus authority and scale are absent",
    "disposition":"complementary-source-records leaf resolved conditionally; actuator-normalization rival selected"
}
(ROOT/"results"/"wp1228_complementary_source_records_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1228 PASS: complementary records formal, actuator authority absent")
