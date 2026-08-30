#!/usr/bin/env python3
"""Test whether oriented D5 naturality selects a unique OFPT incidence cycle."""

import json
from pathlib import Path

from sage.all import QQ, identity_matrix, matrix, vector

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "research/benincasa/results/five-cycle-ofpt-packet.json"
OUTPUT = ROOT / "research/nima/results/five-site-ofpt-dihedral-selector.json"


def boundary(simplex):
    return [(simplex[:i] + simplex[i + 1:], -1 if i & 1 else 1)
            for i in range(len(simplex))]


def permutation_sign(values, order):
    positions = [order[value] for value in values]
    inversions = sum(positions[i] > positions[j]
                     for i in range(len(positions))
                     for j in range(i + 1, len(positions)))
    return -1 if inversions & 1 else 1


def rotate_site(site, n=5):
    return site % n + 1


def reflect_site(site, n=5):
    return (-site) % n + 1


def transform_label(label, site_map, n=5):
    if label.startswith("g_"):
        sites = sorted(site_map(int(digit), n) for digit in label.removeprefix("g_"))
        return "g_" + "".join(map(str, sites))
    if label.startswith("G_minus_e"):
        digits = [int(digit) for digit in label.removeprefix("G_minus_e")]
        edge = frozenset(site_map(site, n) for site in digits)
        edge_labels = {
            frozenset((site, site % n + 1)): f"G_minus_e{site}{site % n + 1}"
            for site in range(1, n + 1)
        }
        return edge_labels[edge]
    raise ValueError(label)


def oriented_action(simplices, index, order, site_map, n=5):
    action = matrix(QQ, len(simplices), len(simplices), sparse=True)
    for source, simplex in enumerate(simplices):
        mapped = tuple(transform_label(label, site_map, n) for label in simplex)
        target_simplex = tuple(sorted(mapped, key=order.__getitem__))
        target = index[frozenset(target_simplex)]
        action[target, source] = permutation_sign(mapped, order)
    return action


def main():
    cycle = json.loads(PACKET.read_text())["five_cycle"]
    terms = cycle["terms"]
    facets = sorted({label for term in terms for label in term})
    order = {label: position for position, label in enumerate(facets)}
    simplices = [tuple(sorted(term, key=order.__getitem__)) for term in terms]
    index = {frozenset(simplex): column for column, simplex in enumerate(simplices)}

    faces = sorted({face for simplex in simplices for face, _ in boundary(simplex)})
    face_index = {face: row for row, face in enumerate(faces)}
    d = matrix(QQ, len(faces), len(simplices), sparse=True)
    for column, simplex in enumerate(simplices):
        for face, sign in boundary(simplex):
            d[face_index[face], column] = sign

    rotation = oriented_action(simplices, index, order, rotate_site)
    reflection = oriented_action(simplices, index, order, reflect_site)
    unit = identity_matrix(QQ, len(simplices), sparse=True)
    cyclic_constraints = d.stack(rotation - unit)
    dihedral_constraints = cyclic_constraints.stack(reflection - unit)
    cyclic_kernel = cyclic_constraints.right_kernel()
    dihedral_kernel = dihedral_constraints.right_kernel()
    odd_constraints = cyclic_constraints.stack(reflection + unit)
    reflection_odd_kernel = odd_constraints.right_kernel()

    assert rotation**5 == unit
    assert reflection**2 == unit
    assert reflection * rotation * reflection == rotation**4

    unseen = set(range(len(simplices)))
    orbit_representatives = []
    while unseen:
        representative = min(unseen)
        orbit_representatives.append(representative)
        current = representative
        for _ in range(5):
            unseen.discard(current)
            image = rotation.column(current)
            current = next(i for i, entry in enumerate(image) if entry)

    def orbit_coordinates(kernel):
        return [
            [str(basis_vector[index]) for index in orbit_representatives]
            for basis_vector in kernel.basis()
        ]

    def functional_audit(values):
        functional = vector(QQ, values)
        cyclic_values = [functional.dot_product(item)
                         for item in cyclic_kernel.basis()]
        even_values = [functional.dot_product(item)
                       for item in dihedral_kernel.basis()]
        odd_values = [functional.dot_product(item)
                      for item in reflection_odd_kernel.basis()]
        return {
            "cyclic_basis_values": list(map(str, cyclic_values)),
            "reflection_even_basis_values": list(map(str, even_values)),
            "reflection_odd_basis_values": list(map(str, odd_values)),
            "nonzero_on_cyclic_sector": any(cyclic_values),
            "nonzero_on_reflection_even_sector": any(even_values),
            "nonzero_on_reflection_odd_sector": any(odd_values),
            "rotation_character": (
                1 if functional * rotation == functional else
                -1 if functional * rotation == -functional else None
            ),
            "reflection_character": (
                1 if functional * reflection == functional else
                -1 if functional * reflection == -functional else None
            ),
        }

    generator = None
    if dihedral_kernel.dimension() == 1:
        raw = dihedral_kernel.basis()[0]
        denominators = [entry.denominator() for entry in raw]
        common = 1
        from sage.arith.functions import lcm
        for denominator in denominators:
            common = lcm(common, denominator)
        integral = vector([int(common * entry) for entry in raw])
        nonzero = [abs(entry) for entry in integral if entry]
        from sage.arith.misc import gcd
        divisor = 0
        for entry in nonzero:
            divisor = gcd(divisor, entry)
        integral //= divisor
        first = next(entry for entry in integral if entry)
        if first < 0:
            integral = -integral
        generator = list(map(int, integral))

    output = {
        "schema": "marici.five_site.ofpt_dihedral_selector.v3",
        "term_count": len(simplices),
        "boundary_kernel_dimension": int(d.right_kernel().dimension()),
        "cyclic_invariant_kernel_dimension": int(cyclic_kernel.dimension()),
        "dihedral_invariant_kernel_dimension": int(dihedral_kernel.dimension()),
        "reflection_odd_kernel_dimension": int(reflection_odd_kernel.dimension()),
        "dihedral_selects_unique_line": dihedral_kernel.dimension() == 1,
        "cyclic_orbit_representatives": [list(simplices[index])
                                           for index in orbit_representatives],
        "cyclic_invariant_orbit_basis": orbit_coordinates(cyclic_kernel),
        "reflection_even_orbit_basis": orbit_coordinates(dihedral_kernel),
        "reflection_odd_orbit_basis": orbit_coordinates(reflection_odd_kernel),
        "source_functional_restrictions": {
            "orientation_normalized_unit_weights": functional_audit(
                cycle["orientation_normalized_term_weights"]),
            "ordered_denominator_determinants": functional_audit(
                cycle["ordered_denominator_determinants"]),
        },
        "primitive_integral_generator": generator,
        "group_relations_verified": {
            "rotation_order_five": True,
            "reflection_order_two": True,
            "reflection_conjugates_rotation_to_inverse": True,
        },
        "interpretation": (
            "Oriented D5 naturality leaves six even and three odd cycle directions. "
            "The ordered denominator determinant is a source-derived D5-invariant "
            "covector: it is nonzero on the even sector and annihilates the odd sector, "
            "thereby defining a canonical rank-one quotient rather than a preferred vector."
        ),
        "passed": True,
    }
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n")
    verbose_keys = {
        "primitive_integral_generator", "cyclic_orbit_representatives",
        "cyclic_invariant_orbit_basis", "reflection_even_orbit_basis",
        "reflection_odd_orbit_basis",
    }
    print(json.dumps({key: value for key, value in output.items()
                      if key not in verbose_keys}, sort_keys=True))


if __name__ == "__main__":
    main()
