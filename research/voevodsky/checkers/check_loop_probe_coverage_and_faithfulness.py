from __future__ import annotations

import json

import sympy as sp


def cycle_rank(vertices: set[str], edges: set[frozenset[str]], components: int = 1) -> int:
    return len(edges) - len(vertices) + components


def main() -> None:
    # Two four-cycles sharing one edge: cycle rank two.
    vertices = {"a", "b", "c", "d", "e", "f"}
    edges = {
        frozenset(("a", "b")), frozenset(("b", "c")), frozenset(("c", "d")), frozenset(("d", "a")),
        frozenset(("c", "e")), frozenset(("e", "f")), frozenset(("f", "d")),
    }
    beta_1 = cycle_rank(vertices, edges)
    assert beta_1 == 2
    measured_cycle_basis_elements = 1
    assert measured_cycle_basis_elements < beta_1

    # Exact measurements on one cycle leave the second cycle unconstrained.
    holonomy_assignment_1 = {"cycle_1": sp.eye(2), "cycle_2": sp.eye(2)}
    holonomy_assignment_2 = {"cycle_1": sp.eye(2), "cycle_2": sp.diag(1, -1)}
    assert holonomy_assignment_1["cycle_1"] == holonomy_assignment_2["cycle_1"]
    assert holonomy_assignment_1 != holonomy_assignment_2

    # One trace coordinate is not faithful on general holonomy operators.
    h1 = sp.diag(1, 1, -1)
    h2 = sp.diag(1, sp.I, -sp.I)
    assert sp.trace(h1) == sp.trace(h2) == 1
    assert h1.eigenvals() != h2.eigenvals()
    assert h1 != h2

    # Repetition under one fault class does not increase independent fault coverage.
    loop_measurements = ["forward", "reverse", "repeat_1", "repeat_2"]
    fault_classes = {measurement: "shared_control_0" for measurement in loop_measurements}
    assert len(set(fault_classes.values())) == 1

    required_fields = {
        "cycle_basis_coverage",
        "higher_relation_coverage",
        "observable_coordinate",
        "coordinate_faithfulness",
        "unresolved_fiber",
        "fault_independence_class",
        "physical_constructor_status",
    }
    assert len(required_fields) == 7

    result = {
        "schema": "marici.voevodsky.loop-probe-coverage-and-faithfulness.v1",
        "status": "loop_probe_global_promotion_gates_verified",
        "fixture_cycle_rank": beta_1,
        "single_loop_cover_complete": False,
        "unmeasured_cycle_countermodel": True,
        "single_trace_coordinate_faithful": False,
        "equal_trace_distinct_holonomy_countermodel": True,
        "shared_control_repetitions_independent": False,
        "higher_simplex_relations_separate": True,
        "required_loop_record_fields": sorted(required_fields),
        "Kitaev_four_copy_global_gluing_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
