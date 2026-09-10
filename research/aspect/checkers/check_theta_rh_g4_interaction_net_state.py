#!/usr/bin/env python3
"""Validate corrected-G4 RH SCC typing, migration, no-go gates, and receipts."""
import copy
import hashlib
import json
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCC = ROOT / "research/aspect/scc"
sys.path.insert(0, str(SCC))
from rh_net_state_compiler import compile_rh_net_state

CONTRACT = ROOT / "research/aspect/contracts/theta-rh-interaction-net-state.v2.json"
V1 = ROOT / "research/aspect/contracts/theta-rh-interaction-net-state.v1.json"
RESULT = ROOT / "research/aspect/results/theta_rh_g4_interaction_net_state.json"
CHECKER = Path(__file__).resolve()
c = json.loads(CONTRACT.read_text(encoding="utf-8"))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def node(contract, identifier):
    return next(item for item in contract["constructors"] if item["id"] == identifier)

def rejected(mutator):
    candidate = copy.deepcopy(c)
    mutator(candidate)
    return compile_rh_net_state(candidate)["passed"] is False

hostiles = {
    "det3_det2_variance_rejected": rejected(lambda x: x["determinant_ideal_contract"].update(bare_euler="det2")),
    "relative_det2_double_count_rejected": rejected(lambda x: x["determinant_ideal_contract"].update(relative_reciprocal_return="det3")),
    "theta_to_green_shortcut_rejected": rejected(lambda x: node(x, "evans_to_conservative_green_chain_map").update(depends_on=["theta_koszul_divisor_complex"])),
    "range_closure_to_exact_range_rejected": rejected(lambda x: x["centered_incidence_contract"].update(forcing_vector_membership="exact_range", exact_lift_authorized=True)),
    "gram_compression_as_dynamics_rejected": rejected(lambda x: x["three_port_contract"].update(gram_compression_is_dynamics=True)),
    "scalar_evans_vector_collapse_rejected": rejected(lambda x: x["rh_bearing_residual"].update(identity="scalar Evans mismatch = 0")),
    "incomplete_prime_shell_promotion_rejected": rejected(lambda x: node(x, "prime_shell_adjoint_residual_family").update(status="constructed", witness_ref="corrected_g4_audit", authority_class="source_derived")),
    "global_response_promotion_rejected": rejected(lambda x: node(x, "global_fourier_poisson_response_intertwining").update(status="constructed", witness_ref="exact_evans_five_port_rigging", authority_class="source_derived")),
    "module_length_omission_rejected": rejected(lambda x: node(x, "critical_seam_green_confinement")["depends_on"].remove("local_module_length_preservation")),
    "rh_terminal_promotion_rejected": rejected(lambda x: node(x, "riemann_hypothesis_terminal").update(status="constructed", witness_ref="corrected_g4_audit", authority_class="source_derived")),
    "missing_witness_rejected": rejected(lambda x: node(x, "two_sided_evans_matching_lift").pop("witness_ref")),
    "interface_mismatch_rejected": rejected(lambda x: node(x, "conservative_green_complex").update(interface_ref="undeclared")),
    "missing_green_interface_field_rejected": rejected(lambda x: node(x, "conservative_green_complex")["required_interface_fields"].remove("function_valued_wronskian_incidence")),
    "negative_knowledge_flip_rejected": rejected(lambda x: x["negative_knowledge_gates"].update(range_closure_equals_exact_range=True)),
    "semantic_promotion_rejected": rejected(lambda x: x["semantic_invariants"].update(pass_does_not_imply_proved=False)),
    "migration_rewrite_rejected": rejected(lambda x: x["versioning"].update(relation="replaces_and_rewrites")),
}
baseline = compile_rh_net_state(c)
historical = compile_rh_net_state(json.loads(V1.read_text(encoding="utf-8")))
checks = {
    "baseline_passes": baseline["passed"],
    "historical_v1_still_passes": historical["passed"],
    "corrected_g4_selected": baseline.get("model_generation") == "corrected_G4",
    "pass_is_not_proof": baseline.get("proved") is False,
    "physical_realization_not_claimed": baseline.get("physical_realization") is False,
    "rh_remains_open": baseline.get("terminal") == {"id":"riemann_hypothesis_terminal","status":"open","rh_proved":False},
    "jet_residual_family_explicit": "0 <= j < multiplicity" in baseline.get("rh_bearing_residual", {}).get("jet_family", ""),
    "underspecified_green_chain_remains_open": all(node(c, x)["status"] == "open" for x in ["conservative_green_complex","exact_evans_history_domain","three_port_block_domain_membership","five_port_arithmetic_summability","maximal_isotropic_evans_domain"]),
    "green_interface_is_frontier_gate": baseline.get("frontier_antichain", []) == ["conservative_green_complex"],
    "terminal_cut_sets_computed": baseline.get("terminal_cut_sets", {}).get("minimal_blocking_sets") == [["conservative_green_complex"]],
    "all_interfaces_checked": baseline.get("interface_pullback", {}).get("all_edges_checked") is True,
    **hostiles,
}
core = {
    "schema": "marici.aspect.theta-rh-g4-interaction-net-check.v2",
    "contract": str(CONTRACT.relative_to(ROOT)).replace("\\", "/"),
    "passed": all(checks.values()),
    "checks": checks,
    "frontier_antichain": baseline.get("frontier_antichain"),
    "terminal_cut_sets": baseline.get("terminal_cut_sets"),
    "rh_bearing_chain_map": "evans_to_conservative_green_chain_map",
    "rh_bearing_residual": baseline.get("rh_bearing_residual"),
    "claim_boundary": "A pass validates contract typing, migration, interface checks, no-go invariants, and hostile rejection; it does not prove response intertwining, prime-shell cancellation, Green confinement, physical realization, or RH."
}
receipt = {
    "schema": "marici.scc.execution-receipt.v1",
    "command": "python research/aspect/checkers/check_theta_rh_g4_interaction_net_state.py",
    "python": platform.python_version(),
    "contract_sha256": digest(CONTRACT),
    "compiler_sha256": digest(SCC / "rh_net_state_compiler.py"),
    "checker_sha256": digest(CHECKER),
    "fixture_ids": [x["id"] for x in c["hostile_fixtures"]],
    "evidence_sha256": hashlib.sha256(json.dumps(core, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
}
out = {**core, "execution_receipt": receipt}
RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
raise SystemExit(0 if out["passed"] else 1)
