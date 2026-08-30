"""Standalone partial composition calculus for source-authority grants."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from typing import Any


AUTHORITY_KINDS = {
    "algebraic_faithfulness",
    "support",
    "readout",
    "observer",
    "executor",
    "constructor",
    "selector",
}
VARIANCES = {"covariant", "contravariant", "bivariant"}
COMPOSITION_MODES = {"transport", "domain_intersection", "authority_extension"}
CASE_CLASSES = {"strict_commuting_square", "coherence_cell_required", "no_composable_authority_map"}
REPRESENTATION_VERDICTS = {
    "process_explained_strictly",
    "process_explained_coherently",
    "presentation_only",
}


@dataclass(frozen=True)
class Error:
    code: str
    subject: str
    detail: str


def _signature(grant: dict[str, Any]) -> tuple[Any, ...]:
    return (
        grant.get("source_object"),
        grant.get("target_operation"),
        grant.get("target_object"),
        grant.get("authority_kind"),
        grant.get("evidence_domain"),
        grant.get("variance"),
    )


def _process_signature(grant: dict[str, Any]) -> tuple[Any, ...]:
    """Presentation-neutral boundary and authority type of a grant."""
    return (
        grant.get("source_object"),
        grant.get("target_object"),
        grant.get("authority_kind"),
        grant.get("variance"),
    )


def _exact_rank(matrix: list[list[int]]) -> int:
    """Exact Gaussian-elimination rank over Q for bounded audit matrices."""
    if not matrix:
        return 0
    width = len(matrix[0])
    if width == 0 or any(len(row) != width for row in matrix):
        return -1
    rows = [[Fraction(value) for value in row] for row in matrix]
    rank = 0
    for column in range(width):
        pivot = next((index for index in range(rank, len(rows)) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [value / scale for value in rows[rank]]
        for index in range(len(rows)):
            if index != rank and rows[index][column]:
                factor = rows[index][column]
                rows[index] = [value - factor * pivot_value for value, pivot_value in zip(rows[index], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def validate(packet: dict[str, Any]) -> list[Error]:
    errors: list[Error] = []
    domains = {item["id"]: item for item in packet.get("evidence_domains", [])}
    transformations = {item["id"]: item for item in packet.get("transformations", [])}
    grants = {item["id"]: item for item in packet.get("authority_grants", [])}
    compositions = {item["id"]: item for item in packet.get("compositions", [])}
    presentation_cells = {item["id"]: item for item in packet.get("presentation_coherence_cells", [])}
    provenance = packet.get("source_provenance", {})
    provenance_nodes = {item["id"]: item for item in provenance.get("nodes", [])}

    def err(code: str, subject: str, detail: str) -> None:
        errors.append(Error(code, subject, detail))

    for did, domain in domains.items():
        atoms = domain.get("atoms", [])
        if not domain.get("kind") or len(atoms) != len(set(atoms)):
            err("invalid_evidence_domain", did, str(domain))
        if not domain.get("authority_boundary"):
            err("missing_evidence_domain_boundary", did, "authority boundary required")

    for tid, transformation in transformations.items():
        if transformation.get("source_domain") not in domains or transformation.get("target_domain") not in domains:
            err("unknown_transformation_domain", tid, f"{transformation.get('source_domain')}->{transformation.get('target_domain')}")
        if transformation.get("variance") not in VARIANCES:
            err("invalid_transformation_variance", tid, str(transformation.get("variance")))
        if not transformation.get("evidence"):
            err("missing_transformation_evidence", tid, "transformation evidence required")

    for gid, grant in grants.items():
        if grant.get("authority_kind") not in AUTHORITY_KINDS:
            err("unknown_authority_kind", gid, str(grant.get("authority_kind")))
        if grant.get("evidence_domain") not in domains:
            err("unknown_grant_evidence_domain", gid, str(grant.get("evidence_domain")))
        if grant.get("variance") not in VARIANCES:
            err("invalid_grant_variance", gid, str(grant.get("variance")))
        for field in ("source_object", "target_operation", "target_object", "source_authority_evidence", "required_coherence_witness"):
            if not grant.get(field):
                err("untyped_authority_grant", gid, field)
        for tid in grant.get("admissible_transformations", []):
            if tid not in transformations:
                err("unknown_admissible_transformation", gid, tid)
        if grant.get("status") not in {"admitted", "identity"}:
            err("grant_not_admitted", gid, str(grant.get("status")))
        if grant.get("identity", False):
            if grant.get("source_object") != grant.get("target_object") or grant.get("target_operation") != "identity":
                err("invalid_authority_identity", gid, _signature(grant).__repr__())

    for cid, composition in compositions.items():
        left, right, result = (grants.get(composition.get(name)) for name in ("left", "right", "result"))
        if left is None or right is None or result is None:
            err("unknown_composition_grant", cid, f"{composition.get('left')},{composition.get('right')}->{composition.get('result')}")
            continue
        if left["target_object"] != right["source_object"]:
            err("authority_endpoint_mismatch", cid, f"{left['target_object']}!={right['source_object']}")
        if result["source_object"] != left["source_object"] or result["target_object"] != right["target_object"]:
            err("authority_composite_endpoint_defect", cid, _signature(result).__repr__())
        kinds = {left["authority_kind"], right["authority_kind"], result["authority_kind"]}
        if len(kinds) != 1:
            err("authority_kind_laundering", cid, "->".join([left["authority_kind"], right["authority_kind"], result["authority_kind"]]))
        variances = {left["variance"], right["variance"], result["variance"]}
        if len(variances) != 1:
            err("authority_variance_mismatch", cid, str(sorted(variances)))
        mode = composition.get("mode")
        if mode not in COMPOSITION_MODES:
            err("unknown_authority_composition_mode", cid, str(mode))
            continue
        if not composition.get("coherence_witness"):
            err("missing_authority_coherence", cid, "composition requires a coherence witness")
        left_atoms = set(domains[left["evidence_domain"]]["atoms"])
        right_atoms = set(domains[right["evidence_domain"]]["atoms"])
        result_atoms = set(domains[result["evidence_domain"]]["atoms"])
        if mode == "domain_intersection":
            if result_atoms != left_atoms & right_atoms:
                err("evidence_intersection_defect", cid, f"{sorted(result_atoms)} != {sorted(left_atoms & right_atoms)}")
        elif mode == "transport":
            transformation = transformations.get(composition.get("transformation"))
            if transformation is None:
                err("missing_authority_transport", cid, str(composition.get("transformation")))
                continue
            if transformation["id"] not in left.get("admissible_transformations", []):
                err("inadmissible_authority_transport", cid, transformation["id"])
            if not transformation.get("preserves_evidence"):
                err("transport_destroys_evidence", cid, transformation["id"])
            if not transformation.get("preserves_authority"):
                err("base_change_preserves_evidence_not_authority", cid, transformation["id"])
            mapping = transformation.get("atom_map", {})
            mapped = {mapping[atom] for atom in left_atoms if atom in mapping}
            if result_atoms != mapped & right_atoms:
                err("transported_evidence_domain_defect", cid, f"{sorted(result_atoms)} != {sorted(mapped & right_atoms)}")
            if transformation.get("variance") != left["variance"]:
                err("authority_variance_mismatch", cid, f"{transformation.get('variance')}!={left['variance']}")
        elif mode == "authority_extension":
            if not composition.get("extension_authority") or not composition.get("new_atom_evidence"):
                err("unauthorized_authority_extension", cid, "extension authority and new-atom evidence required")
            if not result_atoms.issuperset(left_atoms | right_atoms):
                err("authority_extension_domain_defect", cid, f"{sorted(result_atoms)} lacks {sorted(left_atoms | right_atoms)}")

    for cell in packet.get("associativity_cells", []):
        left = compositions.get(cell.get("left_factorization"))
        right = compositions.get(cell.get("right_factorization"))
        if left is None or right is None:
            err("unknown_associativity_factorization", cell["id"], f"{cell.get('left_factorization')}|{cell.get('right_factorization')}")
            continue
        left_result, right_result = grants[left["result"]], grants[right["result"]]
        if _signature(left_result) != _signature(right_result):
            err("factorization_dependent_composite", cell["id"], f"{_signature(left_result)} != {_signature(right_result)}")
        if cell.get("variance") != left_result["variance"] or cell.get("variance") != right_result["variance"]:
            err("associativity_variance_mismatch", cell["id"], str(cell.get("variance")))
        if not cell.get("triple_coherence_witness") or cell.get("coherence_defect") != 0:
            err("triple_authority_coherence_failure", cell["id"], str(cell.get("coherence_defect")))

    for law in packet.get("identity_laws", []):
        composition = compositions.get(law.get("composition"))
        grant = grants.get(law.get("grant"))
        if composition is None or grant is None:
            err("unknown_identity_law", law["id"], str(law))
            continue
        result = grants[composition["result"]]
        if _signature(result) != _signature(grant):
            err("authority_identity_law_defect", law["id"], f"{_signature(result)} != {_signature(grant)}")

    for case in packet.get("application_cases", []):
        classification = case.get("classification")
        if classification not in CASE_CLASSES:
            err("unknown_application_classification", case["id"], str(classification))
        if classification == "strict_commuting_square":
            composition = compositions.get(case.get("composition"))
            if composition is None or composition.get("coherence_witness") != "identity_cell":
                err("application_not_strict", case["id"], str(case.get("composition")))
        elif classification == "coherence_cell_required":
            composition = compositions.get(case.get("composition"))
            if composition is None or not case.get("explicit_coherence_cell") or composition.get("coherence_witness") == "identity_cell":
                err("application_missing_explicit_cell", case["id"], str(case.get("explicit_coherence_cell")))
        elif classification == "no_composable_authority_map":
            if case.get("composition") is not None or not case.get("obstruction_evidence"):
                err("false_application_composability", case["id"], str(case.get("composition")))

    for cell_id, cell in presentation_cells.items():
        for field in ("source_presentation", "target_presentation", "authority_kind", "variance", "evidence"):
            if not cell.get(field):
                err("untyped_presentation_coherence_cell", cell_id, field)
        if cell.get("authority_kind") not in AUTHORITY_KINDS:
            err("unknown_authority_kind", cell_id, str(cell.get("authority_kind")))
        if cell.get("variance") not in VARIANCES:
            err("invalid_grant_variance", cell_id, str(cell.get("variance")))
        if not cell.get("source_derived") or not cell.get("invertible") or not cell.get("preserves_authority_kind"):
            err("invalid_presentation_coherence_cell", cell_id, str(cell))
        if cell.get("naturality_defect") != 0:
            err("presentation_coherence_naturality_failure", cell_id, str(cell.get("naturality_defect")))
        pnode = provenance_nodes.get(cell.get("provenance_node"))
        if pnode is None or pnode.get("role") != "coherence_witness":
            err("missing_coherence_source_provenance", cell_id, str(cell.get("provenance_node")))
        if not cell.get("derived_before_target"):
            err("target_fitted_coherence", cell_id, "coherence was selected after the target")
        if not cell.get("target_independent"):
            err("target_dependent_coherence", cell_id, "coherence changes with desired output")
        if not cell.get("counterfactual_recomputable"):
            err("cached_not_explanatory_coherence", cell_id, "witness cannot be regenerated after a source-preserving replay")

    # Provenance is directed explanatory data, not a bag of citations.  Every
    # derived node must be reachable from a source constructor along strictly
    # forward, source-derived edges; cycles are forbidden.
    provenance_roles = {"source_constructor", "local_mechanism", "coherence_witness", "global_authority", "readout"}
    adjacency = {node_id: [] for node_id in provenance_nodes}
    indegree = {node_id: 0 for node_id in provenance_nodes}
    for node_id, node in provenance_nodes.items():
        if node.get("role") not in provenance_roles or not isinstance(node.get("stage"), int):
            err("invalid_source_provenance_node", node_id, str(node))
    for edge in provenance.get("edges", []):
        eid = edge["id"]
        source = provenance_nodes.get(edge.get("source"))
        target = provenance_nodes.get(edge.get("target"))
        if source is None or target is None:
            err("unknown_source_provenance_endpoint", eid, f"{edge.get('source')}->{edge.get('target')}")
            continue
        adjacency[source["id"]].append(target["id"])
        indegree[target["id"]] += 1
        if not edge.get("source_derived") or source["stage"] >= target["stage"]:
            err("provenance_stage_violation", eid, f"{source['stage']}!<{target['stage']}")
    queue = [node_id for node_id, degree in indegree.items() if degree == 0]
    visited = []
    while queue:
        node_id = queue.pop()
        visited.append(node_id)
        for target_id in adjacency[node_id]:
            indegree[target_id] -= 1
            if indegree[target_id] == 0:
                queue.append(target_id)
    if len(visited) != len(provenance_nodes):
        err("cyclic_explanatory_provenance", provenance.get("id", "source_provenance"), str(sorted(set(provenance_nodes) - set(visited))))
    roots = {node_id for node_id, node in provenance_nodes.items() if node.get("role") == "source_constructor"}
    reachable = set(roots)
    frontier = list(roots)
    while frontier:
        node_id = frontier.pop()
        for target_id in adjacency.get(node_id, []):
            if target_id not in reachable:
                reachable.add(target_id)
                frontier.append(target_id)
    for node_id, node in provenance_nodes.items():
        if node.get("role") != "source_constructor" and node_id not in reachable:
            err("authority_not_source_reachable", node_id, node.get("role", "unknown"))

    for intervention in packet.get("source_intervention_tests", []):
        iid = intervention["id"]
        kind = intervention.get("kind")
        affected = set(intervention.get("observed_affected_nodes", []))
        if not affected.issubset(provenance_nodes):
            err("unknown_intervention_effect_node", iid, str(sorted(affected - set(provenance_nodes))))
        if kind == "source_perturbation":
            required = set(intervention.get("required_downstream_response", []))
            if not required or not required.issubset(affected):
                err("source_perturbation_fails_to_regenerate_witnesses", iid, str(sorted(required - affected)))
            if not intervention.get("fresh_recomputation"):
                err("cached_source_intervention_response", iid, "fresh recomputation required")
        elif kind == "target_perturbation":
            upstream = {node_id for node_id in affected if provenance_nodes[node_id]["role"] != "readout"}
            if upstream:
                err("target_intervention_changes_upstream_authority", iid, str(sorted(upstream)))
        elif kind == "source_deletion":
            if intervention.get("authority_survives"):
                err("authority_survives_deleted_constructor", iid, "cached output cannot retain authority")
            if not intervention.get("cached_output_may_survive"):
                err("source_deletion_test_erases_output_distinction", iid, "test must distinguish cached output from authority")
        else:
            err("unknown_source_intervention_kind", iid, str(kind))

    # Interventions explain only relative to the alternatives they separate.
    # Exact rank computes the unresolved mechanism kernel; only a declared,
    # source-authorized gauge quotient may absorb that nullity.
    for audit in packet.get("mechanism_identification_audits", []):
        aid = audit["id"]
        candidates = audit.get("candidate_mechanisms", [])
        ports = audit.get("intervention_ports", [])
        matrix = audit.get("observation_matrix", [])
        rank = _exact_rank(matrix)
        if rank < 0 or len(matrix) != len(ports) or (matrix and len(matrix[0]) != len(candidates)):
            err("invalid_mechanism_observation_matrix", aid, f"{len(matrix)}x{len(matrix[0]) if matrix else 0}")
            continue
        nullity = len(candidates) - rank
        gauge_dimension = audit.get("source_authorized_gauge_dimension", 0)
        if nullity != gauge_dimension:
            err("intervention_family_not_jointly_faithful", aid, f"nullity={nullity}, authorized_gauge={gauge_dimension}")
        if not audit.get("source_derived_ports"):
            err("target_fitted_intervention_family", aid, "ports lack independent source derivation")
        if not audit.get("bounded_claim_scope") or not audit.get("no_universal_extrapolation"):
            err("unbounded_explanatory_extrapolation", aid, str(audit.get("bounded_claim_scope")))

    rival_admissions = {item["id"]: item for item in packet.get("rival_admissions", [])}
    for admission_id, admission in rival_admissions.items():
        status = admission.get("status")
        if status not in {"admitted", "rejected", "pending"}:
            err("unknown_rival_admission_status", admission_id, str(status))
            continue
        complete = all(
            admission.get(field)
            for field in (
                "mechanism_id",
                "proposer_source",
                "constructor_grammar",
                "admissible_domain",
                "falsifiable_difference",
            )
        )
        admissible = bool(
            complete
            and admission.get("independent_of_incumbent_fit")
            and admission.get("predicts_all_existing_ports")
            and admission.get("non_gauge_witness")
            and admission.get("admitted_before_response_selection")
        )
        if status == "admitted" and not admissible:
            if not admission.get("non_gauge_witness"):
                err("gauge_duplicate_misclassified_as_rival", admission_id, admission.get("mechanism_id", "unknown"))
            elif not admission.get("predicts_all_existing_ports"):
                err("port_incomplete_rival_admission", admission_id, admission.get("mechanism_id", "unknown"))
            elif not admission.get("independent_of_incumbent_fit") or not admission.get("admitted_before_response_selection"):
                err("target_fitted_rival_admission", admission_id, admission.get("mechanism_id", "unknown"))
            else:
                err("untyped_rival_admission", admission_id, str(admission))
        if status == "rejected" and admissible:
            err("admissible_rival_improperly_rejected", admission_id, admission.get("mechanism_id", "unknown"))

    # Admission is itself authority-bearing.  The incumbent may submit evidence,
    # but cannot be the sole adjudicator of its own rival.  Review operates on a
    # frozen content packet under criteria fixed before the response is inspected;
    # it grants challenge standing, never a stronger operative authority kind.
    root_certifications = {item["id"]: item for item in packet.get("review_authority_root_certifications", [])}
    for root_id, root in root_certifications.items():
        for field in ("holder", "issuing_charter", "provenance_chain", "jurisdiction", "authority_kind"):
            if not root.get(field):
                err("uncertified_review_authority_root", root_id, field)
        if root.get("issuing_charter") == root_id or root_id in root.get("provenance_chain", []):
            err("self_authorized_review_root", root_id, str(root.get("provenance_chain")))
        if root.get("authority_kind") != "procedural_review" or root.get("operative_authority_ceiling") != "challenge_standing":
            err("review_root_scope_laundering", root_id, f"{root.get('authority_kind')}:{root.get('operative_authority_ceiling')}")
        if not root.get("revocable") or root.get("may_select_mechanism_truth") is not False:
            err("unbounded_review_authority_root", root_id, str(root))
        if not isinstance(root.get("valid_from"), int):
            err("untyped_review_root_validity_interval", root_id, str(root.get("valid_from")))
        revoked_at = root.get("revoked_at")
        if revoked_at is not None and (not isinstance(revoked_at, int) or revoked_at <= root.get("valid_from", revoked_at)):
            err("untyped_review_root_validity_interval", root_id, str(revoked_at))

    reviews = {item["id"]: item for item in packet.get("rival_admission_reviews", [])}
    reviewed_admissions: set[str] = set()
    for review_id, review in reviews.items():
        admission = rival_admissions.get(review.get("admission_id"))
        if admission is None:
            err("unknown_reviewed_rival_admission", review_id, str(review.get("admission_id")))
            continue
        reviewed_admissions.add(admission["id"])
        proposer = review.get("proposer")
        incumbent = review.get("incumbent")
        reviewers = review.get("reviewers", [])
        appeal_reviewers = review.get("appeal_reviewers", [])
        roots = review.get("reviewer_authority_roots", [])
        appeal_roots = review.get("appeal_authority_roots", [])
        if not reviewers or incumbent in reviewers or proposer in reviewers:
            err("incumbent_or_proposer_controls_rival_admission", review_id, str(reviewers))
        if len(roots) != len(reviewers) or len(set(roots)) != len(roots):
            err("nonindependent_rival_review_authority", review_id, str(roots))
        if any(root not in root_certifications for root in roots + appeal_roots):
            err("uncertified_review_authority_root", review_id, str(roots + appeal_roots))
        else:
            if any(root_certifications[root].get("holder") != reviewer for root, reviewer in zip(roots, reviewers)):
                err("reviewer_root_holder_mismatch", review_id, str(roots))
            if len(appeal_roots) != len(appeal_reviewers) or any(
                root_certifications[root].get("holder") != reviewer
                or root_certifications[root].get("jurisdiction") != "rival_admission_appeal"
                for root, reviewer in zip(appeal_roots, appeal_reviewers)
            ):
                err("invalid_appeal_authority_root", review_id, str(appeal_roots))
        if not review.get("criteria_committed_before_response"):
            err("target_fitted_rival_review", review_id, "review criteria were not precommitted")
        if not review.get("immutable_evidence_packet_sha256"):
            err("mutable_rival_review_packet", review_id, "content-addressed evidence packet required")
        if not review.get("appeal_available") or not appeal_reviewers or set(appeal_reviewers) & set(reviewers):
            err("missing_independent_rival_appeal", review_id, str(appeal_reviewers))
        if review.get("decision") != admission.get("status"):
            err("rival_review_decision_mismatch", review_id, f"{review.get('decision')}!={admission.get('status')}")
        if review.get("authority_kind_before") != review.get("authority_kind_after"):
            err("rival_review_authority_laundering", review_id, f"{review.get('authority_kind_before')}->{review.get('authority_kind_after')}")
        if review.get("grants_only_challenge_standing") is not True:
            err("rival_review_grants_operative_authority", review_id, str(review.get("grants_only_challenge_standing")))
        reviewed_at = review.get("reviewed_at")
        if not isinstance(reviewed_at, int):
            err("untyped_rival_review_time", review_id, str(reviewed_at))
        else:
            for root_id in roots + appeal_roots:
                root = root_certifications.get(root_id)
                if root and (reviewed_at < root.get("valid_from", reviewed_at) or (
                    root.get("revoked_at") is not None and reviewed_at >= root["revoked_at"]
                )):
                    err("rival_review_outside_root_validity", review_id, f"{root_id}@{reviewed_at}")

    for admission_id in rival_admissions:
        if admission_id not in reviewed_admissions:
            err("rival_admission_without_governance_review", admission_id, "every disposition requires an independent review trace")

    for audit in packet.get("proposer_identity_invariance_audits", []):
        aid = audit["id"]
        if audit.get("packet_sha256_left") != audit.get("packet_sha256_right"):
            err("identity_audit_compares_different_rival_packets", aid, "packet digests differ")
        if audit.get("decision_left") != audit.get("decision_right"):
            err("proposer_identity_bias", aid, f"{audit.get('decision_left')}!={audit.get('decision_right')}")
        if not audit.get("identity_blinded_during_merits_review"):
            err("unblinded_rival_merits_review", aid, "proposer identity exposed during merits review")

    for audit in packet.get("review_root_independence_audits", []):
        aid = audit["id"]
        roots = audit.get("roots", [])
        if len(roots) < 2 or any(root not in root_certifications for root in roots):
            err("invalid_review_root_independence_audit", aid, str(roots))
        if audit.get("shared_controlling_ancestors"):
            err("review_roots_share_controlling_authority", aid, str(audit.get("shared_controlling_ancestors")))
        if not audit.get("source_derived_comparison") or audit.get("coherence_defect") != 0:
            err("uncertified_review_root_independence", aid, str(audit.get("coherence_defect")))

    # Revocation changes prospective authority, not the historical audit fact.
    # Restoration requires replay of the same frozen packet through roots valid
    # at replay time; a cached decision is evidence but carries no live standing.
    for audit in packet.get("temporal_review_authority_audits", []):
        aid = audit["id"]
        review = reviews.get(audit.get("original_review"))
        revoked_root = root_certifications.get(audit.get("revoked_root"))
        revoked_at = audit.get("revoked_at")
        if review is None or revoked_root is None or not isinstance(revoked_at, int):
            err("untyped_temporal_review_audit", aid, str(audit))
            continue
        if revoked_at <= review.get("reviewed_at", revoked_at):
            err("backdated_review_root_revocation", aid, f"{revoked_at}<={review.get('reviewed_at')}")
        if not audit.get("historical_decision_preserved"):
            err("revocation_erases_historical_review", aid, review["id"])
        if audit.get("prospective_authority_before_replay"):
            err("revoked_root_leaves_cached_authority_live", aid, revoked_root["id"])
        if not audit.get("replay_required"):
            err("standing_restored_without_review_replay", aid, "replay requirement absent")
        if audit.get("replay_packet_sha256") != review.get("immutable_evidence_packet_sha256"):
            err("review_replay_changes_evidence_packet", aid, str(audit.get("replay_packet_sha256")))
        replayed_at = audit.get("replayed_at")
        replay_roots = audit.get("replay_roots", [])
        roots_live = isinstance(replayed_at, int) and bool(replay_roots)
        for root_id in replay_roots:
            root = root_certifications.get(root_id)
            roots_live = bool(roots_live and root and replayed_at >= root.get("valid_from", replayed_at) and (
                root.get("revoked_at") is None or replayed_at < root["revoked_at"]
            ))
        if not roots_live:
            err("review_replay_uses_inactive_root", aid, str(replay_roots))
        restored = bool(audit.get("prospective_authority_after_replay"))
        if restored != bool(roots_live and audit.get("replay_required") and audit.get("replay_completed")):
            err("invalid_temporal_authority_restoration", aid, str(restored))

    # A temporal replay atlas is flat only when independently rooted replay
    # paths on the same packet have the same disposition.  A higher appeal cell
    # may compare or restart procedures, but cannot coerce disagreement into
    # consensus or acquire truth-selection authority.
    for atlas in packet.get("temporal_replay_atlas_audits", []):
        aid = atlas["id"]
        original = reviews.get(atlas.get("original_review"))
        paths = atlas.get("paths", [])
        if original is None or len(paths) < 2:
            err("untyped_temporal_replay_atlas", aid, str(atlas.get("original_review")))
            continue
        path_root_sets: list[set[str]] = []
        decisions = []
        for path in paths:
            roots = path.get("roots", [])
            replayed_at = path.get("replayed_at")
            path_root_sets.append(set(roots))
            decisions.append(path.get("decision"))
            if path.get("packet_sha256") != original.get("immutable_evidence_packet_sha256"):
                err("temporal_atlas_packet_mismatch", path.get("id", aid), str(path.get("packet_sha256")))
            if not path.get("completed") or not isinstance(replayed_at, int) or not roots:
                err("incomplete_temporal_replay_path", path.get("id", aid), str(path))
                continue
            for root_id in roots:
                root = root_certifications.get(root_id)
                if root is None or replayed_at < root.get("valid_from", replayed_at) or (
                    root.get("revoked_at") is not None and replayed_at >= root["revoked_at"]
                ):
                    err("temporal_atlas_uses_inactive_root", path.get("id", aid), root_id)
        for left_index in range(len(path_root_sets)):
            for right_index in range(left_index + 1, len(path_root_sets)):
                if path_root_sets[left_index] & path_root_sets[right_index]:
                    err("temporal_replay_paths_not_independently_rooted", aid, str(sorted(path_root_sets[left_index] & path_root_sets[right_index])))
        if not atlas.get("comparison_committed_before_replay") or not atlas.get("source_derived_path_comparison"):
            err("target_fitted_temporal_path_comparison", aid, "comparison law must precede replay")
        disagreement = len(set(decisions)) != 1
        if disagreement or atlas.get("disposition_defect") != 0:
            err("unresolved_governance_holonomy", aid, str(decisions))
            if atlas.get("prospective_authority_restored"):
                err("authority_restored_across_governance_holonomy", aid, str(decisions))
        elif not atlas.get("prospective_authority_restored"):
            err("flat_temporal_atlas_withholds_authority", aid, str(decisions))
        cell = atlas.get("higher_appeal_cell", {})
        appeal_root = root_certifications.get(cell.get("authority_root"))
        if appeal_root is None or appeal_root.get("jurisdiction") != "rival_admission_appeal":
            err("uncertified_temporal_higher_cell", aid, str(cell.get("authority_root")))
        if cell.get("role") != "compare_procedure_not_truth" or cell.get("may_override_disagreement") is not False:
            err("temporal_higher_cell_launders_truth_authority", aid, str(cell))

    temporal_atlases = {item["id"]: item for item in packet.get("temporal_replay_atlas_audits", [])}
    for cocycle in packet.get("temporal_governance_cocycle_audits", []):
        cid = cocycle["id"]
        atlas = temporal_atlases.get(cocycle.get("atlas_id"))
        cells = {item["id"]: item for item in cocycle.get("comparison_cells", [])}
        if atlas is None or len(atlas.get("paths", [])) < 3 or len(cells) < 3:
            err("incomplete_temporal_governance_cocycle", cid, str(cocycle.get("atlas_id")))
            continue
        path_ids = {path["id"] for path in atlas["paths"]}
        for cell_id, cell in cells.items():
            if cell.get("source_path") not in path_ids or cell.get("target_path") not in path_ids:
                err("unknown_temporal_comparison_endpoint", cell_id, f"{cell.get('source_path')}->{cell.get('target_path')}")
            if not cell.get("invertible") or not cell.get("source_derived") or not cell.get("committed_before_replay"):
                err("invalid_temporal_comparison_cell", cell_id, str(cell))
            if cell.get("authority_kind") != "procedural_review" or cell.get("may_select_truth") is not False:
                err("temporal_comparison_cell_launders_authority", cell_id, str(cell.get("authority_kind")))
            if cell.get("packet_sha256") != atlas["paths"][0].get("packet_sha256"):
                err("temporal_comparison_packet_mismatch", cell_id, str(cell.get("packet_sha256")))
            if cell.get("naturality_defect") != 0:
                err("temporal_comparison_naturality_failure", cell_id, str(cell.get("naturality_defect")))
        direct = cells.get(cocycle.get("direct_cell"))
        composite_ids = cocycle.get("composite_path", [])
        composite = [cells.get(cell_id) for cell_id in composite_ids]
        if direct is None or len(composite) < 2 or any(cell is None for cell in composite):
            err("incomplete_temporal_governance_cocycle", cid, str(composite_ids))
            continue
        composable = all(composite[index]["target_path"] == composite[index + 1]["source_path"] for index in range(len(composite) - 1))
        same_boundary = direct["source_path"] == composite[0]["source_path"] and direct["target_path"] == composite[-1]["target_path"]
        if not composable or not same_boundary:
            err("noncomposable_temporal_governance_cocycle", cid, str(composite_ids))
        if cocycle.get("cocycle_defect") != 0:
            err("temporal_governance_cocycle_failure", cid, str(cocycle.get("cocycle_defect")))
            if cocycle.get("global_standing_restored"):
                err("standing_restored_across_temporal_cocycle_defect", cid, str(cocycle.get("cocycle_defect")))
        elif not cocycle.get("global_standing_restored"):
            err("flat_temporal_cocycle_withholds_standing", cid, "zero cocycle defect")

    # Open-world DPC: a new admitted rival reopens identification unless the current
    # source-derived ports separate the enlarged family.  New authority is
    # earned only after a source-derived discriminator closes the new kernel.
    for challenge in packet.get("rival_extension_audits", []):
        cid = challenge["id"]
        candidates = challenge.get("candidate_mechanisms", [])
        ports = challenge.get("intervention_ports", [])
        matrix = challenge.get("observation_matrix", [])
        rank = _exact_rank(matrix)
        if rank < 0 or len(matrix) != len(ports) or (matrix and len(matrix[0]) != len(candidates)):
            err("invalid_rival_extension_matrix", cid, f"{len(matrix)}x{len(matrix[0]) if matrix else 0}")
            continue
        nullity = len(candidates) - rank
        gauge = challenge.get("source_authorized_gauge_dimension", 0)
        status = challenge.get("status")
        admission = rival_admissions.get(challenge.get("new_rival_admission"))
        if admission is None or admission.get("status") != "admitted":
            err("rival_challenge_without_admission_authority", cid, str(challenge.get("new_rival_admission")))
        elif admission.get("mechanism_id") not in candidates:
            err("admitted_rival_missing_from_candidate_family", cid, admission.get("mechanism_id", "unknown"))
        if challenge.get("claims_closed_under_all_future_rivals"):
            err("closed_world_explanation_claim", cid, "finite audit cannot quantify over ungenerated rivals")
        if status == "challenge_open":
            if nullity <= gauge:
                err("spurious_open_rival_challenge", cid, f"nullity={nullity}")
            if challenge.get("identification_authority_retained"):
                err("authority_retained_with_unresolved_rival", cid, f"nullity={nullity}")
        elif status == "revalidated":
            if nullity != gauge:
                err("rival_repair_not_jointly_faithful", cid, f"nullity={nullity}, gauge={gauge}")
            if not challenge.get("new_discriminator_source_derived"):
                err("target_fitted_rival_discriminator", cid, "new port lacks source derivation")
            if not challenge.get("identification_authority_retained"):
                err("revalidated_rival_audit_withholds_authority", cid, "full quotient rank achieved")
        else:
            err("unknown_rival_extension_status", cid, str(status))

    for atlas in packet.get("presentation_atlas_coherence", []):
        aid = atlas["id"]
        path_signatures = []
        for path in atlas.get("paths", []):
            cells = [presentation_cells.get(cell_id) for cell_id in path]
            if not cells or any(cell is None for cell in cells):
                err("unknown_presentation_coherence_path", aid, str(path))
                continue
            composable = all(cells[index]["target_presentation"] == cells[index + 1]["source_presentation"] for index in range(len(cells) - 1))
            kinds = {cell["authority_kind"] for cell in cells}
            variances = {cell["variance"] for cell in cells}
            if not composable or len(kinds) != 1 or len(variances) != 1:
                err("noncomposable_presentation_coherence_path", aid, str(path))
                continue
            path_signatures.append((cells[0]["source_presentation"], cells[-1]["target_presentation"], next(iter(kinds)), next(iter(variances))))
        if not path_signatures or len(set(path_signatures)) != 1:
            err("presentation_atlas_factorization_defect", aid, str(path_signatures))
        if not atlas.get("source_derived_comparison") or atlas.get("holonomy_defect") != 0:
            err("presentation_atlas_holonomy_failure", aid, str(atlas.get("holonomy_defect")))

    # Flat descent data need not be effective: local process presentations may
    # satisfy every cocycle while failing to reconstruct a unique global grant.
    for descent in packet.get("authority_descent_objects", []):
        did = descent["id"]
        atlas = next((item for item in packet.get("presentation_atlas_coherence", []) if item["id"] == descent.get("atlas_id")), None)
        local_grants = [grants.get(gid) for gid in descent.get("local_grants", [])]
        global_grant = grants.get(descent.get("global_grant"))
        if atlas is None or not local_grants or any(grant is None for grant in local_grants) or global_grant is None:
            err("untyped_authority_descent_object", did, "atlas, local grants, and global grant are required")
            continue
        signatures = {_process_signature(grant) for grant in [*local_grants, global_grant]}
        if len(signatures) != 1:
            err("descent_changes_process_signature", did, str(signatures))
        if not descent.get("source_derived_gluing") or not descent.get("effective") or descent.get("reconstruction_defect") != 0:
            err("flat_but_noneffective_authority_descent", did, str(descent.get("reconstruction_defect")))
        ambiguity_rank = descent.get("ambiguity_kernel_rank")
        if ambiguity_rank != 0:
            if not descent.get("stabilizer_quotient_declared") or descent.get("quotient_ambiguity_rank") != 0:
                err("nonunique_global_authority_descent", did, str(ambiguity_rank))
        stabilizer = set(descent.get("stabilizer", []))
        authorized = set(descent.get("source_authorized_stabilizer", []))
        if not stabilizer or not stabilizer.issubset(authorized):
            err("unauthorized_descent_stabilizer", did, str(sorted(stabilizer - authorized)))

    # Refining an atlas is a higher coherence operation: reconstruction before
    # and after refinement must agree, not merely every pairwise overlap.
    for refinement in packet.get("presentation_refinement_coherence", []):
        rid = refinement["id"]
        if not refinement.get("source_derived_refinement") or refinement.get("reconstruction_defect") != 0:
            err("presentation_refinement_coherence_failure", rid, str(refinement.get("reconstruction_defect")))
        if refinement.get("authority_kind_before") != refinement.get("authority_kind_after"):
            err("refinement_strengthens_authority", rid, f"{refinement.get('authority_kind_before')}->{refinement.get('authority_kind_after')}")

    # Counterfactual deletion distinguishes redundant presentation scaffolding
    # from a source mechanism on which the process genuinely depends.
    for deletion in packet.get("presentation_deletion_tests", []):
        did = deletion["id"]
        survivor = grants.get(deletion.get("surviving_global_grant"))
        if deletion.get("expected_process_survives"):
            if survivor is None or not deletion.get("source_derived_reconstruction"):
                err("unsupported_presentation_deletion_survival", did, str(deletion.get("surviving_global_grant")))
            elif survivor["authority_kind"] != deletion.get("authority_kind_before"):
                err("deletion_strengthens_authority", did, f"{deletion.get('authority_kind_before')}->{survivor['authority_kind']}")
        elif survivor is not None:
            err("false_source_deletion_independence", did, survivor["id"])

    # DPC representation-change test.  A process survives replacement/removal
    # of an intermediate presentation only if its boundary authority is
    # unchanged.  Non-identical presentations additionally require a
    # source-derived, invertible, natural coherence cell.
    for test in packet.get("representation_change_tests", []):
        tid = test["id"]
        verdict = test.get("verdict")
        if verdict not in REPRESENTATION_VERDICTS:
            err("unknown_representation_test_verdict", tid, str(verdict))
            continue
        baseline = compositions.get(test.get("baseline_composition"))
        baseline_grant = grants.get(test.get("baseline_grant"))
        alternative = compositions.get(test.get("alternative_composition"))
        direct = grants.get(test.get("direct_grant"))
        if baseline is None and baseline_grant is None:
            err("missing_baseline_factorization", tid, str(test.get("baseline_composition") or test.get("baseline_grant")))
            continue
        baseline_result = grants[baseline["result"]] if baseline is not None else baseline_grant
        candidate = grants[alternative["result"]] if alternative is not None else direct
        if candidate is None:
            if verdict != "presentation_only":
                err("representation_removal_destroys_composite", tid, "no alternative composition or direct source grant")
            continue
        same_process = _process_signature(baseline_result) == _process_signature(candidate)
        strengthened = baseline_result["authority_kind"] != candidate["authority_kind"]
        if strengthened:
            err("representation_change_strengthens_authority", tid, f"{baseline_result['authority_kind']}->{candidate['authority_kind']}")
        if not same_process:
            err("representation_dependent_process_signature", tid, f"{_process_signature(baseline_result)} != {_process_signature(candidate)}")
        cell = presentation_cells.get(test.get("coherence_cell_id")) or test.get("coherence_cell")
        presentation_changed = test.get("intermediate_before") != test.get("intermediate_after")
        coherent = bool(
            cell
            and cell.get("source_derived")
            and cell.get("invertible")
            and cell.get("preserves_authority_kind")
            and cell.get("naturality_defect") == 0
        )
        if verdict == "process_explained_strictly":
            if _signature(baseline_result) != _signature(candidate):
                err("false_strict_representation_invariance", tid, "strict verdict requires the same full grant signature")
        elif verdict == "process_explained_coherently":
            if not presentation_changed or not same_process or not coherent:
                err("missing_source_derived_representation_coherence", tid, str(cell))
        elif verdict == "presentation_only" and same_process and (not presentation_changed or coherent):
            err("false_presentation_only_verdict", tid, "an invariant source-coherent composite exists")

    # Finite proof-carrying compression.  The certificate is a replayable DAG
    # over typed bundles, not a hash promoted into authority.  Minimality is
    # relative to the declared constructor grammar and witnessed by deletion.
    object_registry: set[str] = set()
    for collection in (
        "rival_admissions",
        "rival_admission_reviews",
        "review_authority_root_certifications",
        "temporal_replay_atlas_audits",
        "temporal_governance_cocycle_audits",
    ):
        object_registry.update(item["id"] for item in packet.get(collection, []))
    stack_certificates = {item["id"]: item for item in packet.get("finite_authority_stack_certificates", [])}
    for certificate in stack_certificates.values():
        sid = certificate["id"]
        generators = certificate.get("generators", [])
        generator_ids = {item.get("id") for item in generators}
        if not generators or len(generator_ids) != len(generators):
            err("invalid_authority_certificate_generator_basis", sid, str(generator_ids))
        for generator in generators:
            if generator.get("object_ref") not in object_registry or not generator.get("role"):
                err("unknown_authority_certificate_generator", generator.get("id", sid), str(generator.get("object_ref")))
        if not certificate.get("bounded_constructor_grammar") or certificate.get("claims_absolute_minimality") is not False:
            err("unbounded_authority_certificate_minimality", sid, str(certificate.get("bounded_constructor_grammar")))
        if certificate.get("digest_confers_authority") is not False:
            err("authority_by_certificate_digest", sid, str(certificate.get("digest_confers_authority")))
        if not certificate.get("deterministic_replay_checker") or not certificate.get("replay_checker_sha256"):
            err("nonreplayable_authority_stack_certificate", sid, "checker and artifact digest required")
        nodes = {item["id"]: item for item in certificate.get("dependency_nodes", [])}
        terminal = certificate.get("terminal_claim_node")
        adjacency = {node_id: [] for node_id in nodes}
        indegree = {node_id: 0 for node_id in nodes}
        for edge in certificate.get("dependency_edges", []):
            source, target = edge.get("source"), edge.get("target")
            if source not in nodes or target not in nodes:
                err("unknown_authority_certificate_dependency", edge.get("id", sid), f"{source}->{target}")
                continue
            adjacency[source].append(target)
            indegree[target] += 1
        queue = [node_id for node_id, degree in indegree.items() if degree == 0]
        roots = set(queue)
        visited = []
        while queue:
            node_id = queue.pop()
            visited.append(node_id)
            for target in adjacency[node_id]:
                indegree[target] -= 1
                if indegree[target] == 0:
                    queue.append(target)
        if len(visited) != len(nodes):
            err("cyclic_authority_certificate_dependencies", sid, str(sorted(set(nodes) - set(visited))))
        if roots != generator_ids or terminal not in nodes:
            err("authority_certificate_boundary_mismatch", sid, f"roots={sorted(roots)}, generators={sorted(generator_ids)}")
        reverse = {node_id: [] for node_id in nodes}
        for source, targets in adjacency.items():
            for target in targets:
                reverse[target].append(source)
        ancestors = {terminal} if terminal in nodes else set()
        frontier = list(ancestors)
        while frontier:
            node_id = frontier.pop()
            for source in reverse.get(node_id, []):
                if source not in ancestors:
                    ancestors.add(source)
                    frontier.append(source)
        if not generator_ids.issubset(ancestors):
            err("redundant_authority_certificate_generator", sid, str(sorted(generator_ids - ancestors)))
        witnesses = {item.get("generator_id"): item for item in certificate.get("minimality_witnesses", [])}
        if set(witnesses) != generator_ids or any(
            not witness.get("deletion_breaks_terminal_claim") or not witness.get("expected_failure_code")
            for witness in witnesses.values()
        ):
            err("incomplete_authority_certificate_minimality_witness", sid, str(sorted(set(witnesses) ^ generator_ids)))

    # Capability execution closes the time-of-check/time-of-use gap by binding
    # one exact operation to a revocation-epoch snapshot and a short lease.  A
    # lease freezes validity; it neither widens scope nor upgrades authority.
    for execution in packet.get("authority_capability_execution_audits", []):
        eid = execution["id"]
        certificate = stack_certificates.get(execution.get("certificate_id"))
        if certificate is None:
            err("unknown_executed_authority_certificate", eid, str(execution.get("certificate_id")))
            continue
        validation_time = execution.get("validation_time")
        execution_time = execution.get("execution_time")
        lease_expires = execution.get("lease_expires")
        if not all(isinstance(value, int) for value in (validation_time, execution_time, lease_expires)) or not (
            validation_time <= execution_time <= lease_expires
        ):
            err("authority_capability_execution_outside_lease", eid, f"{validation_time}<={execution_time}<={lease_expires}")
        if not execution.get("atomic_revocation_check"):
            err("non_atomic_authority_capability_execution", eid, "revocation epoch not checked atomically")
        snapshot = execution.get("root_revocation_epoch_snapshot", {})
        current = execution.get("execution_revocation_epochs", {})
        if not snapshot or snapshot != current:
            err("stale_authority_capability_snapshot", eid, f"{snapshot}!={current}")
        for root_id in snapshot:
            root = root_certifications.get(root_id)
            if root is None or (isinstance(execution_time, int) and (
                execution_time < root.get("valid_from", execution_time)
                or (root.get("revoked_at") is not None and execution_time >= root["revoked_at"])
            )):
                err("capability_execution_uses_inactive_root", eid, root_id)
        operation = execution.get("operation")
        target = execution.get("target_scope")
        if operation not in certificate.get("allowed_operations", []) or target != certificate.get("target_scope"):
            err("authority_capability_scope_amplification", eid, f"{operation}@{target}")
        if execution.get("authority_kind_before") != "challenge_standing" or execution.get("authority_kind_after") != "challenge_standing":
            err("capability_lease_authority_laundering", eid, f"{execution.get('authority_kind_before')}->{execution.get('authority_kind_after')}")
        if not execution.get("single_use") or not execution.get("nonce") or not execution.get("nonce_consumed"):
            err("replayable_authority_capability_nonce", eid, str(execution.get("nonce")))
        if execution.get("second_use_permitted") is not False:
            err("authority_capability_reuse_permitted", eid, str(execution.get("second_use_permitted")))

    # Distributed-consumption no-go.  With identical local views, no message
    # before execution, and the same deterministic rule, the two decisions are
    # equal.  Hence neither (0,0) nor (1,1) realizes exactly one success.
    repair_kinds = {"shared_linearization", "site_partition", "bounded_multiplicity"}
    for audit in packet.get("distributed_capability_consumption_audits", []):
        did = audit["id"]
        certificate = stack_certificates.get(audit.get("certificate_id"))
        sites = audit.get("sites", [])
        outcomes = audit.get("symmetric_deterministic_outcomes", [])
        if certificate is None or len(sites) != 2:
            err("untyped_distributed_capability_audit", did, str(sites))
            continue
        symmetric_partition = bool(
            audit.get("identical_initial_local_views")
            and audit.get("same_deterministic_local_rule")
            and not audit.get("communication_before_execution")
        )
        exact_outcomes = sorted(outcomes) == [[0, 0], [1, 1]]
        if not symmetric_partition or not exact_outcomes or any(sum(outcome) == 1 for outcome in outcomes):
            err("invalid_distributed_indistinguishability_witness", did, str(outcomes))
        if audit.get("local_protocol_guarantees_exactly_one"):
            err("false_distributed_single_use_guarantee", did, "symmetric sites cannot choose different outcomes")
        if audit.get("delayed_coherence_messages_restore_safety"):
            err("post_execution_coherence_cannot_restore_linearity", did, "messages arrive after both local commits")
        if audit.get("local_nonce_logs_are_global"):
            err("local_nonce_state_misclassified_as_global_linearity", did, "duplicated nonce logs do not linearize")

        repairs = {item.get("kind"): item for item in audit.get("repairs", [])}
        if set(repairs) != repair_kinds:
            err("incomplete_distributed_consumption_trichotomy", did, str(sorted(repairs)))
            continue
        linear = repairs["shared_linearization"]
        if not linear.get("source_authorized") or not linear.get("atomic_compare_and_set") or linear.get("state_cardinality") != 2:
            err("missing_shared_linearization_authority", did, str(linear))
        if linear.get("capability_kind_before") != linear.get("capability_kind_after"):
            err("distributed_linearizer_authority_laundering", did, f"{linear.get('capability_kind_before')}->{linear.get('capability_kind_after')}")
        if sorted(linear.get("global_outcome", [])) != [0, 1] or not linear.get("preserves_single_use"):
            err("linearizer_fails_global_single_use", did, str(linear.get("global_outcome")))
        partition = repairs["site_partition"]
        if not partition.get("partitioned_before_distribution") or partition.get("site_token_count") != 1:
            err("late_or_non_linear_site_partition", did, str(partition))
        if partition.get("semantic_change") != "eligible_locus_restricted":
            err("site_partition_semantics_untyped", did, str(partition.get("semantic_change")))
        multiplicity = repairs["bounded_multiplicity"]
        if multiplicity.get("resource_kind_after") != "bounded_multiplicity" or multiplicity.get("bound") != 2:
            err("untyped_bounded_multiplicity_repair", did, str(multiplicity))
        if multiplicity.get("still_claims_single_use"):
            err("bounded_multiplicity_mislabeled_single_use", did, str(multiplicity.get("bound")))

    # Safety/availability/partition trilemma for a globally linear capability.
    # The three maximal designs each satisfy exactly two properties.  Under a
    # partition, a safe linearizer must fail closed outside the authorized
    # quorum and use a monotone fencing epoch against stale winners.
    for audit in packet.get("distributed_linearity_trilemma_audits", []):
        tid = audit["id"]
        designs = audit.get("maximal_designs", [])
        signatures = {
            (item.get("single_use_safety"), item.get("availability_at_both_sites"), item.get("partition_tolerance"))
            for item in designs
        }
        expected = {(True, True, False), (True, False, True), (False, True, True)}
        if signatures != expected:
            err("invalid_distributed_linearity_trilemma", tid, str(sorted(signatures)))
        if audit.get("claims_all_three"):
            err("impossible_distributed_linearity_trinity", tid, "single-use safety, bilateral availability, partition tolerance")
        partition_run = audit.get("safe_partition_run", {})
        if partition_run.get("quorum_site") not in audit.get("sites", []) or partition_run.get("minority_site") not in audit.get("sites", []):
            err("untyped_partition_authority_loci", tid, str(partition_run))
        if partition_run.get("quorum_outcome") != 1 or partition_run.get("minority_outcome") != 0:
            err("safe_linearizer_serves_both_partition_sides", tid, str(partition_run))
        if not partition_run.get("minority_fails_closed") or partition_run.get("minority_local_fallback"):
            err("minority_locus_launders_local_authority", tid, str(partition_run))
        old_epoch = partition_run.get("old_fencing_epoch")
        new_epoch = partition_run.get("new_fencing_epoch")
        if not isinstance(old_epoch, int) or not isinstance(new_epoch, int) or new_epoch <= old_epoch:
            err("nonmonotone_distributed_fencing_epoch", tid, f"{old_epoch}->{new_epoch}")
        if partition_run.get("stale_epoch_execution_permitted"):
            err("stale_partition_grant_executes", tid, str(old_epoch))
        if audit.get("eventual_recovery_counted_as_partition_availability"):
            err("eventual_recovery_laundered_as_immediate_availability", tid, "availability must hold during partition")

    # Explicit finite constructor for the linearizer.  Pairwise quorum
    # intersection locates a shared replica; durable non-equivocation at that
    # replica prevents two conflicting certificates in one fencing epoch.
    for network in packet.get("linearization_constructor_networks", []):
        nid = network["id"]
        replicas = {item["id"]: item for item in network.get("replicas", [])}
        quorums = [set(items) for items in network.get("authorized_quorums", [])]
        if len(replicas) < 3 or not quorums or any(not quorum.issubset(replicas) for quorum in quorums):
            err("untyped_linearization_constructor_network", nid, str(quorums))
            continue
        intersections = [quorums[i] & quorums[j] for i in range(len(quorums)) for j in range(i + 1, len(quorums))]
        if not intersections or any(not overlap for overlap in intersections):
            err("linearization_quorum_intersection_failure", nid, str([sorted(item) for item in intersections]))
        for replica_id, replica in replicas.items():
            if not replica.get("source_authorized_vote_role"):
                err("unauthorized_linearization_replica", replica_id, "vote role lacks source grant")
            if not replica.get("durable_append_only_vote_cell") or not replica.get("survives_restart") or not replica.get("monotone_epoch"):
                err("missing_durable_replica_non_equivocation", replica_id, str(replica))
            if replica.get("signatures_alone_prevent_equivocation"):
                err("signature_authentication_misclassified_as_non_equivocation", replica_id, "a signer can sign conflicting values")
        proof = network.get("conflict_exclusion_proof", {})
        first_quorum, second_quorum = set(proof.get("first_quorum", [])), set(proof.get("second_quorum", []))
        overlap = first_quorum & second_quorum
        if not overlap or set(proof.get("intersection_witness", [])) != overlap:
            err("invalid_quorum_intersection_witness", nid, str(sorted(overlap)))
        witness_replicas = [replicas.get(replica_id) for replica_id in overlap]
        durable_witness = bool(witness_replicas and all(
            replica and replica.get("durable_append_only_vote_cell") and replica.get("monotone_epoch")
            for replica in witness_replicas
        ))
        if proof.get("same_epoch") and proof.get("conflicting_values") and durable_witness:
            expected_constructible = False
        else:
            expected_constructible = True
        if proof.get("second_certificate_constructible") != expected_constructible:
            err("incorrect_linearization_conflict_exclusion", nid, str(proof.get("second_certificate_constructible")))
        boundary = network.get("implementation_boundary", {})
        if boundary.get("durable_cell_status") != "explicit_constructor_assumption" or not boundary.get("requires_storage_authority"):
            err("hidden_physical_linearization_oracle", nid, str(boundary))
        if boundary.get("claims_derived_from_quorum_math"):
            err("durability_falsely_derived_from_intersection", nid, "quorum mathematics does not build storage")
        if network.get("claims_unconditional_liveness"):
            err("unbounded_linearization_liveness_claim", nid, "safety proof does not imply progress")

    # Fault-parametric quorum theorem.  Two size-q quorums among n replicas
    # intersect in at least max(0, 2q-n) replicas.  Crash faults preserve
    # non-equivocation and require a nonempty overlap.  Byzantine faults may
    # occupy f overlap seats and therefore require minimum_intersection > f.
    for audit in packet.get("fault_parametric_quorum_audits", []):
        fid = audit["id"]
        n, q, f = audit.get("replica_count"), audit.get("quorum_size"), audit.get("fault_bound")
        if not all(isinstance(value, int) for value in (n, q, f)) or n <= 0 or q <= 0 or f < 0 or q > n:
            err("invalid_fault_parametric_quorum", fid, f"n={n},q={q},f={f}")
            continue
        minimum_intersection = max(0, 2 * q - n)
        if audit.get("minimum_intersection") != minimum_intersection:
            err("incorrect_minimum_quorum_intersection", fid, f"{audit.get('minimum_intersection')}!={minimum_intersection}")
        fault_kind = audit.get("fault_kind")
        if fault_kind == "crash_recovery":
            required_condition = "minimum_intersection>=1"
            expected_safe = minimum_intersection > 0 and not audit.get("faulty_replicas_may_equivocate")
        elif fault_kind == "byzantine":
            required_condition = "minimum_intersection>fault_bound"
            expected_safe = minimum_intersection > f and audit.get("faulty_replicas_may_equivocate")
        else:
            err("unknown_linearizer_fault_model", fid, str(fault_kind))
            continue
        if audit.get("safety_condition") != required_condition:
            err("fault_model_safety_condition_mismatch", fid, f"{audit.get('safety_condition')}!={required_condition}")
        if not audit.get("honest_replicas_non_equivocate") or not audit.get("source_authorized_fault_model"):
            err("unauthorized_or_unenforced_fault_model", fid, str(audit.get("source_authorized_fault_model")))
        if audit.get("claimed_safe") != expected_safe:
            err("incorrect_fault_parametric_safety_classification", fid, f"claimed={audit.get('claimed_safe')}, expected={expected_safe}")
        if fault_kind == "byzantine" and not expected_safe:
            witness = audit.get("conflict_witness", {})
            intersection = set(witness.get("first_quorum", [])) & set(witness.get("second_quorum", []))
            faulty = set(witness.get("faulty_replicas", []))
            if not intersection or not intersection.issubset(faulty) or len(faulty) > f or not witness.get("both_certificates_constructible"):
                err("missing_byzantine_quorum_conflict_witness", fid, str(witness))
        if audit.get("claims_fault_model_transport_without_reproof"):
            err("fault_model_authority_transport", fid, "crash proof cannot be transported to Byzantine faults")

    # Correlated-fault hypergraph theorem.  Scalar replica counts are a special
    # case.  Safety requires every pair of winning quorums to retain an honest
    # witness outside every admissible common-cause fault set.
    hypergraph_audits = {item["id"]: item for item in packet.get("fault_hypergraph_quorum_audits", [])}
    for audit in hypergraph_audits.values():
        hid = audit["id"]
        replicas = set(audit.get("replicas", []))
        quorums = [set(quorum) for quorum in audit.get("authorized_quorums", [])]
        fault_sets = [set(fault_set) for fault_set in audit.get("admissible_fault_sets", [])]
        root_map = audit.get("replica_authority_roots", {})
        if not replicas or set(root_map) != replicas or not quorums or not fault_sets:
            err("untyped_fault_hypergraph_audit", hid, str(sorted(replicas)))
            continue
        if any(not quorum.issubset(replicas) for quorum in quorums) or any(not fault_set.issubset(replicas) for fault_set in fault_sets):
            err("fault_hypergraph_unknown_replica", hid, "quorum or fault-set endpoint outside replica set")
        root_fibers: dict[str, set[str]] = {}
        for replica, root in root_map.items():
            root_fibers.setdefault(root, set()).add(replica)
        missing_fibers = [fiber for fiber in root_fibers.values() if fiber not in fault_sets]
        if missing_fibers:
            err("common_cause_fault_set_omitted", hid, str([sorted(fiber) for fiber in missing_fibers]))
        violations = []
        for left_index in range(len(quorums)):
            for right_index in range(left_index, len(quorums)):
                overlap = quorums[left_index] & quorums[right_index]
                for fault_set in fault_sets:
                    if not overlap - fault_set:
                        violations.append((left_index, right_index, sorted(fault_set)))
        expected_safe = not violations
        if audit.get("claimed_safe") != expected_safe:
            err("incorrect_fault_hypergraph_safety_classification", hid, str(violations[:3]))
        if violations:
            witness = audit.get("violation_witness", {})
            left = set(witness.get("first_quorum", []))
            right = set(witness.get("second_quorum", []))
            fault = set(witness.get("fault_set", []))
            if left not in quorums or right not in quorums or fault not in fault_sets or (left & right) - fault:
                err("missing_fault_hypergraph_violation_witness", hid, str(witness))
        if not audit.get("source_authorized_common_cause_model") or not audit.get("bounded_model_scope"):
            err("unauthorized_or_unbounded_common_cause_model", hid, str(audit.get("bounded_model_scope")))
        if audit.get("infers_independence_from_distinct_replica_ids"):
            err("replica_identity_laundered_as_failure_independence", hid, "distinct IDs do not imply distinct authority roots")

    # Open-world common-cause discovery.  A source-derived intervention row
    # generates a fault hyperedge from its nonzero replica support.  Enlarging
    # the fault family is safety-nonmonotone and suspends any certificate whose
    # quorum overlap is swallowed by the new edge.
    for discovery in packet.get("common_cause_discovery_audits", []):
        did = discovery["id"]
        baseline = hypergraph_audits.get(discovery.get("baseline_fault_audit"))
        repair = hypergraph_audits.get(discovery.get("repair_fault_audit"))
        replicas = discovery.get("replicas", [])
        matrix = discovery.get("intervention_response_matrix", [])
        probes = discovery.get("intervention_probes", [])
        if baseline is None or repair is None or len(matrix) != len(probes) or any(len(row) != len(replicas) for row in matrix):
            err("invalid_common_cause_discovery_matrix", did, f"{len(matrix)}x{len(matrix[0]) if matrix else 0}")
            continue
        new_probe = discovery.get("new_probe")
        if new_probe not in probes:
            err("unknown_common_cause_discovery_probe", did, str(new_probe))
            continue
        row = matrix[probes.index(new_probe)]
        support = [replica for replica, response in zip(replicas, row) if response]
        declared = discovery.get("derived_fault_set", [])
        if support != declared:
            err("common_cause_response_support_mismatch", did, f"{support}!={declared}")
        if not discovery.get("new_probe_source_derived") or not discovery.get("probe_committed_before_response"):
            err("target_fitted_common_cause_probe", did, str(new_probe))
        baseline_faults = [set(item) for item in baseline.get("admissible_fault_sets", [])]
        new_fault = set(declared)
        if new_fault in baseline_faults or new_fault not in [set(item) for item in discovery.get("extended_fault_sets", [])]:
            err("discovered_common_cause_not_admitted", did, str(declared))
        swallowed = any(
            not (set(left) & set(right)) - new_fault
            for left in baseline.get("authorized_quorums", [])
            for right in baseline.get("authorized_quorums", [])
        )
        if swallowed and discovery.get("old_safety_authority_retained"):
            err("safety_authority_retained_after_common_cause_discovery", did, str(declared))
        if discovery.get("status") != "challenge_open" or not swallowed:
            err("common_cause_discovery_fails_to_open_challenge", did, str(swallowed))
        repair_faults = [set(item) for item in repair.get("admissible_fault_sets", [])]
        if new_fault not in repair_faults:
            err("repair_drops_discovered_common_cause", did, str(declared))
        if not repair.get("claimed_safe") or discovery.get("repair_status") != "revalidated":
            err("common_cause_repair_not_revalidated", did, str(discovery.get("repair_status")))
        if discovery.get("claims_universal_independence") or not discovery.get("bounded_tested_constructor_grammar"):
            err("closed_world_common_cause_claim", did, str(discovery.get("bounded_tested_constructor_grammar")))

    # Probe coverage is authority-bearing and relative to enumerated source
    # constructors. Refinement preserves discoveries but expires negative
    # certificates until the enlarged grammar is replayed.
    discoveries = {item["id"]: item for item in packet.get("common_cause_discovery_audits", [])}
    for grammar in packet.get("probe_grammar_authority_audits", []):
        gid = grammar["id"]
        discovery = discoveries.get(grammar.get("discovery_audit"))
        classes = grammar.get("constructor_classes", [])
        authorized = grammar.get("authorized_probes", {})
        if discovery is None or not grammar.get("authority_root"):
            err("probe_grammar_lacks_source_authority", gid, str(grammar.get("authority_root")))
            continue
        if set(authorized) != set(classes) or any(not authorized.get(kind) for kind in classes):
            err("probe_grammar_constructor_coverage_gap", gid, str(authorized))
        declared_probes = set(discovery.get("intervention_probes", []))
        covered_probes = {probe for probes in authorized.values() for probe in probes}
        if covered_probes != declared_probes:
            err("probe_grammar_probe_coverage_mismatch", gid, str(sorted(covered_probes ^ declared_probes)))
        if grammar.get("coverage_kind") != "relative_exhaustion" or grammar.get("claims_constructor_universality"):
            err("probe_grammar_launders_relative_coverage", gid, str(grammar.get("coverage_kind")))
        refined = bool(grammar.get("new_constructor_classes"))
        if refined and (not grammar.get("predecessor_negative_certificate_expired") or not grammar.get("replay_required_after_refinement")):
            err("probe_grammar_refinement_retains_stale_negative_authority", gid, str(grammar.get("new_constructor_classes")))
        learned = {tuple(item) for item in discovery.get("extended_fault_sets", [])}
        preserved = {tuple(item) for item in grammar.get("discovered_faults_preserved_under_refinement", [])}
        if not preserved or not preserved <= learned:
            err("probe_grammar_refinement_drops_positive_discovery", gid, str(sorted(preserved)))
        if refined and grammar.get("replay_status") != "passed":
            err("probe_grammar_refinement_not_replayed", gid, str(grammar.get("replay_status")))

    # An authority root certifies an accountable manifest boundary, not its own
    # universal completeness. The complement is represented by a live frontier
    # and a typed refinement port, avoiding both regress and self-certification.
    grammars = {item["id"]: item for item in packet.get("probe_grammar_authority_audits", [])}
    for boundary in packet.get("probe_grammar_boundary_audits", []):
        bid = boundary["id"]
        grammar = grammars.get(boundary.get("probe_grammar_audit"))
        if grammar is None or not boundary.get("accountable_declarer") or not boundary.get("signed_manifest"):
            err("probe_grammar_boundary_unaccountable", bid, str(boundary.get("accountable_declarer")))
            continue
        if set(boundary.get("manifest_constructor_classes", [])) != set(grammar.get("constructor_classes", [])):
            err("probe_grammar_manifest_mismatch", bid, str(boundary.get("manifest_constructor_classes")))
        if boundary.get("self_certifying_root") or boundary.get("totality_authority"):
            err("probe_grammar_root_self_certifies_totality", bid, str(boundary.get("totality_authority")))
        if boundary.get("negative_claim_scope") != "manifest_constructor_classes only":
            err("probe_grammar_negative_scope_exceeds_manifest", bid, str(boundary.get("negative_claim_scope")))
        if not boundary.get("open_frontier") or boundary.get("frontier_emptiness_claimed"):
            err("probe_grammar_erases_open_frontier", bid, str(boundary.get("open_frontier")))
        if not boundary.get("challenge_port") or not boundary.get("challenge_port_live"):
            err("probe_grammar_boundary_has_no_refinement_port", bid, str(boundary.get("challenge_port")))

    # Relative negative authority is epoch-indexed. Manifest mutation fences
    # both the negative certificate and capabilities derived from it; positive
    # discoveries remain valid evidence in the successor epoch.
    boundaries = {item["id"]: item for item in packet.get("probe_grammar_boundary_audits", [])}
    for epoch_audit in packet.get("probe_grammar_epoch_audits", []):
        eid = epoch_audit["id"]
        if epoch_audit.get("boundary_audit") not in boundaries or len(epoch_audit.get("manifest_sha256", "")) != 64:
            err("manifest_epoch_binding_untyped", eid, str(epoch_audit.get("boundary_audit")))
            continue
        audit_epoch = epoch_audit.get("audit_epoch")
        capability_epoch = epoch_audit.get("capability_epoch")
        execution_epoch = epoch_audit.get("execution_epoch")
        expiry = epoch_audit.get("lease_expires_epoch")
        if not all(isinstance(value, int) for value in (audit_epoch, capability_epoch, execution_epoch, expiry)) or not (
            audit_epoch == capability_epoch == execution_epoch <= expiry
        ):
            err("stale_probe_grammar_capability_epoch", eid, f"{audit_epoch},{capability_epoch},{execution_epoch},{expiry}")
        if not epoch_audit.get("atomic_manifest_epoch_check"):
            err("non_atomic_manifest_epoch_check", eid, "manifest may drift between validation and execution")
        drift = epoch_audit.get("drift_scenario", {})
        if not isinstance(drift.get("new_manifest_epoch"), int) or drift.get("new_manifest_epoch", -1) <= audit_epoch:
            err("nonmonotone_manifest_epoch", eid, str(drift.get("new_manifest_epoch")))
        if drift.get("old_negative_certificate_live") or drift.get("old_capability_execution_permitted"):
            err("manifest_drift_preserves_stale_authority", eid, str(drift))
        if not drift.get("grammar_replay_required"):
            err("manifest_drift_skips_probe_replay", eid, str(drift.get("new_constructor_class")))
        if ["r1", "r2"] not in drift.get("positive_discoveries_retained", []):
            err("manifest_drift_drops_positive_discovery", eid, str(drift.get("positive_discoveries_retained")))

    # Local atomicity does not make a distributed manifest view unique. The
    # globally linearized value is the pair (epoch, digest), certified by an
    # authorized intersecting quorum with durable non-equivocation.
    epoch_audits = {item["id"]: item for item in packet.get("probe_grammar_epoch_audits", [])}
    networks = {item["id"]: item for item in packet.get("linearization_constructor_networks", [])}
    for audit in packet.get("distributed_manifest_epoch_audits", []):
        aid = audit["id"]
        views = audit.get("local_views", [])
        if audit.get("probe_grammar_epoch_audit") not in epoch_audits or len(views) != 2:
            err("distributed_manifest_audit_untyped", aid, str(len(views)))
            continue
        same_epoch = views[0].get("epoch") == views[1].get("epoch")
        different_digest = views[0].get("manifest_sha256") != views[1].get("manifest_sha256")
        if same_epoch and different_digest and (audit.get("identical_epoch_numbers_imply_identical_manifest") or audit.get("local_checks_imply_global_consistency")):
            err("local_manifest_atomicity_laundered_as_global_consistency", aid, str(views))
        if not (same_epoch and different_digest and audit.get("fork_is_constructible_before_communication")):
            err("distributed_manifest_fork_witness_missing", aid, str(views))
        repair = audit.get("repair", {})
        network = networks.get(repair.get("linearization_network"))
        if network is None or not repair.get("source_authorized_configuration_role"):
            err("manifest_linearizer_lacks_configuration_authority", aid, str(repair.get("linearization_network")))
            continue
        if set(repair.get("certificate_value_fields", [])) != {"epoch", "manifest_sha256"}:
            err("manifest_certificate_does_not_bind_digest", aid, str(repair.get("certificate_value_fields")))
        first, second = set(repair.get("certificate_quorum", [])), set(repair.get("conflicting_certificate_quorum", []))
        overlap = first & second
        if first not in [set(q) for q in network.get("authorized_quorums", [])] or second not in [set(q) for q in network.get("authorized_quorums", [])] or set(repair.get("intersection_witness", [])) != overlap:
            err("manifest_certificate_quorums_not_coherent", aid, str(sorted(overlap)))
        if not repair.get("durable_non_equivocation") or repair.get("conflicting_same_epoch_digest_certificate_constructible"):
            err("manifest_digest_fork_survives_linearization", aid, str(repair.get("conflicting_same_epoch_digest_certificate_constructible")))

    # Reconfiguration crosses authority loci. Neither side may authorize the
    # transition alone: the successor is activated by a value bound to both
    # configurations and jointly endorsed across the boundary.
    for audit in packet.get("configuration_reconfiguration_audits", []):
        aid = audit["id"]
        old, new = audit.get("old_configuration", {}), audit.get("new_configuration", {})
        required = {"old_epoch", "old_digest", "new_epoch", "new_digest", "new_members"}
        if not isinstance(old.get("epoch"), int) or not isinstance(new.get("epoch"), int) or new.get("epoch", -1) <= old.get("epoch", -1):
            err("nonmonotone_configuration_transition", aid, f"{old.get('epoch')}->{new.get('epoch')}")
        if set(audit.get("transition_value_fields", [])) != required:
            err("reconfiguration_certificate_underbinds_transition", aid, str(audit.get("transition_value_fields")))
        old_endorsement, new_endorsement = set(audit.get("old_quorum_endorsement", [])), set(audit.get("new_quorum_endorsement", []))
        if old_endorsement != set(old.get("quorum", [])) or new_endorsement != set(new.get("quorum", [])) or not audit.get("joint_consensus_required"):
            err("reconfiguration_lacks_joint_consensus", aid, str([sorted(old_endorsement), sorted(new_endorsement)]))
        bridge = old_endorsement & new_endorsement
        if set(audit.get("bridge_witness", [])) != bridge or not bridge or not audit.get("bridge_durable_non_equivocation"):
            err("reconfiguration_bridge_not_non_equivocating", aid, str(sorted(bridge)))
        fault_kind, fault_bound = audit.get("fault_kind"), audit.get("fault_bound")
        safe = len(bridge) >= 1 if fault_kind == "crash_recovery" and not audit.get("bridge_members_may_equivocate") else (
            len(bridge) > fault_bound if fault_kind == "byzantine" and isinstance(fault_bound, int) else False
        )
        if audit.get("claimed_safe") != safe:
            err("incorrect_reconfiguration_fault_threshold", aid, f"bridge={len(bridge)},f={fault_bound},kind={fault_kind}")
        fault_sets = [set(item) for item in audit.get("admissible_bridge_fault_sets", [])]
        root_map = audit.get("bridge_authority_roots", {})
        if set(root_map) != bridge or not audit.get("source_authorized_bridge_fault_model"):
            err("unauthorized_reconfiguration_fault_hypergraph", aid, str(root_map))
        root_fibers = [{r for r, root in root_map.items() if root == authority_root} for authority_root in set(root_map.values())]
        if fault_kind == "byzantine" and any(fiber not in fault_sets for fiber in root_fibers):
            err("reconfiguration_common_cause_omitted", aid, str([sorted(f) for f in root_fibers]))
        hypergraph_safe = all(bool(bridge - fault) for fault in fault_sets)
        if audit.get("claimed_safe") != hypergraph_safe:
            err("incorrect_reconfiguration_hypergraph_safety", aid, str([sorted(f) for f in fault_sets]))
        if audit.get("old_only_may_activate_successor") or audit.get("new_only_may_self_activate") or audit.get("claims_authority_by_membership_transport"):
            err("reconfiguration_authority_laundering", aid, "one configuration cannot unilaterally cross the authority boundary")
        if audit.get("conflicting_transition_constructible"):
            err("reconfiguration_split_brain_survives", aid, "conflicting successor transition remains constructible")

    return errors


def compile_packet(packet: dict[str, Any]) -> dict[str, Any]:
    errors = validate(packet)
    return {
        "valid": not errors,
        "error_count": len(errors),
        "errors": [asdict(error) for error in errors],
        "evidence_domain_count": len(packet.get("evidence_domains", [])),
        "grant_count": len(packet.get("authority_grants", [])),
        "composition_count": len(packet.get("compositions", [])),
        "associativity_cell_count": len(packet.get("associativity_cells", [])),
        "application_case_count": len(packet.get("application_cases", [])),
        "representation_change_test_count": len(packet.get("representation_change_tests", [])),
        "probe_grammar_authority_audit_count": len(packet.get("probe_grammar_authority_audits", [])),
        "probe_grammar_boundary_audit_count": len(packet.get("probe_grammar_boundary_audits", [])),
        "probe_grammar_epoch_audit_count": len(packet.get("probe_grammar_epoch_audits", [])),
        "distributed_manifest_epoch_audit_count": len(packet.get("distributed_manifest_epoch_audits", [])),
        "configuration_reconfiguration_audit_count": len(packet.get("configuration_reconfiguration_audits", [])),
        "presentation_coherence_cell_count": len(packet.get("presentation_coherence_cells", [])),
        "presentation_atlas_count": len(packet.get("presentation_atlas_coherence", [])),
        "authority_descent_object_count": len(packet.get("authority_descent_objects", [])),
        "presentation_refinement_count": len(packet.get("presentation_refinement_coherence", [])),
        "presentation_deletion_test_count": len(packet.get("presentation_deletion_tests", [])),
        "source_provenance_node_count": len(packet.get("source_provenance", {}).get("nodes", [])),
        "source_intervention_test_count": len(packet.get("source_intervention_tests", [])),
        "mechanism_identification_audit_count": len(packet.get("mechanism_identification_audits", [])),
        "rival_extension_audit_count": len(packet.get("rival_extension_audits", [])),
        "rival_admission_count": len(packet.get("rival_admissions", [])),
        "schema": "marici.authority-grant-composition-result.v1",
    }
