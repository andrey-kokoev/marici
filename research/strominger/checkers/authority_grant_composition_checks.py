#!/usr/bin/env python3
"""Exact positive and hostile checks for partial authority composition."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S = ROOT / "research" / "strominger"
sys.path.insert(0, str(S))

from authority_grant_composition import compile_packet  # noqa: E402

CONTRACT = S / "contracts" / "authority-grant-composition.v1.json"
HOSTILES = S / "contracts" / "authority-grant-composition-hostile-fixtures.v1.json"
OUT = S / "results" / "authority_grant_composition.json"


def by_id(packet, collection, item_id):
    items = packet
    for part in collection.split("."):
        items = items[part]
    return next(item for item in items if item["id"] == item_id)


def mutate(packet, mutations):
    candidate = copy.deepcopy(packet)
    for mutation in mutations:
        by_id(candidate, mutation["collection"], mutation["id"])[mutation["field"]] = mutation["value"]
    return candidate


def codes(compiled):
    return {item["code"] for item in compiled["errors"]}


def main():
    packet = json.loads(CONTRACT.read_text(encoding="ascii"))
    hostile_spec = json.loads(HOSTILES.read_text(encoding="ascii"))
    compiled = compile_packet(packet)

    hostile_results = {}
    for fixture in hostile_spec["fixtures"]:
        result = compile_packet(mutate(packet, fixture["mutations"]))
        expected = fixture["expected_code"]
        hostile_results[fixture["id"]] = {
            "description": fixture["description"],
            "valid": result["valid"],
            "expected_code": expected,
            "error_codes": sorted(codes(result)),
            "passed": not result["valid"] and expected in codes(result),
        }

    grants = {item["id"]: item for item in packet["authority_grants"]}
    compositions = {item["id"]: item for item in packet["compositions"]}
    cases = {item["id"]: item for item in packet["application_cases"]}
    transformations = {item["id"]: item for item in packet["transformations"]}
    representation_tests = {item["id"]: item for item in packet["representation_change_tests"]}
    presentation_cells = {item["id"]: item for item in packet["presentation_coherence_cells"]}
    presentation_atlases = {item["id"]: item for item in packet["presentation_atlas_coherence"]}
    descent_objects = {item["id"]: item for item in packet["authority_descent_objects"]}
    refinements = {item["id"]: item for item in packet["presentation_refinement_coherence"]}
    deletions = {item["id"]: item for item in packet["presentation_deletion_tests"]}
    provenance_nodes = {item["id"]: item for item in packet["source_provenance"]["nodes"]}
    provenance_edges = packet["source_provenance"]["edges"]
    interventions = {item["id"]: item for item in packet["source_intervention_tests"]}
    mechanism_audits = {item["id"]: item for item in packet["mechanism_identification_audits"]}

    left_result = grants[compositions["c_AC_CD"]["result"]]
    right_result = grants[compositions["c_AB_BD"]["result"]]
    result_signature = lambda grant: (
        grant["source_object"], grant["target_operation"], grant["target_object"],
        grant["authority_kind"], grant["evidence_domain"], grant["variance"],
    )

    gates = {
        "standalone_contract_compiles": compiled["valid"],
        "identity_laws_declared_twice": len(packet["identity_laws"]) == 2,
        "associativity_holds_on_typed_domain": result_signature(left_result) == result_signature(right_result)
            and packet["associativity_cells"][0]["coherence_defect"] == 0,
        "composition_preserves_authority_kind": all(
            len({grants[c["left"]]["authority_kind"], grants[c["right"]]["authority_kind"], grants[c["result"]]["authority_kind"]}) == 1
            for c in packet["compositions"]
        ),
        "transport_requires_authority_preservation": transformations["chart_transport"]["preserves_authority"],
        "theta_requires_explicit_seam_cell": cases["grothendieck_folded_theta"]["classification"] == "coherence_cell_required"
            and cases["grothendieck_folded_theta"]["explicit_coherence_cell"] == "moving-endpoint seam current plus reciprocal reflection",
        "theta_composite_remains_readout": cases["grothendieck_folded_theta"]["authority_result"] == "readout only",
        "kitaev_has_no_composable_physical_authority": cases["kitaev_logical_to_five_rail"]["classification"] == "no_composable_authority_map"
            and cases["kitaev_logical_to_five_rail"]["composition"] is None,
        "kitaev_rail_base_change_preserves_evidence_not_authority": transformations["rail_base_change"]["preserves_evidence"]
            and not transformations["rail_base_change"]["preserves_authority"],
        "removing_B_preserves_process_only_with_direct_source_grant":
            representation_tests["remove_B_direct_source_route"]["verdict"] == "process_explained_strictly"
            and representation_tests["remove_B_direct_source_route"]["direct_grant"] == "g_AC_direct",
        "changing_B_requires_source_derived_natural_coherence":
            representation_tests["replace_B_by_Bprime"]["verdict"] == "process_explained_coherently"
            and presentation_cells[representation_tests["replace_B_by_Bprime"]["coherence_cell_id"]]["source_derived"]
            and presentation_cells[representation_tests["replace_B_by_Bprime"]["coherence_cell_id"]]["naturality_defect"] == 0,
        "presentation_cells_are_invertible_and_kind_preserving": all(
            cell["invertible"] and cell["preserves_authority_kind"]
            for cell in packet["presentation_coherence_cells"]
        ),
        "presentation_atlas_has_zero_holonomy":
            presentation_atlases["atlas_B_Bprime_Bdoubleprime"]["holonomy_defect"] == 0
            and len(presentation_atlases["atlas_B_Bprime_Bdoubleprime"]["paths"]) == 2,
        "flat_descent_is_effective_and_unique":
            descent_objects["descent_process_AC"]["effective"]
            and descent_objects["descent_process_AC"]["reconstruction_defect"] == 0
            and descent_objects["descent_process_AC"]["ambiguity_kernel_rank"] == 0,
        "descent_stabilizer_is_source_authorized":
            set(descent_objects["descent_process_AC"]["stabilizer"]).issubset(
                descent_objects["descent_process_AC"]["source_authorized_stabilizer"]
            ),
        "source_authorized_gauge_descends_stackily":
            descent_objects["descent_process_AC_stacky"]["ambiguity_kernel_rank"] == 1
            and descent_objects["descent_process_AC_stacky"]["stabilizer_quotient_declared"]
            and descent_objects["descent_process_AC_stacky"]["quotient_ambiguity_rank"] == 0
            and set(descent_objects["descent_process_AC_stacky"]["stabilizer"]).issubset(
                descent_objects["descent_process_AC_stacky"]["source_authorized_stabilizer"]
            ),
        "explanatory_provenance_is_forward_and_source_rooted":
            provenance_nodes["prov_source"]["role"] == "source_constructor"
            and provenance_nodes["prov_readout"]["role"] == "readout"
            and all(
                provenance_nodes[edge["source"]]["stage"] < provenance_nodes[edge["target"]]["stage"]
                and edge["source_derived"]
                for edge in provenance_edges
            ),
        "coherence_is_prior_target_independent_and_recomputable": all(
            cell["derived_before_target"] and cell["target_independent"] and cell["counterfactual_recomputable"]
            for cell in packet["presentation_coherence_cells"]
        ),
        "source_intervention_regenerates_coherence":
            "prov_coherence" in interventions["intervene_on_source_constructor"]["observed_affected_nodes"]
            and interventions["intervene_on_source_constructor"]["fresh_recomputation"],
        "target_intervention_cannot_rewrite_upstream_authority":
            interventions["intervene_on_target_readout"]["observed_affected_nodes"] == ["prov_readout"],
        "source_deletion_revokes_authority_not_cached_output":
            interventions["delete_source_constructor"]["cached_output_may_survive"]
            and not interventions["delete_source_constructor"]["authority_survives"],
        "finite_interventions_identify_declared_mechanisms":
            mechanism_audits["finite_three_mechanism_identification"]["observation_matrix"]
            == [[1, 0, 1], [0, 1, 1], [1, 1, 0]]
            and mechanism_audits["finite_three_mechanism_identification"]["source_authorized_gauge_dimension"] == 0,
        "mechanism_identification_is_explicitly_bounded": all(
            audit["bounded_claim_scope"] and audit["no_universal_extrapolation"]
            for audit in packet["mechanism_identification_audits"]
        ),
        "stacky_mechanism_kernel_equals_authorized_gauge":
            mechanism_audits["finite_stacky_mechanism_identification"]["source_authorized_gauge_dimension"] == 1
            and len(mechanism_audits["finite_stacky_mechanism_identification"]["candidate_mechanisms"]) == 3
            and len(mechanism_audits["finite_stacky_mechanism_identification"]["intervention_ports"]) == 2,
        "atlas_refinement_preserves_global_reconstruction":
            refinements["refine_B_atlas_by_Bprime"]["reconstruction_defect"] == 0
            and refinements["refine_B_atlas_by_Bprime"]["authority_kind_before"]
            == refinements["refine_B_atlas_by_Bprime"]["authority_kind_after"],
        "counterfactual_deletion_separates_presentation_from_source":
            deletions["delete_redundant_Bprime"]["expected_process_survives"]
            and bool(deletions["delete_redundant_Bprime"]["source_derived_reconstruction"])
            and not deletions["delete_source_gluing_mechanism"]["expected_process_survives"]
            and deletions["delete_source_gluing_mechanism"]["surviving_global_grant"] is None,
        "missing_alternative_executor_is_presentation_only":
            representation_tests["kitaev_remove_logical_presentation"]["verdict"] == "presentation_only"
            and representation_tests["kitaev_remove_logical_presentation"].get("alternative_composition") is None
            and representation_tests["kitaev_remove_logical_presentation"].get("direct_grant") is None,
        "all_hostiles_rejected": all(item["passed"] for item in hostile_results.values()),
    }
    passed = all(gates.values())
    payload = {
        "schema": "marici.authority-grant-composition-checks.v1",
        "passed": passed,
        "passed_gates": sum(gates.values()),
        "total_gates": len(gates),
        "gates": gates,
        "hostile_passed": sum(item["passed"] for item in hostile_results.values()),
        "hostile_total": len(hostile_results),
        "hostile": hostile_results,
        "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        "hostile_fixture_sha256": hashlib.sha256(HOSTILES.read_bytes()).hexdigest(),
        "application_classification": {
            "grothendieck_folded_theta": "authority square commutes only with the explicit moving-endpoint seam/reflection coherence cell; result remains readout authority",
            "kitaev_logical_to_five_rail": "no composable authority map; conditional logical synthesis and rail-support evidence do not supply native coupler authority or encoded intertwining",
        },
        "representation_change_verdict": "A claimed explanation survives removal or replacement of B only when the induced A-to-C grant keeps its process signature and any non-identical presentation is joined by a source-derived invertible natural coherence cell. Otherwise it explains a presentation.",
        "descent_verdict": "Flat local presentation coherence is necessary but insufficient: the local grants must glue effectively and uniquely to a global authority grant, remain invariant under atlas refinement, and survive deletion only when an independent source reconstruction remains.",
        "provenance_verdict": "Even effective descent is explanatory only when every coherence and gluing witness is generated along an acyclic source-to-readout provenance order, independently of the desired target, and can be regenerated in a source-preserving replay.",
        "intervention_verdict": "A provenance graph becomes explanatory only when source interventions regenerate downstream coherence, target interventions leave upstream authority fixed, and source deletion revokes authority even if cached output persists.",
        "identification_verdict": "Interventions identify a mechanism only relative to a declared candidate family: the exact observation matrix must have no kernel beyond source-authorized gauge, the ports must be source-derived, and finite rank may not be extrapolated to a universal explanatory claim.",
        "verdict": "Authority grants form a partial category only on matching authority kind, variance, endpoints, and evidenced domains. Transport preserves kind, intersection restricts domains, extension requires fresh authority, and both triple composition and representation change require explicit zero-defect coherence.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="ascii")
    for name, value in gates.items():
        print(f"{'PASS' if value else 'FAIL'} gate.{name}: {value}")
    for name, value in hostile_results.items():
        print(f"{'PASS' if value['passed'] else 'FAIL'} hostile.{name}: {value['error_codes']}")
    print(f"SUMMARY {sum(gates.values())}/{len(gates)}; HOSTILE {sum(x['passed'] for x in hostile_results.values())}/{len(hostile_results)}")
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
