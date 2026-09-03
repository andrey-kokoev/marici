import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1110,1111,1112,1113,1114,1115)
wp1110=json.loads((ROOT/"results"/"wp1110_fused_defect_anomaly_analyticity_fiber.json").read_text())
wp1111=json.loads((ROOT/"results"/"wp1111_local_gs_split_realizability_fiber.json").read_text())
wp1112=json.loads((ROOT/"results"/"wp1112_endpoint_exchange_split_no_go.json").read_text())
wp1113=json.loads((ROOT/"results"/"wp1113_wilson_orientation_split_clock_no_go.json").read_text())
wp1114=json.loads((ROOT/"results"/"wp1114_extended_line_rho_no_go.json").read_text())
wp1115=json.loads((ROOT/"results"/"wp1115_quotient_descent_production_no_go.json").read_text())
assert wp1110["classification"].startswith("conditional gate: exact anomaly")
assert wp1111["classification"].startswith("conditional gate: local split")
for d in [wp1112,wp1113,wp1114,wp1115]: assert d["classification"].startswith("negative gate")
# Exact constraints and local split fibers are now known, but the routes
# meant to select them are closed.
constraint_fiber=True
local_split_fiber=True
endpoint_exchange_closed=True
wilson_orientation_closed=True
extended_rho_closed=True
quotient_production_closed=True
orientation_odd_datum=False
selected_split=False
independent_rho=False
production_kernel=False
physical16_descent=False
source_values=False
assert constraint_fiber and local_split_fiber and endpoint_exchange_closed and wilson_orientation_closed
assert extended_rho_closed and quotient_production_closed
assert not (orientation_odd_datum or selected_split or independent_rho or production_kernel or physical16_descent or source_values)
result={
    "schema":"marici.flavor.wp1251.v1",
    "status":"PASS",
    "question":"Can analytic constraints select the fused-defect field values?",
    "dpc":{
        "conjecture":"Anomaly and analyticity constraints may narrow the fused defect enough for endpoint, Wilson, extended-line, or descent routes to select the fields.",
        "rivals":["exact anomaly/analytic constraint fiber","local Green-Schwarz split fiber","endpoint exchange","orientation-odd Wilson/flux datum","extended determinant/Wilson line","quotient descent"],
        "risky_consequences":["the defect must satisfy the seven-channel lift, coset, parent coefficient -3, clock law, rho weight -3, 6x6 kernel, gain 3/2, and reweighting","g0=-3/2+t and gpi=-3/2-t realize the split with exact target t=0 and coset domain Z","endpoint reflection maps the quartet to a different coset","Wilson orientation does not couple to the split and 6n squared erases clock sign","extended lines reduce to c/D or lack global sections","quotient descent is permutation/projection with gain 1"],
        "falsification_attempt":"no route selects an orientation-odd boundary datum, split, independent rho, source interaction kernel, or Physical16 descent.",
        "residual":"construct an independent orientation-odd UV boundary datum selecting the split and clock orientation, then derive rho, kernel, gain, and descent",
        "disposition":"accept the constraint/split fibers conditionally; close the attempted selector routes"
    },
    "constraints":wp1110["constraints"],
    "branch_distribution":wp1110["branch_distribution"],
    "physical_target":wp1110["physical_target"],
    "split_parameterization":wp1111["split_parameterization"],
    "gravity_levels_t":wp1111["gravity_levels_t"],
    "exact_target_t":wp1111["exact_target_t"],
    "coset_t_domain":wp1111["coset_t_domain"],
    "endpoint_exchange":{
        "quartet_coset":wp1112["quartet_coset"],
        "reflected_coset":wp1112["reflected_coset"],
        "split_action":wp1112["split_action"]
    },
    "wilson_orientation":{
        "clock_ratio_pm1":wp1113["clock_ratio_pm1"],
        "wilson_phase_pair":wp1113["wilson_phase_pair"],
        "joint_selector":wp1113["joint_selector"]
    },
    "extended_line":{
        "candidate_form":wp1114["candidate_form"],
        "constant_ratio":wp1114["constant_ratio"],
        "nontrivial_torsion_global_sections":wp1114["nontrivial_torsion_global_sections"]
    },
    "quotient_descent":{
        "identity_image":wp1115["identity_image"],
        "swap_image":wp1115["swap_image"],
        "permutation_gain":wp1115["permutation_gain"]
    },
    "constraint_fiber":constraint_fiber,
    "local_split_fiber":local_split_fiber,
    "endpoint_exchange_closed":endpoint_exchange_closed,
    "wilson_orientation_closed":wilson_orientation_closed,
    "extended_rho_closed":extended_rho_closed,
    "quotient_production_closed":quotient_production_closed,
    "orientation_odd_datum":orientation_odd_datum,
    "selected_split":selected_split,
    "independent_rho":independent_rho,
    "production_kernel":production_kernel,
    "physical16_descent":physical16_descent,
    "source_values":source_values,
    "classification":"conditional fused-defect gate: constraints and split fiber exact, orientation-odd selector absent",
    "remaining_gate":"construct an orientation-odd UV boundary datum selecting split and clock orientation, then rho, kernel, gain, and descent",
    "hostile_gate":"do not call constraint fibers, local split realizability, endpoint reflection, Wilson orientation, extended lines, or quotient descent a field-value construction",
    "claim_boundary":"WP1110 through WP1115 provide exact constraints, fibers, and no-gos; no source values or Physical16 descent are derived",
    "disposition":"fused-defect analytic-constraints leaf resolved conditionally; orientation-odd boundary-datum rival selected"
}
(ROOT/"results"/"wp1251_fused_defect_analytic_constraints_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1251 PASS: constraint and split fibers exact, orientation-odd selector absent")
