"""Non-live semantic validators for SCC probe certificate candidates."""

import hashlib
from itertools import combinations
from pathlib import Path

ALLOWED_INTERACTIONS = {"matching_defect", "additive_cross_effect", "continuation_projection", "factorized"}


def _faces(vertices):
    vertices = tuple(vertices)
    return {tuple(sorted(face)) for size in range(len(vertices) + 1) for face in combinations(vertices, size)}


def validate(entry, root):
    errors = []
    domain = entry.get("configuration_domain", {})
    vertices = domain.get("vertices", [])
    admitted = {tuple(sorted(face)) for face in domain.get("admitted_faces", [])}
    if admitted != _faces(vertices):
        errors.append("configuration_not_downward_closed")

    presheaf = entry.get("constraint_presheaf", {})
    objects = presheaf.get("objects", {})
    restrictions = presheaf.get("restrictions", [])
    arrow = {(item.get("source"), item.get("target")): item for item in restrictions}
    for face in admitted:
        name = ",".join(face)
        if name not in objects:
            errors.append("constraint_object_missing")
            break
        if (name, name) not in arrow or arrow[(name, name)].get("map") != "identity":
            errors.append("restriction_identity_missing")
            break
    if not presheaf.get("composition_verified", False):
        errors.append("restriction_composition_unverified")

    matching = entry.get("matching_map_certificate", {})
    if not all(matching.get(key) for key in ("domain", "codomain", "map")) or not matching.get("typed", False):
        errors.append("matching_map_untyped")

    continuation = entry.get("continuation_interface_certificate", {})
    if continuation.get("record_projection_faithful") is False and not continuation.get("unresolved_multiplicity"):
        errors.append("nonfaithful_projection_without_multiplicity")
    if "record_projection_faithful" not in continuation:
        errors.append("faithfulness_status_missing")

    rewrite = entry.get("rewrite_naturality_certificate", {})
    squares = rewrite.get("squares", [])
    if rewrite.get("scope") != "local" or not squares or not all(square.get("commutes") is True for square in squares):
        errors.append("rewrite_naturality_unverified")

    interaction = entry.get("interaction_classification", {})
    if interaction.get("kind") not in ALLOWED_INTERACTIONS:
        errors.append("interaction_kind_invalid")

    additive = entry.get("optional_additive_specialization", {})
    if additive.get("applicable") and (not additive.get("target_authority") or "residual" not in additive):
        errors.append("additive_specialization_untyped")

    source = entry.get("source_digest", {})
    try:
        path = Path(root) / source["path"]
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != source.get("sha256"):
            errors.append("source_digest_mismatch")
    except (KeyError, OSError):
        errors.append("source_digest_unreadable")

    boundary = entry.get("authority_and_boundary", {})
    if not boundary.get("nonclaims"):
        errors.append("authority_boundary_missing")
    return {"valid": not errors, "errors": sorted(set(errors))}
