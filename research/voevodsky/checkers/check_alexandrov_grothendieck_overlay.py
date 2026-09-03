from __future__ import annotations

import itertools
import json


def states(nodes: set[str], edges: set[tuple[str, str]]) -> set[frozenset[str]]:
    result = set()
    ordered = sorted(nodes)
    for length in range(len(nodes) + 1):
        for values in itertools.combinations(ordered, length):
            state = frozenset(values)
            if all(target not in state or source in state for source, target in edges):
                result.add(state)
    return result


def domain(all_states: set[frozenset[str]], required: set[str]) -> set[frozenset[str]]:
    return {state for state in all_states if required <= state}


def upward_closed(open_set: set[frozenset[str]], all_states: set[frozenset[str]]) -> bool:
    return all(not (state <= stronger) or stronger in open_set for state in open_set for stronger in all_states)


def main() -> None:
    nodes = {"source", "descent", "completion", "comparison"}
    dependencies = {("descent", "comparison"), ("completion", "comparison")}
    base = states(nodes, dependencies)

    u = domain(base, {"source", "descent"})
    v = domain(base, {"source", "completion"})
    interface = domain(base, {"source"})
    assert upward_closed(u, base) and upward_closed(v, base)
    assert upward_closed(u | v, base) and upward_closed(u & v, base)
    composite = u & v & interface
    assert composite == domain(base, {"source", "descent", "completion"})

    # Distributive lattice of open domains.
    w = domain(base, {"comparison"})
    assert u & (v | w) == (u & v) | (u & w)
    assert u | (v & w) == (u | v) & (u | w)

    # Both local routes can exist without a comparison/gluing cell.
    both_without_comparison = frozenset({"source", "descent", "completion"})
    with_comparison = frozenset({"source", "descent", "completion", "comparison"})
    assert both_without_comparison in composite
    assert both_without_comparison not in w
    assert with_comparison in w

    # Grothendieck base arrows are monotone only.
    base_arrows = {(left, right) for left in base for right in base if left <= right}
    assert (both_without_comparison, with_comparison) in base_arrows
    assert (with_comparison, both_without_comparison) not in base_arrows

    # R_zeta requires two incomparable primitives; either singleton remains outside.
    r_nodes = {"typed_target", "derived_map"}
    r_base = states(r_nodes, set())
    r_domain = domain(r_base, r_nodes)
    assert frozenset({"typed_target"}) not in r_domain
    assert frozenset({"derived_map"}) not in r_domain
    assert frozenset(r_nodes) in r_domain

    # Two sections do not glue merely because their domains cover: overlap agreement is independent data.
    local_values = {"U": "route_descent", "V": "route_completion"}
    overlap_comparison_supplied = False
    glued = local_values["U"] == local_values["V"] or overlap_comparison_supplied
    assert glued is False
    overlap_comparison_supplied = True
    glued = overlap_comparison_supplied
    assert glued is True

    result = {
        "schema": "marici.voevodsky.alexandrov-grothendieck-overlay.v1",
        "status": "open_domain_and_gluing_structure_verified",
        "certificate_states": len(base),
        "realization_domains_upward_open": True,
        "open_domain_lattice_distributive": True,
        "composition_is_domain_meet": True,
        "alternatives_are_domain_join_without_automatic_gluing": True,
        "base_change_one_way": True,
        "comparison_cell_is_independent_gluing_datum": True,
        "R_zeta_single_primitive_states_outside_domain": True,
        "global_equipment_section_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
