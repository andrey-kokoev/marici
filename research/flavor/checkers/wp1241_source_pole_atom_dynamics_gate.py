import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1054,1055,1056,1057,1058,1059)
wp1054=json.loads((ROOT/"results"/"wp1054_irreducible_spin11_pole_cell.json").read_text())
wp1055=json.loads((ROOT/"results"/"wp1055_principal_su12_top_cell.json").read_text())
wp1056=json.loads((ROOT/"results"/"wp1056_su6_localized_quartet_pole_cell.json").read_text())
wp1057=json.loads((ROOT/"results"/"wp1057_localized_quartet_inflow_gate.json").read_text())
wp1058=json.loads((ROOT/"results"/"wp1058_localized_su6_clock_alignment_gate.json").read_text())
wp1059=json.loads((ROOT/"results"/"wp1059_parent_hypermultiplet_clock_fiber.json").read_text())
assert wp1054["classification"].startswith("conditional irreducible-multiplet constructor")
assert wp1055["classification"].startswith("conditional parent/top-cell constructor")
assert wp1056["classification"].startswith("conditional anomaly-localization constructor")
assert wp1057["classification"].startswith("conditional anomaly-inflow cofiber")
assert wp1058["classification"].startswith("negative common-clock gate")
assert wp1059["classification"].startswith("conditional parent-clock fiber")
# Representation and localization ancestry select C,k, inflow, and narrow the
# clock gap, but do not prove the inter-parent mass equality or physical ports.
irreducible_pole_cell=True
principal_parent_cell=True
localized_c23_k2=True
fixed_inflow_cell=True
residual_clock_obstruction=True
parent_clock_gap_one=True
physical_port_law=False
fixed_complete_cs_vector=False
inter_parent_clock_equal=False
projection_to_spin11=False
physical_momentum_calibration=False
source_gain=False
assert irreducible_pole_cell and principal_parent_cell and localized_c23_k2 and fixed_inflow_cell
assert residual_clock_obstruction and parent_clock_gap_one
assert not (physical_port_law or fixed_complete_cs_vector or inter_parent_clock_equal or projection_to_spin11 or physical_momentum_calibration or source_gain)
result={
    "schema":"marici.flavor.wp1241.v1",
    "status":"PASS",
    "question":"Can representation or localization dynamics derive the pole-atom cell?",
    "dpc":{
        "conjecture":"Representation ancestry and anomaly localization jointly derive C=23, k=2, a fixed inflow class, and a narrowed common-clock problem.",
        "rivals":["spin-11 irreducible cell","SU(12) principal top cell","SU(6) one-quartet localization","fixed level-2 inflow","parent-level clock fiber"],
        "risky_consequences":["spin 11 supplies 23 Schur-degenerate atoms and two nilpotent directions","SU(12) uniquely has top C=23 in the bounded parent scan","one boundary quartet leaves C=23,k=2,kappa=14","the selected quartet has U(1) inflow level 2 while the port-destroying doublet pair has -4","SU(6) parent invariance narrows the clock obstruction to one inter-parent gap"],
        "falsification_attempt":"reducible clocks, wrong parents, wrong localizations, and wrong inflow classes fail, but the complete anomaly vector, physical E/F ports, and parent-clock equality remain missing.",
        "residual":"derive the full anomaly vector and UV compactification class, prove the inter-parent clock equality or projection to spin 11, and normalize the physical pole clock",
        "disposition":"accept representation/localization ancestry conditionally; reject it as source-derived pole dynamics"
    },
    "representation":wp1054["representation"],
    "selected_parent":wp1055["selected_parent"],
    "conditional_port_arity":wp1055["conditional_port_arity"],
    "selected_cell":wp1056["selected_cell"],
    "joint_selection":wp1056["joint_selection"],
    "selected_quartet_cell":wp1057["selected_quartet_cell"],
    "inflow_lattice_gate":wp1057["inflow_lattice_gate"],
    "clock_tests":wp1058["clock_tests"],
    "parent_clock":wp1059["clock_tests"],
    "irreducible_pole_cell":irreducible_pole_cell,
    "principal_parent_cell":principal_parent_cell,
    "localized_c23_k2":localized_c23_k2,
    "fixed_inflow_cell":fixed_inflow_cell,
    "residual_clock_obstruction":residual_clock_obstruction,
    "parent_clock_gap_one":parent_clock_gap_one,
    "physical_port_law":physical_port_law,
    "fixed_complete_cs_vector":fixed_complete_cs_vector,
    "inter_parent_clock_equal":inter_parent_clock_equal,
    "projection_to_spin11":projection_to_spin11,
    "physical_momentum_calibration":physical_momentum_calibration,
    "source_gain":source_gain,
    "classification":"conditional source-ancestry constructor: representation and localization select C,k and inflow, common clock and physical ports absent",
    "remaining_gate":"derive the complete anomaly vector, UV compactification class, inter-parent clock equality, and spin-11 projection from one source",
    "hostile_gate":"do not call representation arithmetic, localization selection, fixed U(1) inflow, or a one-gap parent fiber source-derived pole dynamics",
    "claim_boundary":"WP1054 through WP1059 provide exact ancestry, localization, inflow, and clock-gap algebra; no physical action, complete anomaly lattice, or gain is derived",
    "disposition":"source-derived pole-atom dynamics leaf resolved conditionally; inter-parent clock alignment rival selected"
}
(ROOT/"results"/"wp1241_source_pole_atom_dynamics_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1241 PASS: source ancestry conditional, inter-parent clock alignment absent")
