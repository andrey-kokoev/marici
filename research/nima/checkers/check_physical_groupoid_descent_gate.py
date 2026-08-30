"""Finite exact tests for subgroup invariance, reference ports, and framing."""

import itertools
import json


def permutations(items):
    return list(itertools.permutations(items))


def permute_tuple(p, x):
    return tuple(x[p[i]] for i in range(len(p)))


def invariant(points, actions, observable):
    return all(observable(action(x)) == observable(x) for action in actions for x in points)


def chart_gate():
    points = list(itertools.product(range(3), repeat=3))
    group = permutations(range(3))
    full_actions = [lambda x, p=p: permute_tuple(p, x) for p in group]
    stabilizer = [p for p in group if p[0] == 0]
    chart_actions = [lambda x, p=p: permute_tuple(p, x) for p in stabilizer]
    coordinate_zero = lambda x: x[0]
    return {
        "chart_group_order": len(chart_actions),
        "physical_group_order": len(full_actions),
        "chart_invariant": invariant(points, chart_actions, coordinate_zero),
        "physical_invariant": invariant(points, full_actions, coordinate_zero),
    }


def reference_port_gate(modulus=5):
    points = list(itertools.product(range(modulus), repeat=2))
    diagonal = [
        lambda x, a=a: ((x[0] + a) % modulus, (x[1] + a) % modulus)
        for a in range(modulus)
    ]
    independent = [
        lambda x, a=a, b=b: ((x[0] + a) % modulus, (x[1] + b) % modulus)
        for a in range(modulus)
        for b in range(modulus)
    ]
    delta = lambda x: (x[1] - x[0]) % modulus
    diagonal_orbits = {
        frozenset(action(x) for action in diagonal) for x in points
    }
    delta_values = {frozenset(delta(x) for x in orbit) for orbit in diagonal_orbits}
    return {
        "diagonal_group_order": len(diagonal),
        "independent_group_order": len(independent),
        "relative_phase_diagonal_invariant": invariant(points, diagonal, delta),
        "relative_phase_independent_invariant": invariant(points, independent, delta),
        "diagonal_orbit_count": len(diagonal_orbits),
        "delta_separates_diagonal_orbits": len(delta_values) == len(diagonal_orbits)
        and all(len(values) == 1 for values in delta_values),
    }


def gl2_f2():
    matrices = []
    for a, b, c, d in itertools.product(range(2), repeat=4):
        if (a * d - b * c) % 2 == 1:
            matrices.append((a, b, c, d))

    def act(m, x):
        a, b, c, d = m
        return ((a * x[0] + b * x[1]) % 2, (c * x[0] + d * x[1]) % 2)

    points = list(itertools.product(range(2), repeat=2))
    first_loop = lambda x: x[0]
    weight_zero = lambda x: int(x == (0, 0))
    return {
        "mapping_class_image_order": len(matrices),
        "marked_first_loop_invariant": all(
            first_loop(act(m, x)) == first_loop(x) for m in matrices for x in points
        ),
        "zero_vs_nonzero_orbit_readout_invariant": all(
            weight_zero(act(m, x)) == weight_zero(x) for m in matrices for x in points
        ),
        "nonzero_logical_vectors_form_one_unframed_orbit": len(
            {act(m, (1, 0)) for m in matrices}
        )
        == 3,
    }


def main():
    chart = chart_gate()
    reference = reference_port_gate()
    toric = gl2_f2()
    assert chart["chart_invariant"] and not chart["physical_invariant"]
    assert reference["relative_phase_diagonal_invariant"]
    assert not reference["relative_phase_independent_invariant"]
    assert reference["delta_separates_diagonal_orbits"]
    assert not toric["marked_first_loop_invariant"]
    assert toric["zero_vs_nonzero_orbit_readout_invariant"]
    assert toric["nonzero_logical_vectors_form_one_unframed_orbit"]
    print(
        json.dumps(
            {
                "schema": "marici.physical-groupoid-descent-gate.v1",
                "chart_gate": chart,
                "reference_port_gate": reference,
                "toric_framing_gate": toric,
                "gates": {
                    "subgroup_invariance_is_not_physical_descent": True,
                    "reference_port_changes_the_admissible_group": True,
                    "marked_logical_coordinates_require_framing": True,
                },
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
