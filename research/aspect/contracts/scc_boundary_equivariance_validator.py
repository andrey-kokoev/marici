"""Non-live validator for finite boundary-automorphism equivariance certificates."""


def validate(certificate):
    if certificate.get("applicability") == "not_applicable":
        return {"valid": True, "status": "not_applicable", "errors": []}
    errors = []
    source_group = certificate.get("source_automorphism_group", {})
    target_group = certificate.get("target_automorphism_group", {})
    source_elements = source_group.get("elements", [])
    target_elements = target_group.get("elements", [])
    phi = certificate.get("group_isomorphism", {})
    source_points = certificate.get("source_matching_points", [])
    target_points = certificate.get("target_matching_points", [])
    source_action = certificate.get("source_matching_action", {})
    target_action = certificate.get("target_matching_action", {})
    alpha = certificate.get("matching_object_map", {})

    def valid_group(group, elements, label):
        table = group.get("multiplication", {})
        identity = group.get("identity")
        if identity not in elements or set(table) != set(elements) or any(set(table.get(g, {})) != set(elements) for g in elements):
            errors.append(f"{label}_group_table_invalid")
            return False
        if any(table[g][h] not in elements for g in elements for h in elements):
            errors.append(f"{label}_group_not_closed")
            return False
        if any(table[identity][g] != g or table[g][identity] != g for g in elements):
            errors.append(f"{label}_group_identity_failed")
        if any(table[table[g][h]][k] != table[g][table[h][k]] for g in elements for h in elements for k in elements):
            errors.append(f"{label}_group_associativity_failed")
        return True

    source_group_valid = valid_group(source_group, source_elements, "source")
    target_group_valid = valid_group(target_group, target_elements, "target")
    if set(phi) != set(source_elements) or set(phi.values()) != set(target_elements) or len(set(phi.values())) != len(phi):
        errors.append("automorphism_group_map_not_bijective")
    elif source_group_valid and target_group_valid:
        source_mult = source_group["multiplication"]
        target_mult = target_group["multiplication"]
        if any(phi[source_mult[g][h]] != target_mult[phi[g]][phi[h]] for g in source_elements for h in source_elements):
            errors.append("automorphism_group_map_not_homomorphism")

    def valid_action(action, elements, points, label):
        if set(action) != set(elements) or any(set(action.get(g, {})) != set(points) or set(action[g].values()) != set(points) for g in elements):
            errors.append(f"{label}_matching_action_not_permutation")
            return
        identity = source_group.get("identity") if label == "source" else target_group.get("identity")
        multiplication = source_group.get("multiplication", {}) if label == "source" else target_group.get("multiplication", {})
        if any(action[identity][point] != point for point in points):
            errors.append(f"{label}_matching_action_identity_failed")
        if any(action[multiplication[g][h]][point] != action[g][action[h][point]] for g in elements for h in elements for point in points):
            errors.append(f"{label}_matching_action_composition_failed")

    valid_action(source_action, source_elements, source_points, "source")
    valid_action(target_action, target_elements, target_points, "target")

    orbit_only = certificate.get("orbit_only", False)
    quotient_authority = certificate.get("source_derived_quotient_authority")
    if orbit_only:
        if not quotient_authority:
            errors.append("orbit_quotient_authority_missing")
        status = "authorized_orbit_quotient" if quotient_authority and not errors else "rejected"
        return {"valid": not errors, "status": status, "errors": sorted(set(errors))}

    if set(alpha) != set(source_points) or set(alpha.values()) != set(target_points) or len(set(alpha.values())) != len(alpha):
        errors.append("matching_object_map_not_bijective")
    elif not errors:
        if any(alpha[source_action[g][point]] != target_action[phi[g]][alpha[point]] for g in source_elements for point in source_points):
            errors.append("matching_object_equivariance_failed")
    return {"valid": not errors, "status": "reversible_equivariant" if not errors else "rejected", "errors": sorted(set(errors))}
