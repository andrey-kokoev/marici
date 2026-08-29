#!/usr/bin/env python3
import copy,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/"research/aspect/scc"))
from rh_net_state_compiler import compile_rh_net_state
CP=ROOT/"research/aspect/contracts/theta-rh-interaction-net-state.v1.json";RP=ROOT/"research/aspect/results/theta_rh_interaction_net_state.json"
base=json.loads(CP.read_text(encoding="utf-8"));report=compile_rh_net_state(base)
expected={"type_fiber_adams_composition","endpoint_operator_attachment","archimedean_determinant_operator_lift"}
def hostile(name,mutate,gate):
 c=copy.deepcopy(base);mutate(c);r=compile_rh_net_state(c);return {"id":name,"expected":gate,"actual":r.get("first_failed_gate"),"passed":r.get("first_failed_gate")==gate}
hostiles=[
 hostile("promote_common_domain_early",lambda c:next(x for x in c["constructors"] if x["id"]=="common_nine_operation_graph_domain").update(status="constructed",source_locator="scalar-shadow",authority_class="source_derived"),"premature_promotion"),
 hostile("promote_pairwise_overlap_early",lambda c:next(x for x in c["constructors"] if x["id"]=="overlap_adams_endpoint").update(status="constructed",source_locator="formal-pair",authority_class="source_derived"),"premature_promotion"),
 hostile("skip_associator",lambda c:next(x for x in c["constructors"] if x["id"]=="four_input_pentagon_cocycle_coherence").update(depends_on=["overlap_adams_endpoint","overlap_adams_archimedean","overlap_endpoint_archimedean"]),"higher_coherence_topology"),
 hostile("skip_pentagon",lambda c:next(x for x in c["constructors"] if x["id"]=="completion_stable_frontier_coherence").update(depends_on=["typed_three_way_associator"]),"higher_coherence_topology"),
 hostile("skip_unitors",lambda c:next(x for x in c["constructors"] if x["id"]=="triangle_unit_associator_coherence").update(depends_on=["typed_three_way_associator"]),"higher_coherence_topology"),
 hostile("skip_triangle",lambda c:next(x for x in c["constructors"] if x["id"]=="completion_stable_frontier_coherence").update(depends_on=["four_input_pentagon_cocycle_coherence"]),"higher_coherence_topology"),
 hostile("erase_completion_controls",lambda c:c.update(completion_evidence_requirements=[]),"completion_evidence_schema"),
 hostile("bound_generators_only",lambda c:c["completion_control_contract"].update(quantifies_over=["generating_associator_and_unitors"]),"composite_path_control"),
 hostile("omit_inverse_composite_bound",lambda c:c["completion_control_contract"].update(controls=["forward_composite_norm"]),"composite_path_control"),
 hostile("erase_hexagon_obligation",lambda c:c["conditional_coherences"].pop(0),"conditional_coherence"),
 hostile("authorize_domain_from_pairs",lambda c:next(x for x in c["constructors"] if x["id"]=="common_nine_operation_graph_domain").update(depends_on=["overlap_adams_endpoint","overlap_adams_archimedean","overlap_endpoint_archimedean","tail_seam_hilbert_schmidt_coupling"]),"higher_coherence_topology"),
 hostile("claim_rh",lambda c:c.update(claim="rh_proved"),"claim_boundary"),
 hostile("promote_determinant_lens_from_scalar",lambda c:next(x for x in c["lenses"] if x["kind"]=="determinant").update(status="constructed"),"lens_typing"),
 hostile("missing_source_locator",lambda c:next(x for x in c["constructors"] if x["id"]=="weighted_adams_cocycle").update(source_locator=None),"source_authority"),
]
checks={
 "partial_net_compiles":report.get("passed") is True,
 "frontier_is_exact_three_cell_antichain":set(report.get("frontier_antichain",[]))==expected,
 "pairwise_overlap_layer_declared":{x["id"] for x in base["constructors"] if x["id"].startswith("overlap_")}=={"overlap_adams_endpoint","overlap_adams_archimedean","overlap_endpoint_archimedean"},
 "associator_requires_all_pairwise_overlaps":next(x for x in base["constructors"] if x["id"]=="typed_three_way_associator")["depends_on"]==["overlap_adams_endpoint","overlap_adams_archimedean","overlap_endpoint_archimedean"],
 "pentagon_requires_associator":next(x for x in base["constructors"] if x["id"]=="four_input_pentagon_cocycle_coherence")["depends_on"]==["typed_three_way_associator"],
 "unitors_share_pairwise_basis":all(next(x for x in base["constructors"] if x["id"]==u)["depends_on"]==["overlap_adams_endpoint","overlap_adams_archimedean","overlap_endpoint_archimedean"] for u in ("left_unitor","right_unitor")),
 "triangle_requires_associator_and_unitors":next(x for x in base["constructors"] if x["id"]=="triangle_unit_associator_coherence")["depends_on"]==["typed_three_way_associator","left_unitor","right_unitor"],
 "completion_stability_requires_pentagon_and_triangle":next(x for x in base["constructors"] if x["id"]=="completion_stable_frontier_coherence")["depends_on"]==["four_input_pentagon_cocycle_coherence","triangle_unit_associator_coherence"],
 "higher_coherence_precedes_common_domain":next(x for x in base["constructors"] if x["id"]=="common_nine_operation_graph_domain")["depends_on"]==["completion_stable_frontier_coherence","tail_seam_hilbert_schmidt_coupling"],
 "compiler_exposes_finite_witness_basis":set(report.get("higher_coherence_witness_chain",[]))=={"typed_three_way_associator","left_unitor","right_unitor","four_input_pentagon_cocycle_coherence","triangle_unit_associator_coherence","completion_stable_frontier_coherence","common_nine_operation_graph_domain"},
 "completion_controls_are_analytic":set(report.get("completion_evidence_requirements",[]))=={"associator_continuity","left_unitor_continuity","right_unitor_continuity","inverse_continuity","uniform_composite_path_control","pentagon_residual_zero","triangle_residual_zero"},
 "uniform_control_quantifies_over_composites":report.get("completion_control_contract",{}).get("quantifies_over")==["admitted_canonical_coherence_paths","cutoffs","constructor_depths"],
 "uniform_control_bounds_forward_and_inverse":report.get("completion_control_contract",{}).get("controls")==["forward_composite_norm","inverse_composite_norm"],
 "isometric_or_global_bound_modes_only":report.get("completion_control_contract",{}).get("accepted_modes")==["isometric_unitary","uniform_composite_path_bound"] and report.get("completion_control_contract",{}).get("generator_only_bound_admissible") is False,
 "hexagon_and_dagger_are_conditionally_typed":{x["structure"] for x in report.get("conditional_coherences",[])}=={"braiding","dagger"},
 "source_inhabitants_distinct_from_formal_slots":set(report.get("domain_algebra",{}).get("source_derived_inhabitants",[])).isdisjoint(report.get("domain_algebra",{}).get("formal_constructor_slots",[])),
 "agents_have_one_principal_output":len(report.get("interaction_net",{}).get("agents",[]))==len(base["constructors"]) and all(a["principal"]["role"]=="principal" and a["principal"]["direction"]=="out" for a in report["interaction_net"]["agents"]),
 "dependencies_are_typed_auxiliary_wires":len(report["interaction_net"]["wires"])==sum(len(n["depends_on"]) for n in base["constructors"]) and all(w["wire_type"] and ".out" in w["source_port"] and ".in." in w["target_port"] for w in report["interaction_net"]["wires"]),
 "five_margins_and_spectral_identification_declared":{"completion_stable_five_margin_coercivity","spectral_identification"}<=set(report.get("downstream_open",[])),
 "universal_core_correctly_unavailable":report.get("domain_algebra",{}).get("universal_core_eligible") is False,
 "all_three_lenses_remain_open":set(report.get("lenses",{}).values())=={"open"},
 "rh_terminal_open":report.get("terminal",{}).get("rh_proved") is False,
 "all_hostiles_rejected":all(x["passed"] for x in hostiles),
}
out={"schema":"marici.aspect.theta-rh-interaction-net-state-check.v1","passed":all(checks.values()),"checks":checks,"hostiles":hostiles,"report":report}
RP.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,indent=2));raise SystemExit(0 if out["passed"] else 1)
