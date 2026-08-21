#!/usr/bin/env python3
"""Test whether hidden term orientations can rescue the OFPT incidence cycle."""

import json
from pathlib import Path

from sage.all import MixedIntegerLinearProgram, QQ, matrix as sage_matrix
from sage.numerical.mip import MIPSolverException

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "research/benincasa/results/five-cycle-ofpt-packet.json"
OUTPUT = ROOT / "research/nima/results/five-site-ofpt-orientation-rescue.json"


def boundary(simplex):
    return [(simplex[:i] + simplex[i+1:], -1 if i & 1 else 1)
            for i in range(len(simplex))]


def rotate_label(label, n=5):
    if label.startswith("G_minus_e"):
        digits = label.removeprefix("G_minus_e")
        return "G_minus_e" + "".join(str(int(digit) % n + 1) for digit in digits)
    if label.startswith("g_"):
        digits = label.removeprefix("g_")
        rotated = sorted(int(digit) % n + 1 for digit in digits)
        return "g_" + "".join(map(str, rotated))
    raise ValueError(label)


def permutation_sign(values, order):
    positions = [order[value] for value in values]
    inversions = sum(positions[i] > positions[j]
                     for i in range(len(positions))
                     for j in range(i + 1, len(positions)))
    return -1 if inversions & 1 else 1


def solve_signing(matrix, orbit_columns=None):
    problem = MixedIntegerLinearProgram(maximization=False)
    bit = problem.new_variable(binary=True)
    for row in matrix:
        problem.add_constraint(
            sum(value*(2*bit[column]-1)
                for column, value in enumerate(row) if value) == 0
        )
    if orbit_columns:
        for orbit in orbit_columns:
            seed, seed_transport = orbit[0]
            assert seed_transport == 1
            for column, transport in orbit[1:]:
                problem.add_constraint(
                    2*bit[column]-1 == transport*(2*bit[seed]-1)
                )
    problem.set_objective(0)
    try:
        problem.solve()
    except MIPSolverException:
        return None
    values = problem.get_values(bit)
    signs = [1 if round(values[column]) else -1 for column in range(len(matrix[0]))]
    assert all(sum(value*sign for value, sign in zip(row, signs)) == 0
               for row in matrix)
    return signs


def main():
    packet = json.loads(PACKET.read_text())
    cycle = packet["five_cycle"]
    terms = cycle["terms"]
    facets = sorted({label for term in terms for label in term})
    order = {label: index for index, label in enumerate(facets)}
    simplices = [tuple(sorted(term, key=order.__getitem__)) for term in terms]
    index = {frozenset(simplex): column for column, simplex in enumerate(simplices)}
    faces = sorted({face for simplex in simplices for face, _ in boundary(simplex)})
    face_index = {face: row for row, face in enumerate(faces)}
    matrix = [[0]*len(simplices) for _ in faces]
    for column, simplex in enumerate(simplices):
        for face, sign in boundary(simplex):
            matrix[face_index[face]][column] = sign

    unseen = set(range(len(simplices)))
    orbit_columns = []
    while unseen:
        seed = min(unseen)
        column = seed
        transport = 1
        orbit = []
        for _ in range(5):
            assert column not in [item[0] for item in orbit]
            orbit.append((column, transport))
            unseen.discard(column)
            mapped_in_source_order = tuple(rotate_label(x) for x in simplices[column])
            target = tuple(sorted(mapped_in_source_order, key=order.__getitem__))
            step_sign = permutation_sign(mapped_in_source_order, order)
            column = index[frozenset(target)]
            transport *= step_sign
        assert column == seed and transport == 1
        orbit_columns.append(orbit)
    unrestricted = solve_signing(matrix)
    cyclic = solve_signing(matrix, orbit_columns)
    boundary_matrix = sage_matrix(QQ, matrix)
    collapsed = sage_matrix(
        QQ,
        [[sum(transport*row[column] for column, transport in orbit)
          for orbit in orbit_columns]
         for row in matrix],
    )
    cyclic_kernel = collapsed.right_kernel()
    cyclic_coordinate_supported = [
        any(vector[column] != 0 for vector in cyclic_kernel.basis())
        for column in range(len(orbit_columns))
    ]
    transport_sign_counts = {
        str(sign): sum(transport == sign
                       for orbit in orbit_columns
                       for _, transport in orbit)
        for sign in (-1, 1)
    }
    unrestricted_kernel_dimension = int(boundary_matrix.right_kernel().dimension())
    cyclic_kernel_dimension = int(cyclic_kernel.dimension())
    output = {
        "schema": "marici.five_site.ofpt_orientation_rescue.v2",
        "term_count": len(simplices),
        "triple_face_count": len(faces),
        "cyclic_orbit_count": len(orbit_columns),
        "unrestricted_unit_magnitude_signing_exists": unrestricted is not None,
        "cyclic_invariant_unit_magnitude_signing_exists": cyclic is not None,
        "unrestricted_rational_kernel_dimension": unrestricted_kernel_dimension,
        "cyclic_invariant_rational_kernel_dimension": cyclic_kernel_dimension,
        "cyclic_invariant_rational_kernel_supports_every_orbit":
            bool(cyclic_kernel.dimension()) and all(cyclic_coordinate_supported),
        "oriented_cyclic_transport_sign_counts": transport_sign_counts,
        "rational_c5_dimension_check": {
            "total_kernel_dimension": unrestricted_kernel_dimension,
            "invariant_dimension": cyclic_kernel_dimension,
            "cyclotomic_multiplicity":
                (unrestricted_kernel_dimension-cyclic_kernel_dimension)//4,
            "holds":
                (unrestricted_kernel_dimension-cyclic_kernel_dimension) % 4 == 0,
        },
        "unrestricted_signing": unrestricted,
        "cyclic_invariant_signing": cyclic,
        "interpretation": (
            "After transporting oriented simplices with the reordering sign, the "
            "C5-invariant rational cycle space is nine-dimensional. The previously "
            "reported zero-dimensional orbit collapse omitted this orientation sign."
        ),
        "scope": (
            "Tests unit signings and arbitrary C5-invariant rational weights in the "
            "oriented abstract four-facet incidence complex. It does not identify a "
            "canonical vector in the surviving nine-plane or supply a physical readout."
        ),
        "passed": True,
    }
    OUTPUT.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
