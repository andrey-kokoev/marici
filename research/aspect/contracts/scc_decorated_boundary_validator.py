"""Non-live semantic validator for decorated SCC boundary transport certificates."""


def validate(certificate):
    if certificate.get("applicability") == "not_applicable":
        return {"valid": True, "status": "not_applicable", "errors": []}
    errors = []
    source = certificate.get("source_boundary_presentation", {})
    target = certificate.get("target_boundary_presentation", {})
    transport = certificate.get("transport", {})

    def occurrence_map(presentation, side):
        occurrences = presentation.get("occurrences", [])
        ids = [item.get("id") for item in occurrences]
        if presentation.get("occurrence_count") != len(occurrences) or None in ids or len(ids) != len(set(ids)):
            errors.append(f"{side}_occurrence_identity_invalid")
        if any(not item.get("carrier") or not item.get("incidence") for item in occurrences):
            errors.append(f"{side}_boundary_typing_invalid")
        return {item.get("id"): item for item in occurrences if item.get("id")}

    source_occurrences = occurrence_map(source, "source")
    target_occurrences = occurrence_map(target, "target")
    index = transport.get("index_equivalence", {})
    if set(index) != set(source_occurrences) or set(index.values()) != set(target_occurrences) or len(set(index.values())) != len(index):
        errors.append("boundary_index_not_equivalence")

    carrier = transport.get("carrier_natural_isomorphism", {})
    if set(carrier) != set(source_occurrences) or not all(item.get("isomorphism") is True for item in carrier.values()):
        errors.append("boundary_carrier_naturality_missing")
    else:
        for source_id, comparison in carrier.items():
            target_id = index.get(source_id)
            if comparison.get("source_carrier") != source_occurrences[source_id]["carrier"] or target_id not in target_occurrences or comparison.get("target_carrier") != target_occurrences[target_id]["carrier"]:
                errors.append("boundary_carrier_naturality_ill_typed")
                break

    if transport.get("apex_isomorphism") is not True:
        errors.append("boundary_apex_isomorphism_missing")
    coherence = transport.get("incidence_coherence", {})
    if set(coherence) != set(source_occurrences) or not all(value is True for value in coherence.values()):
        errors.append("boundary_incidence_coherence_failed")
    return {"valid": not errors, "status": "validated" if not errors else "rejected", "errors": sorted(set(errors))}
