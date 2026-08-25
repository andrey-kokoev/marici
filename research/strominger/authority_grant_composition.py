"""Standalone partial composition calculus for source-authority grants."""

from __future__ import annotations

from dataclasses import asdict, dataclass
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


def validate(packet: dict[str, Any]) -> list[Error]:
    errors: list[Error] = []
    domains = {item["id"]: item for item in packet.get("evidence_domains", [])}
    transformations = {item["id"]: item for item in packet.get("transformations", [])}
    grants = {item["id"]: item for item in packet.get("authority_grants", [])}
    compositions = {item["id"]: item for item in packet.get("compositions", [])}
    presentation_cells = {item["id"]: item for item in packet.get("presentation_coherence_cells", [])}

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
        "presentation_coherence_cell_count": len(packet.get("presentation_coherence_cells", [])),
        "presentation_atlas_count": len(packet.get("presentation_atlas_coherence", [])),
        "authority_descent_object_count": len(packet.get("authority_descent_objects", [])),
        "presentation_refinement_count": len(packet.get("presentation_refinement_coherence", [])),
        "presentation_deletion_test_count": len(packet.get("presentation_deletion_tests", [])),
        "schema": "marici.authority-grant-composition-result.v1",
    }
