#!/usr/bin/env python3
"""Aggregate the exact Clark positivity frontier without asserting RH."""
import hashlib,json
from pathlib import Path
R=Path(__file__).parents[1]/"results"
files={
 "normalization":"xi_clark_weyl_sewing_normalization.json",
 "sylvester":"reciprocal_sylvester_storage_gate.json",
 "neutral_matching":"reciprocal_neutral_matching_quotient.json",
 "parity":"bilateral_theta_parity_block_gate.json",
 "polar_compatibility":"polar_graph_clark_boundary_compatibility.json",
 "linear_graph_nogo":"no_fixed_linear_clark_graph.json",
 "codefect":"clark_hardy_codefect_gate.json",
 "certified_packet":"xi_clark_nested_six_point_rung.json",
 "nested_Douglas":"certified_nested_source_douglas_system.json",
}
d={k:json.loads((R/v).read_text(encoding="utf-8")) for k,v in files.items()}
checks={
 "all_frontier_certificates_pass":all(x["passed"] for x in d.values()),
 "normalization_closed":d["normalization"]["checks"]["Clark_sum_recovers_twice_X"],
 "Sylvester_solution_not_enough":d["sylvester"]["checks"]["algebraic_sylvester_solution_does_not_imply_positivity"],
 "neutral_matching_criterion_exact":d["neutral_matching"]["checks"]["matched_graph_is_neutral"],
 "bilateral_problem_reduced_to_parity_graph":d["parity"]["checks"]["green_form_has_only_off_diagonal_parity_blocks"],
 "polar_graph_rejected_by_physical_sections":d["polar_compatibility"]["checks"]["positive_polar_graph_does_not_preserve_Clark_transfer"],
 "every_fixed_continuous_linear_graph_rejected":d["linear_graph_nogo"]["checks"]["no_parameter_independent_continuous_linear_graph"],
 "Hardy_codefect_is_exact_remaining_gate":d["codefect"]["checks"]["correct_defect_is_I_minus_M_Mstar"],
 "finite_six_point_packet_certified":d["certified_packet"]["all_63_principal_minors_strictly_positive"],
 "nested_Douglas_maps_compatible_through_rung_six":d["nested_Douglas"]["checks"]["restriction_compatibility_is_exact"],
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.clark-positivity-frontier.v1",
 "checks":checks,"passed":True,
 "closed":["oriented resolvent normalization","reciprocal Xi sewing","Clark E/E* sewing","source Krein factorization","typing of the Hardy co-defect"],
 "rejected_shortcuts":["off-diagonal Sylvester solvability alone","unqualified neutral matching","polar-phase graph compression","any fixed continuous linear parity graph containing all exponential sections"],
 "finite_certified_progress":"One nested six-point family has strict positive Grams and exact compatible Douglas contractions at every prefix rung.",
 "single_open_statement":"I-M_Theta M_Theta* >= 0 on upper-half-plane Hardy space",
 "equivalences":["Theta is Schur","|E*(z)|<=|E(z)| for Im(z)>0","the de Branges/Clark kernel is positive semidefinite","the completed signed Weil form has the required positivity"],
 "claim_boundary":"Finite-rung certification does not imply the all-packet Pick condition. No global positivity or RH claim is made; a proof must control arbitrary finite packets or establish the Hardy co-defect inequality directly.",
 "dependencies":{k:{"path":v,"sha256":hashlib.sha256((R/v).read_bytes()).hexdigest()} for k,v in files.items()}
}
p=R/"clark_positivity_frontier.json";p.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!="dependencies"},indent=2))
