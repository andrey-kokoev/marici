"""Non-live validator for finite SCC boundary-index constructors."""

from itertools import product

KINDS = {"discrete_occurrences_with_external_action", "internal_groupoid_diagram", "authorized_orbit_quotient"}


def validate(certificate):
    errors = []
    kind = certificate.get("index_kind")
    if kind not in KINDS:
        return {"valid": False, "status": "rejected", "errors": ["boundary_index_kind_missing_or_invalid"]}
    if certificate.get("constructor_inferred_from_cardinality"):
        errors.append("constructor_identity_inferred_from_cardinality")

    if kind == "authorized_orbit_quotient":
        if not certificate.get("source_action_reference") or not certificate.get("orbit_projection"):
            errors.append("orbit_quotient_source_action_missing")
        if not certificate.get("source_derived_quotient_authority"):
            errors.append("orbit_quotient_authority_missing")
        return {"valid": not errors, "status": "authorized_orbit_quotient" if not errors else "rejected", "errors": sorted(set(errors))}

    objects = certificate.get("objects", [])
    values = certificate.get("object_values", {})
    if not objects or set(values) != set(objects) or any(not values[obj] for obj in objects):
        errors.append("boundary_index_objects_or_values_invalid")

    internal = certificate.get("internal_morphisms", [])
    if kind == "discrete_occurrences_with_external_action":
        if internal:
            errors.append("discrete_index_has_internal_morphisms")
        expected_size = 1
        for obj in objects:
            expected_size *= len(values[obj])
        if certificate.get("matching_cardinality") != expected_size:
            errors.append("discrete_matching_cardinality_wrong")
        return {"valid": not errors, "status": "discrete_external" if not errors else "rejected", "errors": sorted(set(errors))}

    maps = certificate.get("diagram_maps", {})
    morphism_names = {item.get("name") for item in internal}
    if None in morphism_names or set(maps) != morphism_names:
        errors.append("internal_groupoid_diagram_map_missing")
    else:
        for morphism in internal:
            name, source, target = morphism["name"], morphism.get("source"), morphism.get("target")
            mapping = maps[name]
            if source not in values or target not in values or set(mapping) != set(values[source]) or set(mapping.values()) != set(values[target]):
                errors.append("internal_groupoid_diagram_map_not_bijective")
                break

    if len(objects) == 2 and not errors:
        left, right = objects
        forward = next((item for item in internal if item.get("source") == left and item.get("target") == right), None)
        backward = next((item for item in internal if item.get("source") == right and item.get("target") == left), None)
        if not forward or not backward:
            errors.append("walking_groupoid_inverse_pair_missing")
        else:
            f, g = maps[forward["name"]], maps[backward["name"]]
            if any(g[f[x]] != x for x in values[left]) or any(f[g[y]] != y for y in values[right]):
                errors.append("walking_groupoid_inverse_law_failed")
            computed = sorted([[x, y] for x, y in product(values[left], values[right]) if y == f[x] and x == g[y]])
            reported = sorted(certificate.get("matching_limit", []))
            if reported != computed:
                errors.append("internal_matching_limit_not_compatibility_solution")
    elif len(objects) != 2:
        errors.append("validator_scope_requires_two_object_groupoid")
    return {"valid": not errors, "status": "internal_groupoid" if not errors else "rejected", "errors": sorted(set(errors))}
